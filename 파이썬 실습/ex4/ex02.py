def madeGrade(_score, _time):
    i = 0
    totalScore = 0
    totalTime = 0
    while i < len(_score):
        totalTime += _time[i]
        if _score[i] == 'A+':
            totalScore += (4.5 * _time[i])    
        elif _score[i] == 'A':
            totalScore += (4.0 * _time[i])    
        elif _score[i] == 'B+':
            totalScore += (3.5 * _time[i])    
        elif _score[i] == 'B':
            totalScore += (3.0 * _time[i])    
        elif _score[i] == 'C+':
            totalScore += (2.5 * _time[i])    
        elif _score[i] == 'C':
            totalScore += (2.0 * _time[i])    
        elif _score[i] == 'D+':
            totalScore += (1.5 * _time[i])    
        elif _score[i] == 'D':
            totalScore += (1.0 * _time[i])    
        else:
            totalScore = totalScore + 0
        i += 1
        
        
    return totalScore, totalTime

count = 0
score = list()
time = list()


while count < 5 :    
    score.append(input("평점 : "))
    time.append(int(input("이수 학점 : ")))
    count += 1

totalScoreAndTotalTime = madeGrade(score, time)
# print(f"TotalScore : {totalScoreAndTotalTime[0]}")
# print(f"TotalTime : {totalScoreAndTotalTime[1]}")
print(f"총 평점은 {totalScoreAndTotalTime[0]/totalScoreAndTotalTime[1]}입니다.")