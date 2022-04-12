s = "Tech int prep"
l = s.split(" ")
s=[]

for i in l:
    s.append(i)



for i in range(len(s)):
    print(s.pop(),end=" ")

