def valid_palindrome(s):
    s = "".join([x for x in "".join(s.split(" ")).lower() if x.isalnum()])
    return s == s[::-1]

print(valid_palindrome("A man, a plan, a canal: Panama"))