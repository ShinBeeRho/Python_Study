dan = 0
num = 0
result = 0

while dan < 9 :
    dan+=1
    print(f"{dan}단")
    while num < 9:
        num+=1
        result = dan*num
        print(f"{dan} X {num} = {result}")
    print()
    num = 0
    