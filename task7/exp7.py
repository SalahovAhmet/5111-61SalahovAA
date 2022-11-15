begin = 1
for i in range(2, 101):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if (i % 3 == 0) and (i % 5 == 0):
        print("Fizz-Buzz")
