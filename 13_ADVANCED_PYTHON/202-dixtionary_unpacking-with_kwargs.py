def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")

d = {'name': 'Siddhi', 'age': '21'}
func(**d)