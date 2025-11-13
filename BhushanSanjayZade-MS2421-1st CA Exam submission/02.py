import numpy as np

# Step 1: Take input for rows and columns ---

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter array values row by row (type 'nan' for missing values):")

# Step 2: Take input row by row ---
data = []
for i in range(rows):
    row_values = []
    for j in range(cols):
        val = input(f"Enter value for element [{i+1},{j+1}]: ")
        if val.lower() == "nan":
            row_values.append(np.nan)
        else:
            row_values.append(float(val))
    data.append(row_values)

#  Convert list of lists into numpy array
arr = np.array(data, dtype=float)

# Step 1: Compute column-wise mean (ignoring NaNs)
col_mean = np.nanmean(arr, axis=0)

# Step 2: Find indices of NaNs
inds = np.where(np.isnan(arr))

# Step 3: Replace NaNs with corresponding column mean
arr[inds] = np.take(col_mean, inds[1])

print("\nArray after replacing NaNs:")
print(arr)
