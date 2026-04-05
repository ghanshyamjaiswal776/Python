#WAP to check if a number entered by the user is odd or even
num = int(input("Enter the num :"))
if(num%2 == 0):
    print("Even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user
a = int(input("Enter the num :"))
b = int(input("Enter the num :"))
c = int(input("Enter the num :"))
if(a>=b and a>=c):
    print("first num is largest" ,a)
elif(b>=c):
    print("second num is largest",b)
else:
    print("third num is largest",c)

# WAP to check is a number is a multiple of 7 or not
x = int(input("Enter the num :"))
if(x%7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
