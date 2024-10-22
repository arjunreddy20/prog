
class Solution(object):
    def sortArray(self, nums):
        self.nums=nums
        n=len(nums)
        for i in range (n) :
            for j in range (0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums

solution=Solution()
nums=[-5,2,3,1,-411245,4548,-789,489,16269,-75168]
print(solution.sortArray(nums))
        