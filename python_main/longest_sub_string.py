def longest_sub_str(s):
    temp_str=""
    max_len=0

    for i in list(s):
        present_str="".join(i)
        if present_str in temp_str:
            temp_str=temp_str[temp_str.index(present_str)+1:]
        else:
            temp_str=temp_str+"".join(i)
        max_len=max(len(temp_str),max_len)
    print("length of longest substring=",max_len)

s=input("enter=")
longest_sub_str(s)