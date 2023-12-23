from collections import deque

input_string = "Civic"

def varify_palindrome(input_string):
    formatted_input_string = ''.join(input_string.lower().split())
    
    d = deque(formatted_input_string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return "The string is not palindrome"
        
    return "The string is palindrome"


# def varify_palindrome(input_string):
#     formatted_input_string = ''.join(input_string.lower().split())
#     d = deque()
#     first = formatted_input_string[:len(formatted_input_string)//2]
#     second = formatted_input_string[len(formatted_input_string)//2:]
    
#     d.extend(first.lower())
#     d.extend(second.lower())
    
#     if "".join(d) == "".join(reversed(formatted_input_string)):
#         return "The string is palindrome"
#     else:
#         return "The string is not palindrome"

print(varify_palindrome(input_string))


