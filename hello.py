number = [1,2,3,4]

def numbers(number):
    total = 0
    for x in number:
        total = total + x
    return total

print(numbers(number))