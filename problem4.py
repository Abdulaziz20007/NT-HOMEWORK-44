sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
max = 0
for i in sentences:
    temp = 0
    for j in i:
        if j == ' ':
            temp += 1
    if max < temp: max = temp
print(max+1)