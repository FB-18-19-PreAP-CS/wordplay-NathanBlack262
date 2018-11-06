count = 0
for i in range(18,111):
    momString = str(i)
    if (i-18) < 10:
        kidString = "0" + str(i-18)
    else:
        kidString = str(i-18)
    if momString[::1] == kidString[::-1]:
        count += 1
        if count == 6:
            print(kidString)
    