# calculate the sum of number 1 to 100
a = 1
sum = 0
print ("Hello, welcome to my program!")
upto = int (input("Please input a number."))

# using infinity loop and break statement
while True:
    if a % 2 == 0:
        sum += a
    a += 1
    if a > upto:
        break
print("Sum = {0}".format(sum))
