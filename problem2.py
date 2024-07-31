words = ["leet","code"]
x = "e"
out = []
for i in range(len(words)):
    if x in words[i]:
        out.append(i)
print(out)