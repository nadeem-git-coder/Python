l=[2,5,3,7,8,1,9]
a=[]
for i in range( len(l)):
    j=i-1
    while(j>=0 and l[j]>l[i]):
        j-=1
    if(j==-1):
        a.append(-1)
    else:
        a.append(l[j])

print(a)