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
    '''
    determines if a word possesses an e in it:
    returns True if not,
    False if so
    
    >>> has_no_e("EEEEY")
    False
    
    >>> has_no_e("Hey")
    False
    
    >>> has_no_e("abcdEefghijklmnopqrstuvwxyz")
    False
    
    >>> has_no_e("Jolly")
    True
    
    >>> has_no_e("wut")
    True
    '''
    
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
    '''
    determines if a word avoids all of the characters in a given string:
    returns True if so,
    False if not
    
    >>> avoids("EEEEY", "e")
    False
    
    >>> avoids("Hey", "h")
    False
    
    >>> avoids("abcdEefghijklmnopqrstuvwxyz", "/")
    True
    
    >>> avoids("cvbn", "aeiou")
    True
    
    >>> avoids("wut", "wutv")
    False
    '''
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
    '''
    determines if a word possesses only the characters in the given string:
    returns True if so,
    False if not
    
    >>> uses_only("EEEEY", "E")
    False
    
    >>> uses_only("Hey", "hEY")
    True
    
    >>> uses_only("abcdEefghijklmnopqrstuvwxyz", "/")
    False
    
    >>> uses_only("Jolly", "j")
    False
    
    >>> uses_only("wut", "utw")
    True
    '''
    for i in word:
        if i.lower() not in usesString and i.upper() not in usesString:
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
    '''
    determines if a word possesses all of the characters given in a string:
    returns True if so,
    False if not
    
    >>> uses_all("EEEEY", "Ey")
    True
    
    >>> uses_all("Hey", "aeiou")
    False
    
    >>> uses_all("abcdEefghijklmnopqrstuvwxyz", "AIOU")
    True
    
    >>> uses_all("Jolly", "YoJl")
    True
    
    >>> uses_all("wut", "tWu")
    True
    '''
    count = 0
    for i in usesString:
        if i.lower() in word or i.upper() in word:
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
    '''
    determines if a word progresses in alphabetical order:
    returns True if so,
    False if not
    
    >>> is_abecedarian("EEEEY")
    True
    
    >>> is_abecedarian("Hey")
    False
    
    >>> is_abecedarian("abcdEefghijklmnopqrstuvwxyz")
    True
    
    >>> is_abecedarian("Jolly")
    False
    
    >>> is_abecedarian("wut")
    False
    '''
    for i in range(1,len(word)):
        if word[i].lower() < word[i-1].lower():
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
    import doctest
    doctest.testmod()