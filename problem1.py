accounts = [[1,2,3],[3,2,1]]
max = 0
for i in accounts:
    if sum(i) > max:
        max = sum(i)
print(max)