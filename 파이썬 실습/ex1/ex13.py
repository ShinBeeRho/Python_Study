user = dict()

#강사 : list[
#   0-> 이름 : 김준일, 연락처 : 010-9988-1916, 나이 : 29, 주소 : 동래구    
#   1-> 이름 : 김준이, 연락처 : 010-9988-1917, 나이 : 30, 주소 : 부산진구    
#   ]
#학생 : list[
#   0-> 이름 : 노신비, 연락처 : 010-5620-8135, 나이 : 22, 주소 : 김해시    
#   1-> 이름 : 홍길동, 연락처 : 010-5620-8136, 나이 : 23, 주소 : 부산    
#]

user['강사'] = list()
user['학생'] = list()

user.get('강사').append(dict())
user_dtl1 = user.get('강사')[0]

user_dtl1['이름'] = "김준일"
user_dtl1['연락처'] = "010-9988-1916"
user_dtl1['나이'] = "29"
user_dtl1['주소'] = "동래구"

user.get('강사').append(dict())
user_dtl2 = user.get('강사')[1]
user_dtl2['이름'] = "김준이"
user_dtl2['연락처'] = "010-9988-1917"
user_dtl2['나이'] = "30"
user_dtl2['주소'] = "부산진구"

user.get('학생').append(dict())
user_dtl3 = user.get('학생')[0]
user_dtl3['이름'] = "노신비"
user_dtl3['연락처'] = "010-5620-8135"
user_dtl3['나이'] = "22"
user_dtl3['주소'] = "김해시"

user.get('학생').append(dict())
user_dtl4 = user.get('학생')[1]
user_dtl4['이름'] = "홍길동"
user_dtl4['연락처'] = "010-5620-8136"
user_dtl4['나이'] = "23"
user_dtl4['주소'] = "부산진구"

name1 = user.get('강사')[0].get('이름')
profile1 = user.get('강사')[0]
print(f"{name1} : {profile1}")

name2 = user.get('강사')[1].get('이름')
profile2 = user.get('강사')[1]
print(f"{name2} : {profile2}")

name3 = user.get('학생')[0].get('이름')
profile3 = user.get('학생')[0]
print(f"{name3} : {profile3}")

name4 = user.get('학생')[1].get('이름')
profile4 = user.get('학생')[1]
print(f"{name4} : {profile4}")


