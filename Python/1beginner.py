name = "Abhisht"
age = 23
value = 69.69
old = False

print(name)

#datatype
print(type(name))
print(type(value))
print(type(old))

#sum
a=7
b=3
print (a+b)
print (a ** b) #a^b
 #logical operator
print(not(a>b)) #gives opposite answer
c= True
d= False
print(c and d) #And operator-gives true answer when both are same
print(c or d) #Or operator-gives true when any of value is true

#type conversion- converts datatype automatically 
e=4
f=5.5
print(e+f)
#type casting- converts datatype forcefully
g=int("2") #2 is string here
h=4.5
print(g+h)
i=str("3")
print(type(i))

#input *all the input in python are in string type
value=input("enter any value:")
print("your value",value)
print(type(value))
#if we have to specify the type of input
#if we want only such type of input
value=int (input("enter any value:"))
print("your value",value)
print(type(value))