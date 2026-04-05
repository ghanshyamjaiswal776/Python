# Lists is a built-in data type that store set of values . It can store elements of different types
marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.6
marks5 = 45.1

marks = [94.4,87.5,95.2,66.6,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student =["Karan" ,95.4,17,"Delhi"]
print(student)
student[0]="arjun"
print(student)
#list slicing
marks = [85,94,76,63,48]
print(marks[-3:-1])

#list method
list =[2,1,3]
list.append(4)
print(list)
list = [2,1,3]
print(list.append(4))
print(list.sort())
print(list)

my_list = ["banana","apple","mango"]
my_list.sort()
print(my_list)
list = ["a","d","f","b"]
print(list.sort())

print(list)
list = ["a","d","f","b"]
list.reverse()
print(list)

list = [2,1,3] 
list.insert(1,5)
print(list)

list = [2,1,3,1]
list.remove(1)
print(list)
 
list = [2,1,3,1]
list.pop(2)
print(list)