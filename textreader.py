#def read_file():
#    with open("words.txt") as file:
#        count = 0
#        for line in file:
#            for word in line.strip().split():
#                count += 1
#        print(count)


def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if len(word) >= 20:
                    print(word)
                    
def has_no_e(word):
    if 'e' in word:
        return False
    return True

def no_e():
    counter = 0
    counterNoE = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                counter += 1
                if has_no_e(word):
                    counterNoE += 1
        percentage = (((((counterNoE/counter) * 10000) // 1)  / 100))
        print("{}% of the words have no 'e'.".format(percentage))
        
def avoids(word, forbidden):
    for i in forbidden:
        if i in word:
            return False
    return True

def count_avoids():
    count = 0
    subCount = 0
    forbidden = str(input("Enter a string of characters you want to avoid: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                for i in range(len(forbidden)):
                    if forbidden[i] not in word:
                        subCount += 1
                    if subCount == len(forbidden):
                        count += 1
                subCount = 0
        print(count)
                        
                
    
    


if __name__ == "__main__":
    count_avoids()