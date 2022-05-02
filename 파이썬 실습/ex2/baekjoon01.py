#변수 score 입력받기
#score가 0보다 작거나 100보다 크면 해당 점수는 계산할 수 없습니다.
#아니라면 A,B,C,D,E 학점을 계산하여 출력

score = int(input("점수 : "))

if score > 0 and score <= 100 :
    if score >= 90 :
        print("A학점")
    elif score >= 80 :
        print("B학점")
    elif score >= 70 :
        print("C학점")
    elif score >= 60 :
        print("D학점")
    else :
        print("F학점")
else :
    print("해당 점수는 계산할 수 없습니다.")
    
