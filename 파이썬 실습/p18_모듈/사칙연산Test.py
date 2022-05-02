# from 사칙연산 import sum, div   #from 파일명 import 함수
# print(sum(10,20,30,40)) #함수명만으로 사용가능
# print(div(100,20,2))

import 사칙연산 #import 파일명
print(사칙연산.sum(10,20,30,40))    #파일명.함수()로 사용
print(사칙연산.div(100,20,2))

import 사칙연산 as a #import 파일명 as 별명
#as = 알리아스 -> 별명
print(a.sum(10,20,30,40))    #별명.함수()로 사용가능
print(a.div(100,20,2))

print(a.getName())
print(a.__name__)


def sum(num1,num2):
    return num1 + num2

name = input("사용할 모듈을 입력하세요.")
if a.__name__ == name :
    print(a.sum(10, 20))
elif __name__ == name:
    print(a.sum(50, 20))