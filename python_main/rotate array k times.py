'''
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

class Solution():
    def Rotate_array(arr,k):
        k=k % len(arr)
        for i in range(0,k):
            val=arr[0]
            for i in range(1,len(arr)):
                temp=val
                val=arr[i]
                arr[i]=temp
            arr[0]=val
        return arr
s=Solution()
arr=list(map(int, input("enter with spaces=").split()))
x=int(input())
print(s.Rotate_array(arr))

    
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        """Do not return anything, modify nums in-place instead."""
        k=k%len(nums)
        for i in range(0,k):
            variable=nums[0]
            for j in range(1,len(nums)):
                temp=variable
                variable=nums[j]
                nums[j]=temp
            nums[0]=variable
        return nums


            
    
    

#========== User's Code Ends Here ==========

   
    
    
def main():
    n=int(input())
    arr=[]
    s=input().split(" ")
    for i in range(0,n):
        arr.append(int(s[i]))
    s=Solution()
    k=int(input())
    s.rotate(arr,k)
    string =""
    for i in range(0,n):
        string =string + str(arr[i]) +" "
    print(string)
    
main()
'''