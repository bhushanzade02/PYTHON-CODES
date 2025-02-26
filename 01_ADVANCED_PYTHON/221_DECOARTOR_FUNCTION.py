def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function ')
        any_function()
    return wrapper_function
 


@decorator_function
def func1():
    print("this is function 1")

func1()


# def func2():
#     print("this is function 2")




# var = decorator_function(func1)
# var()

# var2 = decorator_function(func2)
# var2()


# func1 = decorator_function(func1)
# func1()





