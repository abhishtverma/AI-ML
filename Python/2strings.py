str1="This is a String.\nIt is very good "
# \n is used for new line
# \t is used for tab space(5-6 space)
print(str1)
#concatenation
str2="abhi"
str3="verma"
print(str2+str3)
#length of string
print(len(str2))
#indexing
print(str3[2])
#slicing
print(str3[1:3])
#slicing from backward
print(str3[-3:-1])

print(str3.endswith("ma")) #return true if string ends with substring
print(str3.capitalize()) #make 1st character capital
print(str3.replace("v","k")) #replace word
print(str3.find("m")) #return 1st index of 1st occurence
print(str3.find("er")) #count the occurence of substring
