

for i in range(100000,999999):
    j = i
    eyy = str(j)
    if eyy[2:6] == eyy[5:1:-1]:
        eyyMod = str(j+1)
        if eyyMod[1:6] == eyyMod[5:0:-1]:
            eyyMod = str(j+2)
            if eyyMod[1:5] == eyyMod[4:0:-1]:
                eyyMod = str(j+3)
                if eyyMod[0:6] == eyyMod[5::-1]:
                    print(eyy[0] + "-" + eyy[1] + "-" + eyy[2] + "-" + eyy[3] + "-" + eyy[4] + "-" + eyy[5]) 