nums = [1,2,3,4]
ls = []
for i in range(0,len(nums),2):
    dona = nums[i]
    son = nums[i+1]
    ls += [son] * dona
print(ls)