#immutable and collection of unordered items 
set1={1,2,2,11,4,"hello","world","world"}
print(set1)#remove duplicate items
print(type(set1))
print(len(set1))
set2=set() #to create empty sets
#method
set3=set()
set3.add(11)
set3.add(22)
set3.add(33)
set3.add((1,2,3))#tuples can be add 
#set3.add([1,2,3]) # we cannot add list and dictionary 
print(set3)
set3.remove(22)#remove the given value
print(set3)
print(set3.pop())#removes any random value
set3.clear()#clears the values
print(len(set3))
set4={5,6,11,1}
print(set1.union(set4))#union of two sets
print(set1.intersection(set4))#intersection of two sets
#if we want to save two same value we will make it a string
values={5,"5.0"}
print(values)

"""List = changeable ordered data.
Tuple = fixed ordered data.
Dictionary = key-value data.
Set = unique unordered data."""