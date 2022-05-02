class 아부지 :
    carModel = ""
    carColor = ""
    
    def showCarInfo(self):
        self.carColor = "화이팅"
        print('[차량정보')
        print(f"차량모델 : {self.carModel}")
        print(f"차량 셍긱 : {self.carColor}")
        
        
class 자식(아부지):
            def showCarInfo(self):
                self.carColor = '블랙'
                print("[차량정보]")
                print(f"차량 색상 : {self.carColor}")
                
신비 = 자식()
신비.carModel = '소나타'
신비.showCarInfo()