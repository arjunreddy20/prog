def check_armstrong(num):
    temp=num
    x=0
    while num>0:
        i=num%10
        x=x+i**3
        num=num//10
    if temp == x:
        print("true")
    else:
        print("false")
num=int(input("n="))
print(check_armstrong(num))




