def find_subs(arr):
    i=0
    while i < len(arr):
        j=i
        while j < len(arr):
            k=i
            while k <= j:         # for value printing
                print(arr[k],end="")
                k+=1
            print() #next line for new sub array
            j+=1
        i+=1

arr=[1,2,3,4,5]
print(find_subs(arr))



