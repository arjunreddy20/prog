def reverse_num(n):
    temp=n

    rev_num=0
    while n > 0:
        i = n % 10
        rev_num=rev_num*10+i
        n = n // 10
    return rev_num
n=int(input("enter="))
result=reverse_num(n)
print(result)
if reverse_num == n:
    print("yes")
else:
    print("noo")