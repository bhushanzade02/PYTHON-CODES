# kwargs(keyword arguments)
# **kwargs(double star operator)



#kwargs as a paramter 


# def func(**kwargs):
#     print(kwargs)

# func(first_name='bhsuhan',last_name='zade')


def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")

func(first_name='bhsuhan',last_name='zade')