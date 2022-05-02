from dataclasses import dataclass
import json

class DataBase:
    data = {
        "user_mst": list()
    }
    
    def __init__(self):
        try:
            with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/UserManagement/userdata.json","r", encoding = "utf8") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/UserManagement/userdata.json","w", encoding = "utf8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/UserManagement/userdata.json","r", encoding = "utf8") as f:
                data = json.load(f)
        
    def getData(self):
        return self.data
    
    def save(self):
            with open("C:/Users/노신비/OneDrive/바탕 화면/노신비/파이썬 실습/UserManagement/userdata.json","w", encoding = "utf8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
                
        