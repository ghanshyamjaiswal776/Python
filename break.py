# Break used to terminate the loop when encountered


nums = (1,4,9,16,25,36,49,64,81,100)
x= 36
i = 0
while i < len(nums) :
    if(nums[i]==x):
     print("Found at idx",i)
    break
else:
    print("finding..")
    idx += 1
print("end of loop")