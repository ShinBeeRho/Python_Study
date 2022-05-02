#f문자열 포매팅
#python 3.6버전 이상부터 지원.

name = "노신비"
address = "김해시 주촌면"

str1 = f"이름 : {name:^10} {{name}}"
str2 = f"주소 : {address:>10}"

print(str1)
print(str2)
