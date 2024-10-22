#printing all permutations of a string

def permute(string,n=0):
    if n==len(string):
        print("".join(string))
    for j in range(n,len(string)):
        words=[c for c in string]
       # print(words)
        #print(n,j)
        words[n],words[j]=words[j],words[n]

        permute(words,n+1)
permute("run")

#printing all the subsequences of a string

def Subsequence(arr, idx=0, seq=[]):
    if idx==len(arr):
        if seq:
            print(seq)
        return
    Subsequence(arr, idx+1, seq)
    Subsequence(arr,idx+1,seq+[arr[idx]])
x=[1,2,3]
Subsequence(x)


#merge sort of an array

class Solution(object):
    def sortArray(self, nums):
        freq = {}
        start = end = nums[0]

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            if num < start:
                start = num
            if num > end:
                end = num + 1
        
        nums = [x for x in range(start, end+1) if x in freq for repeat in range(freq[x])]
        return nums

nums=[1,2,2,0,0,5,3]
print(Solution().sortArray(nums))