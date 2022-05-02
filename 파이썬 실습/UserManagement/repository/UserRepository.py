class UserRepository:
    
    dataBase = None
    
    def __init__(self, dataBase):
        self.dataBase = dataBase
        
        
    def insertUser(self, user):
        data = self.dataBase.getData()
        data.get("user_mst").append(user.toDict())
        self.dataBase.save()
        
        
    def getUserByUsername(self, username):
        data = self.dataBase.getData()
        print(data)
        userList = data.get("user_mst")
        for user in userList:
            if user.get("username") == username:
                return user
            
        return None
    
    def getUserListAll(self):
        data = self.dataBase.getData()
        userList = data.get("user_mst")
        return userList
    