# print the list of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
# traverse
idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1

# Search for a number x in this tuple using loop :
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums) :
    if(nums[i] == x):
     print("FOUND at idx" , i)
    else:
       print("finding..")
    i += 1

