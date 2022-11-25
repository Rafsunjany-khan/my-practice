# Check For Palindrome
s = input("Enter your string: ")
# function to check the palindrome
def palindrome(string):
    for i in range(1, int(len(string) / 2)):
        if string[i] == string[len(string) - i - 1]:
            return True
    return False
print(palindrome(s))

# No 2.
# s = input("Enter a string: ")
#
# # reverse a given string
# def palindrome(string):
#     x = ""
#     for i in string:
#         x = i + x
#     return x
#
# if s == palindrome(s):
#     print("It is palindrome")
# else:
#     print("It is not a palindrome")