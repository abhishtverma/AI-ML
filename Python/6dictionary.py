#it is mutable,unordered,no allow of duplicate key
dict={
    "key":"value",
    "name" : "abhisht",
    "age" : 21,
    "intrest" : "cricket",
    "is_adult" : True,
    "subject" : ("python","c","java"),#tuples
     12 : 15
    }
print(dict)
print(type(dict))
print(dict["name"])
dict["name"]="arin"#overwrite
print(dict)
dict["surname"]="verma"
print(dict)
null_dict={}
null_dict["name"]="saprit"
print(null_dict)
#nesting dictionary
dict2={
    "name" : "abhisht",
    "age" : 21,
    "subject" : {
        "phy":97,
        "chem":95,
        "math":99
    }
}
print(dict2)
print(dict2["subject"]["chem"])
#methods
print(len(dict2))#length of keys
pairs=list(dict2.items())
print(pairs[2])#print the pair of key and value of index
print(dict2.keys())#return all keys
print(dict2.values())#return all values
print(dict2.items())#return all (key,val) pairs as tuples
print(dict2.get("subject"))#return the key according to value
dict2.update({"city":"delhi"})#insert the specific item to dictionary
print(dict2)