from methods import DiffEquation
from func import call_function
# from methods import call_function

if __name__ == "__main__":

    print("________Differential Equation Solver__________\n")

    x0 = float(input(" x0: "))
    y0 = float(input(" y0: "))
    h = float(input(" h : "))
    x_end = float(input(" x target: "))
    fstring = input("Enter f'(x, y): ")

    f = call_function(fstring)
    de = DiffEquation(x0, y0, h, x_end)

    print("\n" )
    print("="*50)
    eul = de.euler(f)
    print(f" y({x_end}) by euler = {eul:.4f}")

    print("\n")
    print("="*50)
    mod = de.mod_euler(f)
    print(f" y({x_end}) by mod-euler = {mod:.4f}")

    print("\n")
    print("="*50)
    rk4 = de.rk4(f)
    print(f" y({x_end}) by rk4 = {rk4:.4f}")



    print("\nxxxxxxx Program Completed xxxxxxxxxxx")
