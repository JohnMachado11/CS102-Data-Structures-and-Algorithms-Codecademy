
def wrap_string(str, n):
    result = ""
    if n <= 0:
        return str
    result += "<"
    result += wrap_string(str, n-1)
    result += ">"
    
    return result

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
wrapped = wrap_string("Gemstone", 8)
print(wrapped)