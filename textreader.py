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
    if 'e' in word or 'E' in word:
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
        if i.lower() in word or i.upper() in word:
            return False
    return True

def count_avoids():
    count = 0
    forbidden = str(input("Enter a string of characters you want to avoid: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if avoids(word, forbidden):
                    count += 1
        print(count)
        
def uses_only(word, usesString):
    for i in usesString:
        if i.lower() not in word or i.upper() not in word:
            return False
    return True

def words_with_only():
    count = 0
    usesString = str(input("Enter a string of characters you want the word to have: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_only(word, usesString):
                    count += 1
        print(count)
        
def uses_all(word, usesString):
    count = 0
    for i in usesString:
        if i in word:
            count += 1
            if count == len(usesString):
                return True
    return False

def how_many_uses_all(usesString):
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_all(word, usesString):
                    count += 1
        print(count)
        
        
def is_abecedarian(word):
    for i in range(1,len(word)):
        if word[i] < word[i-1]:
            return False
    return True

def count_abecdarian():
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if is_abecdarian(word):
                    count += 1
        print(count)
        
        
    
            

    
                        
                
    
    


if __name__ == "__main__":
    count_avoids()