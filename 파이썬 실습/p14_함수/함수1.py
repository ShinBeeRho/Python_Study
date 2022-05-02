def lastName(name):
    if name[0] == "김" :
        print(f"{name}님은 김씨입니다.")
    else :
        print(f"{name}님은 김씨가 아닙니다.")


names = ["김가나","이다라","박마바","김사아","송자차","강카타"]

for name in names :
    lastName(name)
    
    
# 내장함수  : python 설치하면서 바로 같이 사용할 수 있는 것
# 외장함수  : import등을 써서 불러오는 함수  
# 사용자 지정함수   :def 처럼 지정해서 사용하는 함수


def add(x, y):
    return x + y
print(add(10, 20))

#입력값이 없는 함수
def say():
    return "Hi"
print(say())

#출력값이 없는 함수
def show(str):
    print(str)
show("출력값이 없는 함수")

#입출력 모두 없는 함수
def printInfo():
    print("이름 : 노신비")
printInfo()

#return값이 없으면 None
test2 = printInfo()
print(test2)   