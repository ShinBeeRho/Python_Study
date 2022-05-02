# 예외 만들기

class CustomError(Exception):
    def __str__(self):
        return "우리가 만든 예외가 발생했습니다."

number = 0

try:
        
    if number == 0:
        raise CustomError()
    else:
        print("예외발생하지 않음")
        
except CustomError as e:
    print(f"Error 내용 : {e}")
    
