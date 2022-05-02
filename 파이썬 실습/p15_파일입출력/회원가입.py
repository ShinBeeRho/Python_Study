# 이메일 : 
# 성명 :
# 사용자 이름 :
# 비밀번호 : 

#f = open('p15_파일입출력/회원가입.txt','w',encoding = 'utf8')


userList = list()

i = 0
while i < 2 :
    user = dict()
    email = input("이메일 : ")
    name = input("성명 : ")
    username = input("사용자 이름 : ")
    password = input("비밀번호 : ")

    print(f"이메일 : {email}")
    print(f"성명 : {name}")
    print(f"사용자 이름 : {username}")
    print(f"비밀번호 : {password}")

    user['email'] = email
    user['name'] = name
    user['username'] = username
    user['password'] = password

    userList.append(str(user))
    userList.append('\n')
    
    i += 1
    
print(userList)

with open('p15_파일입출력/user.txt','w',encoding = 'utf8') as f :
    f.writelines(userList)

