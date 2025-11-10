# -*- coding: utf-8 -*-
import numpy as np
import math
from typing import List, Tuple

# ----------------------------
# Utility: build forward diff table
# ----------------------------
def forward_diff_table(y: List[float]) -> np.ndarray:
    """
    Build forward difference table as a 2D array.
    table[0] = y (level 0), table[1] = first differences, etc.
    """
    n = len(y)
    table = np.zeros((n, n))
    table[0, :n] = y
    for level in range(1, n):
        for i in range(n - level):
            table[level, i] = table[level - 1, i + 1] - table[level - 1, i]
    return table

# ----------------------------
# Evaluate Newton forward polynomial using forward difference table
# ----------------------------
def newton_forward_interpolate(x0: float, h: float, y: List[float], target_x: float) -> float:
    """
    Newton's forward interpolation.
    x0: x of the first sample (index 0)
    h: spacing between x values (must be constant)
    y: list of y-values (y0, y1, ..., y_{n-1})
    target_x: the x where you want estimate
    """
    n = len(y)
    table = forward_diff_table(y)
    p = (target_x - x0) / h
    result = table[0, 0]
    # incremental p-product for terms p*(p-1)*(p-2)...
    p_prod = 1.0
    for k in range(1, n):
        p_prod *= (p - (k - 1))
        term = (p_prod / math.factorial(k)) * table[k, 0]
        result += term
    return result

# ----------------------------
# Newton backward interpolation
# ----------------------------
def backward_diff_table(y: List[float]) -> np.ndarray:
    """
    Build backward difference table arranged so that table[0,-1] = y_n, etc.
    We'll compute using forward differences but use reversed indexing.
    """
    # simplest: reverse y and reuse forward table
    y_rev = list(reversed(y))
    tbl_rev = forward_diff_table(y_rev)
    # keep reversed table for convenience
    return tbl_rev

def newton_backward_interpolate(xn: float, h: float, y: List[float], target_x: float) -> float:
    """
    Newton's backward interpolation centered at xn (x of last sample).
    xn: x coordinate of last sample (index n-1)
    h: spacing
    y: list of y-values
    """
    n = len(y)
    tbl_rev = backward_diff_table(y)  # table built using reversed y
    p = (target_x - xn) / h  # typically negative if target_x < xn
    result = tbl_rev[0, 0]  # this is y_n (last original y)
    p_prod = 1.0
    for k in range(1, n):
        p_prod *= (p + (k - 1))
        term = (p_prod / math.factorial(k)) * tbl_rev[k, 0]
        result += term
    return result

# ----------------------------
# Central interpolation using symmetric points (for Gauss/Stirling style)
# ----------------------------
def central_interpolate(x: List[float], y: List[float], target_x: float, window: int = 2) -> float:
    """
    Central interpolation: choose symmetric window around target_x with 2*window+1 points,
    fit polynomial of degree 2*window and evaluate at target_x.
    x: array of x positions (equal spaced)
    y: array of y values (same length)
    window: number of points on each side of center (e.g., window=2 uses 5 points total)
    """
    n = len(x)
    # find index of nearest x to target_x
    idx_center = int(np.argmin(np.abs(np.array(x) - target_x)))
    # pick symmetric indices
    left = max(0, idx_center - window)
    right = min(n - 1, idx_center + window)
    # if edges clipped, try to expand on the other side
    while (right - left) < 2 * window:
        if left > 0:
            left -= 1
        elif right < n - 1:
            right += 1
        else:
            break
    xs = np.array(x[left:right + 1])
    ys = np.array(y[left:right + 1])
    # fit polynomial (degree = len(xs)-1) but we can limit degree if needed
    deg = len(xs) - 1
    coeffs = np.polyfit(xs, ys, deg)
    value = np.polyval(coeffs, target_x)
    return value

# ----------------------------
# Helpers: example parse / use
# ----------------------------
def example_usage():
    # synthetic sample (equally spaced 16-day)
    # let x be day-of-year: 153, 169, 185, 201, 217  (example 16-day spaced)
    x = [153, 169, 185, 201, 217]
    y = [0.40, 0.45, 0.50, 0.52, 0.55]  # NDVI values (already scaled)
    h = x[1] - x[0]  # should be 16
    # target: day 177 (between 169 and 185)
    t = 177.0

    nf = newton_forward_interpolate(x0=x[0], h=h, y=y, target_x=t)
    nb = newton_backward_interpolate(xn=x[-1], h=h, y=y, target_x=t)
    central_5 = central_interpolate(x, y, t, window=2)  # uses 5 points (2 each side)

    print("Newton Forward estimate at", t, "=", nf)
    print("Newton Backward estimate at", t, "=", nb)
    print("Central (5-point polynomial) at", t, "=", central_5)

if __name__ == "__main__":
    example_usage()
