def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("Number must be in int or floats")
    except:
        print("unexcept error")

print(divide(10,'2'))
        