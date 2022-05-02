string = ''
string = ''
f = open('p15_파일입출력/hello.txt','r',encoding = 'utf8')
string = f.readline()
string2 = f.readline()
f.close()

print(string, end='')
print(string2, end='')

print('=======================')
f = open('p15_파일입출력/hello.txt','r',encoding = 'utf8')
strList = f.readlines()
strList2 = list()
print(strList)
for string in strList :
    strList2.append(string.replace('\n',''))
    #string = string.strip()
    #string = string.replace('\n','') 도 가능
    print(string)
f.close()

print(strList)
print(strList2)

f = open('p15_파일입출력/hello.txt','r',encoding = 'utf8')
string = f.read()
f.close()
print(string)