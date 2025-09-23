
# Modified Eulers Method // predictor corrector method // Heun's Method

def function(x, y):
    return y - (x**2) + 1 

# Input values
x0 = float(input("Enter the value of x0 : "))
y0 = float(input("Enter the value of y0 : "))
h  = float(input("Enter the step size h : "))
x  = float(input("Enter value of x to compute y : "))


x_curr = x0
y_curr = y0

print("\nModified Euler's Method Table")
print("-------------------------------------------------------")
print(f"{'x':<10}{'y (pred)':<15}{'y (corr)':<15}{'Final y':<15}")
print("-------------------------------------------------------")

while x_curr < x:
    # Predictor
    y_pred = y_curr + h * function(x_curr, y_curr)
    
    # Corrector
    y_corr = y_curr + (h/2) * (function(x_curr, y_curr) + function(x_curr + h, y_pred))
    
    # Print step
    print(f"{x_curr+h:<10.4f}{y_pred:<15.4f}{y_corr:<15.4f}{y_corr:<15.4f}")
    
    # Update values
    x_curr += h
    y_curr = y_corr


