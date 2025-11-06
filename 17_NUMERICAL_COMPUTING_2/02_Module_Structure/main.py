# from methods import DiffEquation
# from func import call_function
# # from methods import call_function

# if __name__ == "__main__":

#     print("___Differential Equation Solver___\n")

#     x0 = float(input(" x0: "))
#     y0 = float(input(" y0: "))
#     h = float(input(" h : "))
#     x_end = float(input(" x target: "))
#     fstring = input("Enter f'(x, y): ")

#     f = call_function(fstring)
#     de = DiffEquation(x0, y0, h, x_end)

#     print("\n" )
#     print("="*50)
#     eul = de.euler(f)
#     print(f" y({x_end}) by euler = {eul:.4f}")

#     print("\n")
#     print("="*50)
#     mod = de.mod_euler(f)
#     print(f" y({x_end}) by mod-euler = {mod:.4f}")

#     print("\n")
#     print("="*50)
#     rk4 = de.rk4(f)
#     print(f" y({x_end}) by rk4 = {rk4:.4f}")



#     print("\nxxxxxxx Program Completed xxxxxxxxxxx")



from methods import DiffEquation
from func import call_function
from methods import PowerMethod
import math

if __name__ == "__main__":

    # print("___Differential Equation Solver___\n")

    # x0 = float(input(" x0: "))
    # y0 = float(input(" y0: "))
    # h = float(input(" h : "))
    # x_end = float(input(" x target: "))
    # fstring = input("Enter f'(x, y): ")


    # f = call_function(fstring)

    
    # de = DiffEquation(x0, y0, h, x_end)

    # print("\n" + "=" * 50)
    # eul = de.euler(f)
    # print(f" y({x_end}) by Euler = {eul:.4f}")

    # print("\n" + "=" * 50)
    # mod = de.mod_euler(f)
    # print(f" y({x_end}) by Modified Euler = {mod:.4f}")

    # print("\n" + "=" * 50)
    # rk4 = de.rk4(f)
    # print(f" y({x_end}) by Runge-Kutta 4 = {rk4:.4f}")

    # print("\n" + "=" * 50)
    # choice = input("Do you want to plot Error vs h graph? (y/n): ").strip().lower()

    # if choice == "y":
    #     print("\nEnter the *true solution* y(x) for error comparison.")
    #     print("Example: (x+1)**2 - 0.5*math.exp(x)")
    #     y_true_str = input("Enter y(x): ")

    #     # Convert string to Python function
    #     def true_solution(x):
    #         return eval(y_true_str, {"x": x, "math": math})

    #     print("\nGenerating Error vs h plot...")
    #     de.plot_error_vs_h(f, true_solution)

    # print("\nxxxxxxx Program Completed xxxxxxxxxxx")
    
    
    
    print("\n--- Power Method Example ---")
    A = [[2, 1],
         [1, 3]]

    pm = PowerMethod(A)
    eigenvalue, eigenvector = pm.run()

    print(f"Dominant Eigenvalue: {eigenvalue:.6f}")
    print(f"Corresponding Eigenvector: {eigenvector}")
