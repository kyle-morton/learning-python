hello = 'this is my message'
print(hello)

def add_numbers(val1: int, val2: int):
    return val1 + val2

print(add_numbers(5, 10))

def add_more_numbers(val3: int):
    return add_numbers(20, 100) + val3

print('add_more_numbers: ' + add_more_numbers(25).__str__())
