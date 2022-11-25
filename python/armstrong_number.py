for x in range(400):
    num = x
    result = 0
    n=len(str(x))
    while x != 0:
        digit = x % 10
        result = result + digit ** n
        x = x//10

    if num == result:
        print(num, end=" ")

