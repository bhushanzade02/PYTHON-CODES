with open('235.txt', 'r') as rf:
    with open('237.txt', 'w') as wf:
        wf.write(rf.read())
        