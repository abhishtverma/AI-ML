#this is immutable and it will be in round bracket
marks=(1,3,3,5,7)
print(marks)
print(type(marks))
print(marks[1])
# marks[2]=5 it will show error bcz we cannot change value of any index
tup=(1,)#to create single value tuple
print(tup)
print(marks[1:3])
#methods
print(marks.index(3))
print(marks.count(3))