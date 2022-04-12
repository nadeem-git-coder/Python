l =[10,10,20,10,33,10]
res=1
for i in range(1,len(l)):
    for j in range(0,i):

        if(l[i]==l[j]):
            res=res
        else:
            res = res + 1
    
    

print(res)