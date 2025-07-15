x= 5
def fun():
    x = 10 
    d = globals()
    print('x = %d y = %d'%(x,d['x']))

fun()