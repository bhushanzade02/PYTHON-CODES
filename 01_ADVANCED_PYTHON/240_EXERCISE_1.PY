with open('235.txt', 'r') as rf:
    with open('237.txt', 'a') as wf:
        for line in rf.readlines():
            name, salary = line.split(',')
            wf.write(f'{name}\'s salary is{salary}')