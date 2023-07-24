def singleNonDuplicate(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        if(nums[0]!=nums[1]):
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low,high =1,n-2
        
        while low<=high:
            mid = (low+high)//2
            if(nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            # we are in left
            if ((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):
                low = mid+1
            #  we are in right
            else:
                high=mid-1
        return -1
'''Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10'''