#자료구조
#선형(리스트, 스택, 큐, 데크), 비선형(트리, 그래프)
#스택 LIFO(Last In First Out)
list1 = [10, 20, 30, 40, 50]
stack1 = []
stack1.append(list1.pop(0))

print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)

print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)



#큐 FIFO(First In First Out)
list2 = ["a","b","c","d","e"]
queue1 = []

queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)

print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))



#Q) list3의 가장 뒤에서 부터 pop을 해서 
#   list4에 삽입할 때 0번 인덱스에 삽입하고
#   list4에서 가장 나중에 들어온 것 부터 pop해서 출력

list3 = ["가","나","다","라","마"]
list4 = []
list4.insert(0,list3.pop())
print(list4)
list4.insert(0,list3.pop())
print(list4)
list4.insert(0,list3.pop())
print(list4)
list4.insert(0,list3.pop())
print(list4)
list4.insert(0,list3.pop())
print(list4)

print(list4.pop(0))
print(list4.pop(0))
print(list4.pop(0))
print(list4.pop(0))
print(list4.pop(0))

