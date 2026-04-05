dict ={
    "table":[" a piece of furniture","list of facts & figure"],
    "cat":"a small animal"
    }
# 2
print(dict)

subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(subjects))
#3
marks = {}

x = int(input("enter phy : "))
marks.update({"phy":x})
y = int(input("enter math : "))
marks.update({"math":y})
z = int(input("enter chem : "))
marks.update({"chem":z})
print(marks)

#4
values = {9,"9.0"}
print(values)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)