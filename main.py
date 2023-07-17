def is_palindrome_number(s):
    str=""
    for i in s:
        str=i+str
    if str==s:
            return True
    else:
            return False
s="123"
print(is_palindrome_number(s))  