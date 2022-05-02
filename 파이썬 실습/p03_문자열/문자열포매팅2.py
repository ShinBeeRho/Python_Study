str1 = "첫번째 수 {0} 두번째 수 {1} 두수의 합 {2}".format(10, 20, 10+20)
print(str1)

num1 = 10
num2 = 20
num3 = num1 + num2

str2 = "첫번째 수 {0} 두번째 수 {1} 두수의 합 {2}".format(num1,num2,num3)
print(str2)

str3 = "첫번째 수 {num1} 두번째 수 {num2} 두수의 합 {num3}".format(num1 = 10, num2 = 20 ,num3 = 10 + 20)

str4 = "문자열 포매팅 정렬 |{0:^10}| ".format("신비")
print(str4)

str5 = "문자열 포매팅 정렬 |{0:@^10}| ".format("신비")
print(str5)

str6 = "문자열 포매팅 정렬 |{0:@^10.4f}| ".format(3.15555)
print(str6)

str7 = "문자열 포매팅 정렬 {0} {{신비}} ".format("노")
print(str7)


