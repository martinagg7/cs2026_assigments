""" @author: Patrick
Goal: make software that encrypts and decrypts Pig Latin
See: https://en.wikipedia.org/wiki/Pig_Latin

Secret messages and languages are cool. 

Pig Latin is a language game or argot in which words in English are altered, 
usually by adding a fabricated suffix or by moving all beginning consonants 
of a word to the end, and then adding a 'ay' (or similar) as an ending suffix.
For example, Wikipedia would become Ikipediaway. 
(moving the 'W' and adding 'ay' to the end). 

"pig" = "igpay"
"latin" = "atinlay"
"friends" = "iendsfray"
"smile" = "ilesmay"
"eat" = "eatway" or "eatay"
"omelet" = "omeletway" or "omeletay"
"""

print("------ Learning some pig-latin --------")

# First write a test (a basic assertion, for now).  Start simple. 


# THEN implement the solution.  Repeat 


# Better way than basic assertions: python's unittest.TestCase
# Let's make them for entire phrases we can pig-latin-ize


# THEN implement the solution for making phrases














import sys
sys.exit()  #stops below from running

# password = input("Enter password")
# isCorrect = password == "42"
# assert isCorrect, "bad password!!"

def testToPig():
    print(toPig("pig"))


def translate(manyWords, langFunc):
    translation = []
    for word in manyWords.split():
        newWord = langFunc(word)
        translation.append(newWord)
    return " ".join(translation)
    

def toPig(word):
    vowels = 'aeiou'
    firstVowelSpot = 0
    for c in word:
        if c in vowels:
            break # stops the for loop early!
        else:
            firstVowelSpot += 1
    # 'break' will jump to here and continue normal execution below
    firstChars = word[0:firstVowelSpot]
    restWord = word[firstVowelSpot:]
    return restWord + firstChars + "ay"
    

# assert toPig("pig") == "igpay", "pig didn't translate to igpay!"
# assert toPig("latin") == "atinlay"
# result = toPig("friends")
# assert result == "iendsfray", str(result)
# assert toPig("smile") == "ilesmay"
# assert toPig("eat") == "eatay"
# assert toPig("omlet") == "omletay"

# print(toPig("friends"))
print('assertion not even run!', flush=True)


import unittest



class TestPigLatin(unittest.TestCase):
    
    def testPigLatinPig(self):
        result = toPig("pig")
        self.assertEqual(result, "igpay")

    def testPigLatinLatin(self):
        result = toPig("latin")
        self.assertEqual(result, "atinlay")

    def testPigLatinFriends(self):
        result = toPig("friends")
        self.assertEqual(result, "iendsfray")
        
    def testTranslateOneWord(self):
        result = translate("pig", toPig)
        self.assertEqual(result, "igpay")
        
    def testTranslateTwoWords(self):
        result = translate("   pig     latin", toPig)
        self.assertEqual(result, "igpay atinlay")
        
unittest.main()



import sys
sys.exit()


'''Old Archive:

def translate(words, tFunc):
    newWords = []
    for word in words.split():
        newWords.append(tFunc(word))
    return ' '.join(newWords)
    # for word in manyWords:




def toFrech(aWord):
    return "bonjour"

def toSwahili(aWord):
    return 'habari'

def toSpanish(aWord):
    return "hola"
    

print(translate("hi there", toSwahili))
print(translate("hi there", toSpanish))





import sys
print("Exiting demo early..."), sys.exit()



def toPig(phrase):
    words = phrase.split()
    result = ""
    for w in words:
        pigWord = toPigWord(w)
        result += pigWord
        result += ' '
    return result[:-1]

vowels = 'aeiou'
def toPigWord(word):
    vowels = 'aeiou'
    # print(vowels)
    
    if word.strip() == "":
        return ""
    while word[0] not in vowels:
        word = word[1:] + word[0]
    return word + 'ay'

def allBasicTests():
    assert toPig("") == "", "Return is bad for empty input?"
    assert toPig("    ") == ""
    assert toPigWord("pig") == "igpay"
    assert toPig("pig") == "igpay"
    # print(toPig())
    # print(toPig('friends')) # == 'eindsfray' # 'riendsfay'
    assert toPig('friends') == 'iendsfray'
    assert toPig('eat') == 'eatay'
    assert toPig('pig friends') == 'igpay iendsfray'
    assert toPig('eat pigs') == 'eatay igspay'
    assert toPig('eat omlet') == 'eatay omletay'
    assert toPig('pig latin friends') == 'igpay atinlay iendsfray'
    print("Basic tests done and passed!")

# def main():
#     allBasicTests()

# if __name__ == '__main__':
#     main()

# Better, more structured testing:
import unittest

class MainTester(unittest.TestCase):
    def testToPigWord(self):
        self.assertEqual(toPigWord(""), "")
        self.assertEqual(toPigWord("eat"), "eatay")
        self.assertEqual(toPigWord("pig"), "igpay")
        self.assertEqual(toPigWord("friends"), "iendsfray")
        
    def testToPig(self):
        self.assertEqual(toPig("hello world"), "ellohay orldway")
    def testToPig1(self):
        self.assertEqual(toPig("hello world"), "ellohay orldway")
        

def main():
    unittest.main()
    print("unittests done!")

if __name__ == '__main__':
    main()










def toPigLatin(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        pl = toPigLatinWord(word)
        result += pl + " "
    return result.strip()

def toPigLatinWord(word):
    vowels = "AEIOUaeiou"
    while word[0] not in vowels:
        word = word[1:] + word[0]
    word = word + "ay"
    return word



import sys
sys.exit() # To prevent next code from affecting live demo:


def toEngWord(word):
    word = word[:-2]
    vowels = "AEIOUaeiou"
    while word[-1] not in vowels:
        word = word[-1] + word[:-1]
    return word
    

import unittest

#########################################
# Tests using main and assert
class MainTester(unittest.TestCase):
    def test_toPig(self):
        assert toPigWord("pig") == "igpay", "igpay didn't work!!!"
        assert toPigWord("Latin") == "atinLay"
        assert toPigWord("eat") == "eatay"
        assert toPigWord("omlet") == "omletay"
        assert toPigWord("Omlet") == "Omletay"
        assert toPigWord("smile") == "ilesmay"
        
    def test_MoreToPig(self):
        self.assertEqual(toPig("pig latin"), "igpay atinlay")
        # help(unittest.TestCase)
        self.assertEqual(toPig("hello world"),"ellohay orldway")

    def testToEng(self):
        self.assertEqual(toEngWord("igpay"), "pig")
        # self.assertEqual(toEngWord("atinLay"), "Latin")
        # self.assertEqual(toEngWord("eatay"), "eat")
    


#########################################
# Start main
if __name__=="__main__":
    # main()
    unittest.main()

#########################################


'''