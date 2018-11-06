for i in range(36,111):
    count = 0
    strI = str(i)
    for j in range(1,75):
        strJ = str(j)
        if strI[::-] == strJ[len(strJ)-1:-1:-1]:
            count += 1
            if count == 7:
                print(strI, strJ)