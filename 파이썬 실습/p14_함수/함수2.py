def add(x,y):
    print(f"x : {x}")
    print(f"y : {y}")
    return (x*2) + (y*3)

result = add(y = 10, x = 20)
print(result)

def add2(*args):
    for i in args :
        print(i)
        
add2(1,2,3,4,5,6,7,8,9)