i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ') #this will loop until i2 reaches its capacity then it will restart with i1 equalling 11
        i2 = i2 + 3
    i1 = i1 + 10
