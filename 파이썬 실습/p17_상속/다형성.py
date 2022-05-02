class Factory :
    
    def start(self):    #부모 클래스에서 정의만 해둔 후
        pass
    
class ComputerFactory(Factory) :
    
    def start(self):    #자식 클래스에서 구체화
        print('컴퓨터 생산 라인을 가동합니다')
        
class AirConditionerFactory(Factory) :
    
    def start(self):
        print("에어컨 생산 라인을 가동합니다.")
    
factoryList = list()

cf = ComputerFactory()
af = AirConditionerFactory()


factoryList.append(cf)
factoryList.append(af)

for factory in factoryList:
    factory.start()
    