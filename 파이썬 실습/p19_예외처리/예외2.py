# 에러가 나도 정상적으로 프로그래밍을 종료시키기 위해서 except를 사용한다
number = -1

try:
    if number > 0:
        pass
    elif number ==-1:
        list1 = [1,2,3,4,5]
        list1.index(6)
    else:
        raise FileNotFoundError
except ValueError as e:
    print(f"오류내용: {e}")
except IndexError as e:
    print(f"오류내용: {e}")
except FileNotFoundError as e:
    print(f"오류내용: {e}")
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"오류내용: {e}")
else:
    print("오류가 발생하지 않으면 실행")
finally:     #무조건 실행
    print("무조건 실행")
    
print("프로그램종료")


