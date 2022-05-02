# 최대값, 최소값
# num1, num2, num3 정수 3개 입력받는다.
# madeMax(_num1, _num2, _num3)
# madeMin(_num1, _num2, _num3)

# 최대값 : 00 
# 최소값 : 00

def madeMax(_num1, _num2, _num3):
    if _num1 > _num2 and _num1 > _num3:
        return _num1
    elif _num2 > _num1 and _num2 > _num3:
        return _num2
    else :
        return _num3
    
def madeMin(_num1, _num2, _num3) :
    if _num1 < _num2 and _num1 < _num3:
        return _num1
    elif _num2 < _num1 and _num2 < _num3:
        return _num2
    else :
        return _num3
    
    
num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))
num3 = int(input("세번째 정수 : "))
min = madeMin(num1,num2,num3)
max = madeMax(num1,num2,num3)
print(f"최대값 : {max}")
print(f"최소값 : {min}")