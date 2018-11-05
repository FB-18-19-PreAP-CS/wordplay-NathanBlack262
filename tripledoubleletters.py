

with open("words.txt") as file:
    pair1 = False
    pair2 = False
    pair3 = False
    for line in file:
        for word in line.strip().split():
            stop = False
            pair1 = False
            pair2 = False
            pair3 = False
            if len(word) < 6:
                stop = True
            if len(word) > 6:
                if word[0] != "b" and word[1] != "o" and word[2] != "o":
                    stop = True
            if stop == False:
                for i in range(1, len(word), 2):
                    if word[i] == word[i-1]:
                        if pair1 == False and pair2 == False and pair3 == False:
                            pair1 = True
                        elif pair1 == True and pair2 == False and pair3 == False:
                            pair2 = True
                        elif pair1 == True and pair2 == True and pair3 == False:
                            pair3 = True
                        if pair1 == True and pair2 == True and pair3 == True:
                            print(word)
                    else:
                        pair1 = False
                        pair2 = False
                        pair3 = False
                        
                
                
    