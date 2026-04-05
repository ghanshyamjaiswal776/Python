# For loop are used  to sequential traversal. For traversing list,string,tuples etc
nums = [1,2,3,4,5]

for val in nums:
    print(val)

veggies = ["patato","brinjal","tamato","pea"]
for val in veggies:
    print(val)


tup = (1,2,3,4,5,6)
for val in tup:
    print(val)

str = "apnacollege"
for char in str:
    if (char == 'o'):
         print("o found")
         break
    print(char)
print("End")