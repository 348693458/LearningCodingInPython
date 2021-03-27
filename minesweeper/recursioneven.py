num = int (input("Please input a number."))
def addup(num):
        if num == 2:
            print('addup({0}) - return: {0}'.format(num))
            return 2
        elif num == 0: 
            print('addup({0}) - return: {0}'.format(num))
            return 0
        elif (num % 2) == 1:
            print('addup({0}) - return: {0} + addup({1})'.format(num, num - 1))
            return addup (num - 1)
        else:
            print('addup({0}) - return: {0} + addup({1})'.format(num, num - 2))
            return num + addup(num - 2)
print(addup(num))
