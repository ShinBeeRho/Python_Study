print('로그인 페이지')
username = input('사용자이름 : ')
password = input('비밀번호 : ')

userList = list()
with open('p15_파일입출력/user.txt','r',encoding = 'utf8') as f:
    while True :
        user = f.readline()
        if not user :
            break
        userList.append(user.strip())
    
loginFlag = False   #로그인 성공 및 실패
loginUser = dict()  

for user in userList :
    
    userDict = eval(user) #eval : list를 dict으로 바꿔준다
    if userDict.get("username") == username and userDict.get('password') == password : #로그인 성공 확인
        print(f'{username} 계정 로그인 성공')
        loginUser = userDict    #로그인 성공시 loginUser 에 해당 사용자의 데이터 저장 
        loginFlag = True
        break
if loginFlag == False : #로그인 실패시
    print('해당 계정으로 로그인 할 수 없습니다.')    
else:   #로그인 성공시
    _email = loginUser.get('email')
    _name = loginUser.get('name')
    _username = loginUser.get('username')
    _password = loginUser.get('password')
    
    print('\n[사용자 정보]')
    print(f'이메일 : {_email}')
    print(f'성명 : {_name}')
    print(f'사용자 이름 : {_username}')
    print(f'비밀번호 : {_password}')
    
    