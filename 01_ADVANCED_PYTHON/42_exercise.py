name = "bhushan"

i = 0
tmp_var = ""
while i < len(name):
    if name[i] not in tmp_var:
        tmp_var += name[i]
        print(f'{name[i]}: {name.count(name[i])}')
        i += 1
        