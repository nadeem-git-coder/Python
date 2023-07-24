
def count(rowm,m):
    l =0
    h =len(rowm)-1
    while l<=h:
        mid = (l+h)>>1
        if (rowm[mid]<=m):
            l =mid+1
        else:
            h =mid-1
    return l
def median(matrix: [[int]], m: int, n: int) -> int:
    # Write your code here.
    l =1
    h = 10**9
    
    while l<=h:
        mid = (l+h)>>1
        cnt =0
        for i in range(m):
            cnt+= count(matrix[i],mid)
        if cnt<=((n*m)//2):
            l=mid+1
        else:
            h = mid-1
    return l

'''Example 1:
Input: 
r = 3 , c = 3
1 4 9 
2 5 6
3 8 7
Output: Median = 5
Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9
So, median = 5

Example 2:
Input: 
r = 3 , c = 3
1 3 8
2 3 4
1 2 5
Output: Median = 3
Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8
So, median = 3'''