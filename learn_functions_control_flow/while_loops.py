# Use 'while loops' with an int

x = 0
while x < 10:
    print(f'print x -> {x}')
    # if x not incremented, infinite loop
    x += 1

x = 0
while x < 10:
    if x <= 4:
        print(f'print x -> {x}')
        x += 1
    else:
        break