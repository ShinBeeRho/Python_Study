n = int(input("별의 개수 : ")) #순서대로
i = 0
while i < n :  
    i+=1
    print("*"*i)
        
n = int(input("별의 개수 : "))  #거꾸로
i = 0
while i < n :
    print("*"*(n-i))
    i+=1        
    
n = int(input("별의 개수 : ")) #오른쪽 정렬 순서대로
i = 0
while i < n :
    i+=1
    print(" "*(n-i),end='')
    print("*"*i)

n = int(input("별의 개수 : ")) #오른쪽 정렬 거꾸로
i = 0
while i < n :
    print((" "*i) + ("*"*(n-i)))
    i+=1

  
  