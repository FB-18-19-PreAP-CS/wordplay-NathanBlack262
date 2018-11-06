def checkword(word):
    pair1 = False
    pair2 = False
    pair3 = False
    index = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            index = i
            break
    for i in range(index, len(word), 2):
        if word[i] == word[i-1]:
            if pair1 == False and pair2 == False and pair3 == False:
                pair1 = True
            elif pair1 == True and pair2 == False and pair3 == False:
                pair2 = True
            elif pair1 == True and pair2 == True and pair3 == False:
                pair3 = True
            if pair1 == True and pair2 == True and pair3 == True:
                return True
        else:
            pair1 = False
            pair2 = False
            pair3 = False
    return False
            
with open("words.txt") as file:
    pair1 = False
    pair2 = False
    pair3 = False
    for line in file:
        for word in line.strip().split():
            if checkword(word):
                print(word)

                        
                        

                
    