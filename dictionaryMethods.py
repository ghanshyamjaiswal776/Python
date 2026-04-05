student = {
    "name": "Ghanshyam",
    "subjects":{
        "phy":61,
        "maths" : 81,
        "chemistry" : 96
    }
}
print(len(student))
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[1])
#print(student["name2"])# error
print(student.get("name2")) # no error  method do not give error
new_dict = {"city" : "delhi","age":16}
student.update(new_dict)
print(student)