def addup(num):
    if num == 1 or 0:
        print('addup({0}) - return: {0}'.format(num))
        return 1
    else:
        print('addup({0}) - return: {0} + addup({1})'.format(num, num - 1))
        return num * addup(num - 1)

print(addup(5))