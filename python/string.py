s = input("Enter your string: ")

def palindrome(string):
    x = ""
    for i in string:
        x = i + x
    return x

print(palindrome(s))