def namesAndphones(names, phones):
    namesStr = ",".join(names)
    phonesStr = ",".join(phones)
    return namesStr, phonesStr

names = ["A","B","C","D","E"]
phones = ["1","2","3","4","5"]
result = namesAndphones(names, phones)
print(result)
    
result1, result2 = namesAndphones(names, phones)
print(result1)
print(result2)