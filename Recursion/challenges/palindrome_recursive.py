

def is_palindrome(string):

    if not string:
        return True
    
    if string[0] == string[-1] and len(string) > 2:
        mod_string = string[1:-1]
    elif string[0] == string[-1]:
        return True
    else:
        return False

    return is_palindrome(mod_string)


print(is_palindrome("abba"))
print(is_palindrome("abcba"))
print(is_palindrome(""))
print(is_palindrome("abcd"))