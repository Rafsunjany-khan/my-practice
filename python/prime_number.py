# printing a prime number in a range
lower = 100
upper = 200
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ") # prime