def find_max_sum_subarray(arr,length):
    if length==0:
        print("error")
    first_sum=arr[0]
    max_sum=arr[0]
    i=1
    while i < length:
        if first_sum+arr[i] > arr[i]:
            first_sum=first_sum+arr[i]
        else:
            first_sum=arr[i]
        max_sum=max(first_sum,max_sum)
        i+=1
    return max_sum

arr=[1,-1,2,-3,4,-2,5,-1]
length=len(arr)
print(find_max_sum_subarray(arr,length)) 
