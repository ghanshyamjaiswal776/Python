# lecture 2 string and conditional statement
str1 = "This is a string.\t we are creating it in python"
str4 = "This is a string.\n we are creating it in python"
str2 = 'ApnaCollege'
str3 = """this is a string"""

"this is apna college's tutorials"
print(str1)
print(str4)

# concatenation add two string
str1 = "apna"
str2 ="college"
final_str = str1+" "+str2
print(final_str)
print(len(final_str))


str1 = "ghanshyam"
len1=len(str1)
print(len1)
str2 ="jaiswal"
len2 = len(str2)
print(len2)
final_str2=str1+" "+str2
print(final_str2)
print(len(final_str2))

# indexing 
str = "apna college"
ch = str[4]
print(ch)
str1 = "ghanshyam"
print(str1[3])

# slicing /accessing parts of a string
str = "apna college"
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]
# negative slicing
str = "apple"
print(str[-5:-2])

# string function
str = "i am from studying python from apnacollege"
print(str.endswith("ege"))
str = str.capitalize()
print(str)
print(str.replace("o","a"))
print(str.find("o"))
print(str.count("from"))
