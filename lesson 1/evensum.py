# calculate the sum of number 1 to 100
a = 1
sum = 0

# using infinity loop and break statement
while True:
    if a % 2 == 0:
        sum += a
    a += 1
    if a > 100:
        break
print("Sum = {0}".format(sum))
