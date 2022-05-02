#
#절대경로(경로 맨 앞에 / 또는 \로 시작하는 것)
#
#상대경로(./ 또는 ../또는 생략으로 시작하는 것)

strList = ['이름 : 노신비\n', '나이 : 29\n', '주소 : 김해시\n']

f = open('p15_파일입출력/hello.txt', 'w', encoding='utf8')
for string in strList:
    f.write(string)

f.writelines(strList) #write.lines : 리스트 출력시 자동 줄바꿈 및 출력

f.close()

