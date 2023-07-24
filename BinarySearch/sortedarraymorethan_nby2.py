arr =[1,2,3,3,3,4,5,6]
low = 0
high = len(arr)-1

while low<=high:
    mid  = (low+high)//2
    if arr[mid]==arr[mid-1]:
        high=mid-1
    else:
        if arr[mid] < arr[mid-1]:
            low=mid+1
        else:
            high =mid-1
