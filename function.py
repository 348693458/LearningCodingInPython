# define a sum function.
def sum(number_list):
    amount = 0
    for number in number_list:
        amount += number
    return amount

print(sum([1,3,5,7,9,11]))