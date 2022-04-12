nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m = 3
n = 3
i=0
j=0
c=[]
k=0
while(i<m and j<n):
    if(nums1[i]<=nums2[j]):
            c.append(nums1[i])
            i+=1
            
    else:
        c.append(nums2[j])
        j+=1
       
while(i<m):
        c.append(nums1[i])
        i+=1
while(j<n):
        c.append(nums2[j])
        j+=1
                


print(c)