#lists(we can store element of any type)
marks=["arin",5.5,2,7.7]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
#in list we can mutate i.e. can change value
marks[0]="abhisht"
print(marks)
#sublist i.e. slicing of a part of list
print(marks[1:3])
#methods
list=[8,6,4,2]
list.append(10)#add element at end
print(list)
list.sort()#sorts in ascending order
print(list)
list.sort(reverse=True)#sorts in descending order
print(list)
list.reverse()#reverse
print(list)
list.insert(2,7)#insert element at end
print(list)
list.remove(6)#remove first occurence of element
print(list)
list.pop(3)#remove element of that index
print(list)
mist=list.copy()#copy the elements
print(mist)