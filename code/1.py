arr =[1,4,5,6,3]
arr1=[2,4,8]

a=[]
for i in arr:
    a.append(i)

for i in arr1:
    if(i not in arr):
        a.append(i)
print(a)