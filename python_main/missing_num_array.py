class Solution():
    def missing_num(self,arr):
        n=len(arr)
        req_num=0
        max_sum=n*(n+1)//2
        actual_sum=sum(arr)
        req_num=max_sum-actual_sum
        return req_num
find=Solution()
arr=list(map(int, input("Enter numbers separated by space: ").split()))
print(find.missing_num(arr))


        