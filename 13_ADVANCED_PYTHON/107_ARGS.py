# create a function in which any nmber of args pass ded



def total_all(*args):
    total=0;
    for i in args:
        total += i;
    return total;



print(total_all(1,2,5,3,4,5))