#finding max number in array
def solve(arr):
    j=arr[0]
    for i in arr:
        if j<=i:
            j=i
    return j
arr=[151,48,3,9,-7]
print(solve(arr))   
# Write a program to store first n prime numbers in an array . After storing return the array.﻿  

def first_prime(n):
    arr=[]
    num=2

    while len(arr) < n:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            arr.append(num)
        num+=1
    return arr
n=int(input("="))
print(first_prime(n))