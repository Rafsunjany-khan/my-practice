i = 0
while i <= 10:
    print(i, end=" ")
    i = i + 1
    
# reverse a given number
def reverse(num):
    rev = 0
    while num > 0:
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
    return rev
print(f"reverse of the number is: {reverse(567838)}")