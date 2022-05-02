import json

user_json = '''{
    "company" : "kakao",
    "users" : [{
        "usercode" : "20220001",
        "username" : "junil",
        "password" : "1234",
        "name" : "김준일",
        "email" : "skjil1218@kakao.com"
        },{
        "usercode" : "20220002",
        "username" : "junil2",
        "password" : "2222",
        "name" : "김준이",
        "email" : "skjil1212@kakao.com"
        }
    ]
}'''

user_json_obj = json.loads(user_json)

print(user_json_obj)
print(type(user_json_obj))
print(f'회사명: {user_json_obj.get("company")}')
userList = user_json_obj.get("users")
print(f'첫번째 사윈의 정보 : {userList[0]}')
print(f'두번째 사윈의 정보 : {userList[1]}')


