n = 1
sum = 0
while n<1001 :
    if n % 3 == 0 :
        sum += n
    n+=1
print(sum)

sum = 0
for i in range(1,1001):
    if i % 3 == 0:
        sum += i
print(sum)