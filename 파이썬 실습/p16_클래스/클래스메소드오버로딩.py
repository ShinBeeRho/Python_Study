from multipledispatch import dispatch
class User :
    username = ""
    password = ""
    name = ""
    
    # @->어노테이션
    @dispatch(str)
    def addUser(self, username) :
        self.username = username 
    
    @dispatch(str, str)
    def addUser(self, username, password):
        self.username = username
        self.password = password

    @dispatch(str, int)
    def addUser(self, username, password):
        self.username = username
        self.password = str(password)
        
    @dispatch(str, str, str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
   
    @dispatch(str, int, str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = str(password)
        self.name = name
    
    def showUserInfo(self):
        print(f"username : {self.username}")    
        print(f"password : {self.password}")    
        print(f"name : {self.name}")    
    
    user1 = User()
    user1.addUser("Shinbee")
    user1.showUserInfo()
    
    user2 = User()
    user2.addUser("Shinbee",1234)
    user2.showUserInfo()

    user3 = User()
    user3.addUser("Shinbee",1234, "노신비")
    user3.showUserInfo()

