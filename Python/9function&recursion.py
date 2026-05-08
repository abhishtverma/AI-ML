#function
def sum(a,b):
  s=a+b
  print(s)
  return s
sum(2,3)#1st calling
sum(4,7)#2nd calling
#or by this(function definition)
def w(a,b):
  s=a+b
  return s
sum=w(6,7)
print(sum)
#recursion
def show(n):
  if(n==0):
    return
  print(n)
  show(n-1)
show(5)
def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)
print(fact(5))