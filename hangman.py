import random
import string

WORDLIST_FILENAME = "D:/Python/hangman/words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    isGuessed = True
    for char in secretWord:
        if char in lettersGuessed and isGuessed == True:
            isGuessed = True
        else:
            isGuessed = False
    return isGuessed
            



def getGuessedWord(secretWord, lettersGuessed):
    def check_guess(char, wordL, wordFinal):
        if char in wordL:
            char_index = wordL.index(char)
            wordFinal[char_index] = char
            wordL[char_index] = ['_']
            check_guess(char,wordL, wordFinal)
    wordL = []
    wordFinal = []
    printout = ''
    for char in secretWord:
        wordFinal.append('_')
    for char in secretWord:
        wordL.append(char)
    for char in lettersGuessed:
        check_guess(char, wordL, wordFinal)
    for i in wordFinal:
        printout += i
    return printout



def getAvailableLetters(lettersGuessed):
    lettersRemainingStr = 'abcdefghijklmnopqrstuvwxyz'
    lettersRemainingList = []
    lettersRemainingFinal = ''
    for letter in lettersRemainingStr:
        lettersRemainingList.append(letter)
    for char in lettersGuessed:
        if char in lettersRemainingList:
            lettersRemainingList.remove(char)
    for char in lettersRemainingList:
        lettersRemainingFinal += char
    return lettersRemainingFinal
    

def hangman(secretWord):
    wordLength = str(len(secretWord))
    guessesLeft = 8
    lettersGuessed = []
    line = '-------------'
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of word that is ' + wordLength + ' letters long.'
    print line
    while guessesLeft > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print 'You have ' + str(guessesLeft) + ' guesses left.'
        print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
        userInput = raw_input('Please guess a letter: ')
        userInputLower = userInput.lower()
        if userInputLower in secretWord and userInputLower not in lettersGuessed:
            lettersGuessed.append(userInputLower)
            print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            print line
        elif userInputLower in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print line
        elif userInputLower not in secretWord:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            if userInputLower not in lettersGuessed:
                lettersGuessed.append(userInputLower)
                guessesLeft -= 1
            print line
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, You won!'
    else:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "." 
        
