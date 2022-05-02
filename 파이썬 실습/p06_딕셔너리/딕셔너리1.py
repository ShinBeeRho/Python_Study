dir1 = {
    'a' : 'python',
    'b' : 'java',
    'c' : 'c',
    'd' : 'html',
    'e' : 'css',
    'f' : 'javascript',
    'g' : 'json',
    'h' : [1,2,3,4,5,6,7]
}

hashtag = {
    '맛집' : {
        '지역' : {
            '기장' : ['얼크니손칼국수', '일등가'],
            '영도' : ['거인왕돈까스', '김밥천국'],
            '서면' : ['삼정타워', '먹담']
        
        },  
        '메뉴' : ['돈까스', '김밥', '소고기', '오리고기']  
    },
    '여행' : ['국내여행', '해외여행'],
    '카페' : ['스타벅스', '컴포즈', '이디야']
    
}

print(dir1)

print(dir1['d'])

print(dir1['h'])

print("맛집출력 : " + hashtag['맛집']['지역']['영도'][0])
#print(hashtag.맛집.지역.영도[0]) -- 오류남

dir2 = {
    'name' : '노신비',
    'phone' : '010-5620-8135',
    'email' : 'nsbee7@naver.com'
}

print(dir2.keys())

list1 = list(dir2.keys())   #리스트형으로 변환
print(list1)

list2 = []

list2.append(list1.pop(0))
list2.append(list1.pop(0))
list2.append(list1.pop(0))

print(list2)

list3 = list(dir2.values())

print(list3)

list4 = list(dir2.items())  #튜플
print(list4)
print(list4[0][0])   #인덱싱 가능

dir2.clear()    #clear

print(dir2)
list5 = hashtag.get('카페') #get
print(list5)
list5 = hashtag.get('운동','값이 없습니다.')  #없을경우 ,default값 입력가능
print(list5)

print('카페' in hashtag) #True or False 값 반환
print('운동' in hashtag)
