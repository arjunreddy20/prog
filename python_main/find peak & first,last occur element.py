
class Solution:
    def Find_peak(self,nums):     
        le=len(nums)
        left=0
        right=le-1
        while left < right:
            mid=(left+right)//2
            if nums[mid] > nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left
    
x=Solution()
nums=list(map(int ,input("enter-with_space").split()))
print(x.Find_peak(nums))


'''You are Given an array Sorted in ascending order. Find the Starting and ending Position of a given Target value.
If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8    Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,8,8,8,8,10], target = 8   Output: [3,8]
Example 3:
Input: nums = [5,7,7,8,8,10], target = 6     Output: [-1,-1]
'''

class Things:
    def first_and_last(self,arr,k):         
                                                   
        def get_left(arr,k):
            left=0
            right=len(arr)-1
            first=-1
            while left <= right:
                mid=(left+right)//2
                if arr[mid] >= k:
                    right=mid-1    
                else:
                    left=mid+1
                if arr[mid]==k:
                    first=mid
            return first
        
        def get_right(arr,k):
            left=0
            right=len(arr)-1
            last=-1
            while left <= right:
                mid=(left+right)//2
                if arr[mid] <= k:
                    left=mid+1
                else:
                    right=mid-1
                if arr[mid]==k:
                    last=mid

            return last
        first=(get_left(arr,k))
        last=(get_right(arr,k))
        return [first,last]
    
a=Things()
nums=list(map(int ,input("enter-with_space= ").split()))
k=int(input("k= "))
result=a.first_and_last(nums,k)
print(result)
