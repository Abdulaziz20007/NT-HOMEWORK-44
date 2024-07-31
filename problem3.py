nums = [2,5,1,3,4,7]
n = 3
ls = list()
for i in range(n):
    ls.append(nums[i])
    ls.append(nums[i+n])
print(ls)