import json

json_data = '''{
    "username": "junil",
    "password":"1234"
}
'''

user_data = json.loads(json_data)   # 문자열관련은 loads

print(user_data)
print(type(user_data))
print(user_data.get("username"))

with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/p22_JSON2/userdata.json","w", encoding="utf8") as f:
    json.dump(user_data, f, indent=2, ensure_ascii=False)
    

with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/p22_JSON2/userdata.json","r", encoding="utf8") as f:
    user_data = json.load(f)    # 파일관련은 load
    
print(user_data)

user_data_str = json.dumps(user_data)
print(user_data_str)

print(type(user_data_str))
