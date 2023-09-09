# Full
number, substractor = input().split(' ')
number = int(number)
substractor = int(substractor)

while substractor != 0:
    if number % 10 != 0:
        if substractor % 10 != 0:
            number -= 1
            substractor -= 1
        else:
            substractor -= 1
            number -= 1
    else:
        if substractor % 10 != 0:
            number /= 10
            substractor -= 1
        else:
            number /= 10
            substractor -= 1
print(int(number))
