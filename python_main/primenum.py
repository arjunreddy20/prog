def is_prime(n):
    temp=False
  
    for i in range(2,n):
        if n % i == 0:
           temp=True
    if temp:
        print("not a prime")
    else:
        print("is a prime")
n=int(input("enter="))
is_prime(n)


def num_prime(num):
    if num <=1:
        print("none")
    for i in range(2,n):
        if num % i == 0:
            return False
        return True
num=int(input("enter="))
if num_prime(num):
    print("is prime")
else:
    print("not prime")