def add(*args):
    #print(args)

    sum = 0
    for i in args:
        sum += i
    return sum

#print(add(1,2,4,5,6))

#**kwargs

def results(**kwargs):
    print(kwargs)
results( MSC = 4.0, HSC = 5.0, SSC = 5.0)