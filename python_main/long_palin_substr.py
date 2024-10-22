"""ababa,cbba"""
def longest_palindrome(s):
    if len(s)<=1:
        return ""
    def check_around_centre(s,left,right):
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right+=1
        return s[left+1:right]
    max_str=""
    for i in range(len(s)-1):
        odd=check_around_centre(s,i,i)
        even=check_around_centre(s,i,i+1)
        if len(odd) > len(max_str):
            max_str=odd
        if len(even) > len(max_str):
            max_str=even
    return max_str
s="cbba"
print(longest_palindrome(s))