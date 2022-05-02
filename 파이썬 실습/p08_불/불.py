bool1 = True
bool2 = False

print(bool1)
print(bool2)

print(10>5)

#not 연산(부정)
#4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수인것

year = 2000 # True
#year = 1999 # False

result3 = (year%4==0) and (year%100!=0) or(year%400==0)

print(f"윤년 결과 : {result3}")

bool1 = True
