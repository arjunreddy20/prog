class Solution():
    def finding_sum_odd_subarrays(self,arr):
        n=len(arr)
        max_sum_of_odd_subarrays=0
        for i in range(0,n):
            end=i+1
            start=n-i
            number_of_times_i_present_in_subarrays=start*end
            odds_in_them=(number_of_times_i_present_in_subarrays+1)//2
            i_s_contribution=odds_in_them*arr[i]
            max_sum_of_odd_subarrays += i_s_contribution

        return max_sum_of_odd_subarrays
    
solution=Solution()
arr=list(map(int, input("enter with spacing = ").split()))
#list(map(int, input("Enter numbers separated by space: ").split()))
print(solution.finding_sum_odd_subarrays(arr))