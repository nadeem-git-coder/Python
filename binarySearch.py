def binarySearch(arr,l,r,x):
    if(r>=l):
        mid= l+r//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        return -1

lst=[]
n = int(input("enter the size of array: "))
print("Enter the elements: \n")
for i in range(n):
    x=int(input())
    lst.append(x)

lst.sort()
print(lst)
key = int(input("Enter the element you want to search: "))
result =binarySearch(lst,0,len(lst)-1,key)
if result!=-1:
    print("Element found at index",result)
else:
    print("not found")