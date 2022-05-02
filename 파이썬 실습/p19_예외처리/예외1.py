strName = "김준일, 김기덕, 송지한, 전주홍"

print(strName.find("노신비"))
print(strName.find("노신비"))
try:    #파일 입출력시 반드시 예외처리를 해야함.
    print(strName.index("노신비"))
except:
    print("예외가 발생하였습니다.")
    

print("프로그램 정상 종료")

