import json

json_obj = {
    "id" : 20220001,
    "username": "junil",
    "password": "1234",
    "hobby": ["축구", "농구", "골프", "테니스"]
    
}
with open('C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/p22_json/user.json', 'w', encoding="utf8") as f:
    json_string = json.dump(json_obj, f, indent=4, ensure_ascii=False)
    
        