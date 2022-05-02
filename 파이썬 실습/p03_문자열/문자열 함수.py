#count함수

name = "노신비"

nameStrCount = name.count('노')

print(f"문자 김의 개수 : {nameStrCount}")

#find함수
address = "김해시 주촌면 천곡로"

cityIndex = address.find("시")
print(address[:cityIndex+1])

cityIndex = address.index("시")
print(address[:cityIndex+1]) 
#find는 못찾아도 오류가 나지않지만 index는 못찾을 경우 오류발생

meonIndex = address.find("면")
print(address[cityIndex+2:meonIndex+1])

roIndex = address.rfind("로")
print(address[meonIndex+2:roIndex+1])
#rfind는 오른쪽 부터 찾기

#join 함수(문자열 삽입)
name = "노신비"
nameJoin = " ".join(name)
print(nameJoin)

#upper합수(대문자 변환)
str1 = "Rho"
print(str1.upper())

#lower(소문자 변환)
str2 = str1.upper()
print(str2.lower())

#strip(공백 제거)
username = " nsbee7 "
lstripUsername = username.lstrip()
print("000" + lstripUsername + "000")

rstripUsername = username.rstrip()
print("000" + rstripUsername + "000")

stripUsername = username.strip()
print("000" + stripUsername + "000")

#replace(문자열바꾸기)
phoneNumber = "010-5620-8135"
replacePhone = phoneNumber.replace("-","")
print(replacePhone)

