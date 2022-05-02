marks = [90, 25, 67, 45, 80]

count = 0

for score in marks:
    count+=1
    if score >= 60:
        result = "합격"
    else :
        result = "불합격"
    
    
    print(f"{count}번 학생의 점수는 {score}점이라서 {result}입니다.")
    
    
count = 0
for score in marks:
    count +=1
    if score % 2 !=0 :
        continue
    print(f"{count}번 학생의 점수는 {score}이고 짝수 입니다")
    