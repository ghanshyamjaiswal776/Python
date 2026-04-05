# Dictionary are used to store data values in key:value pairs . They are unordered,mutable(changeable), and don't allow duplicate key
info = {
    
    "name" : "ghanshyam",
    "subjects":["python","java","C"],
    "topics" :("dicitonary","sets"),
    "learning" : "coding",
    "age": 21,
    "is_adult":True,
    "marks":94.4,
    12 : "True"
} 
print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
print(info["topics"])
info["name"]= "Aditya" # overwrite
info["surname"]= "Jaiswal"
print(info)

null_dic={

}
null_dic["name"] = "ghanshyam"
print(null_dic)