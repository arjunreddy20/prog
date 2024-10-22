arr=[[1,2,3],[1,4,3]]
max_sum=0
i=0
for i in range(0,len(arr),1):         #2D array initialize as first total array
    list_sum=0
    j=0
    for j in range (0,len(arr[i]),1):        # small for array in array
        list_sum=list_sum+arr[i][j]       #represents each element in small array
    if list_sum > max_sum:
        max_sum = list_sum
print(max_sum)






'''from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def maximumWealth(self, arr: List[List[int]]) -> int:
        max_sum=0
        i=0
        for i in range(0,len(arr),1):
            list_sum=0
            j=0
            for j in range (0,len(arr[i]),1):
                list_sum=list_sum+arr[i][j]
            if list_sum > max_sum:
                max_sum = list_sum
        return max_sum


       

#========== User's Code Ends Here ==========


    
    
    
    
    
def main():
    n=int(input())
    c=int(input())
    arr=[]
    for j in range(0,n):
        new_arr=[]
        s=input().split(" ")
        for i in range(0,len(s)):
            new_arr.append(int(s[i]))
        arr.append(new_arr)
    s=Solution()
    output = s.maximumWealth(arr)
    string =""
    print(output)
main()
    '''