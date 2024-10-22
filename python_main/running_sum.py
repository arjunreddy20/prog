class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        running_sums = []
        for num in nums:
            running_sum += num
            running_sums.append(running_sum)
        return running_sums

# Read input and convert it to a list of integers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Create an instance of the Solution class and call the runningSum method
solution = Solution()
print(solution.runningSum(nums))
