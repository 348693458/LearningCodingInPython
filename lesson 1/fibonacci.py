# print the fibonacci sequence up to 100
a = 0
b = 1

# using infinity loop and break statement
while True:
    c = a + b
    print(c, end = ", ")
    a = b
    b = c
    if c >= 100:
        break