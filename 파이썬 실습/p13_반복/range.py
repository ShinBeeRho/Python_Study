# for i in range(1,11) : 
#     print("*"*i)

# for i in range(10, 0, -1) : 
#     print("*"*i)
    
n = int(input("n = "))

for i in range(1,n+1) :
    print(" "*(n-i) + "*" * i)
    
for i in range(1,n+1) :
    print(" " * i + "*" * (n-i))

for i in range(1, n+1):
    print(" " * (n-i)+ "*"*(i*2-1) + " " * (n-i))

for i in range(n, 0, -1):
    print(" " * (n-i)+ "*"*(i*2-1) + " " * (n-i))


