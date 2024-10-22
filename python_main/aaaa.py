def String_check(word):
    x=word.count("z")
    y=word.count("o")
    if 2*x == y:
        return "Yes"
    else:
        return "No"
word = input()
print(String_check(word))









        
    