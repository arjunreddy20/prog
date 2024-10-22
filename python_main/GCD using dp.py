def gcf(a,b):
    while b:
        a,b=b,a%b        #finds greatest common divisor b/w 2 elements
    return a

def find_greatness(n,arr):

    dp=[[0]*(n+1) for _ in range(n)]      #creates dp table of n+1*n size
    result=[0]*n          #creates array  of size n

    for i in range(0,n):
        dp[i][1]=arr[i]                        # for first column of dp table
        result[0]=max(result[0],arr[i])
    
    for length in range(2,n+1):
        for i in range(0,n-length+1):                       # for rest of columns of dp table
            dp[i][length]=gcf(dp[i][length-1],arr[i+length-1])
            result[length-1]=max(result[length-1],dp[i][length])
    return result






def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_greatness(n, arr)

    for i in range(n):
        print(result[i], end=" ")

if __name__ == "__main__":
    main()