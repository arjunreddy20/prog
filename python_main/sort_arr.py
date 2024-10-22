class Solution():
    def bubble_sort(self,a):
        x=len(a)
        for i in range (0,x):
            for j in range (0,x-i-1):
                if a[j]<a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a
ans=Solution()
a=list(map(int, input("=").split()))
print(ans.bubble_sort(a))
print("------------------------------------------------------------------")
# insertion_sort
class insertion():
    def insertion_sort(self,arr):
        for i in range (1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key < arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr

answer=insertion()
arr=list(map(int,input("enter with space=").split()))
print(answer.insertion_sort(arr))
