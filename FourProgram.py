#arthimetic operators
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b) #remainder
print(a**b) #a^b

#relationaloperator
a =50
b=20
print(a==b) #False
print(a !=b ) #True
print(a>=b)#True 
print(a>b)#True
print(a<=b)#False
print(a<b)#False

# assignment operators
num = 10
num = num+10
print("num :",num)#20
num = 10
num -= 10
print("num :",num) #0
num = 10
num *= 5
print("num :",num)
num = 10
num /= 5
print("num :",num)
num = 10
num %= 5
print("num :",num)
num = 10
num  **= 5
print("num :",num)

#logical operators
a = 50
b=30
print(not False)
print(not (a>b))

val1 = True
val2 = False
print ("NOT opertor :",val1 and val2)
print ("OR opertor :",val1 or val2)
print ("OR opertor :",(a==b) or (a>b))