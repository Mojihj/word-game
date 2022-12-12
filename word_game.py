import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
s_word="ant camel cat cobra parrot pigeon rabbit salmon shark sheep".split()
#function for choose a random word
#Function for check if the input character by user is correct
def check_guess_char(char):
    while True:
        print("Enter your guess:")
        guess_char=input().lower()
        if len(guess_char) !=1:
            print("Enter only one character")
        elif guess_char not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter only abc character")
        elif guess_char in char:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess_char
c_word=""
m_word=""
secret_word=random.choice(s_word)
gameIsDone = False
blanks = '_' * len(secret_word)
print("This is word guessin game".center(50,'-'))
while True:
    print(HANGMAN_PICS[len(m_word)])
    guess1=check_guess_char(c_word+m_word)
    if guess1 in secret_word:
        c_word=c_word+guess1
        for i in range(len(secret_word)):
            if secret_word[i] in guess1:
                blanks=blanks[:i]+secret_word[i]+blanks[i+1:]
                print("The secret word is:\n",blanks)
                if "_" not in blanks:
                    print('Yes! The secret word is "' + secret_word + '"! You have won!')
                    gameIsDone=True          
    else:
        m_word=m_word+guess1
        if len(m_word)==len(HANGMAN_PICS):
            print('You have run out of guesses')
            print("Do you want to play again?")
            x=input("Enter yes or no!!\n")
            if x=="yes":
                m_word=""
                gameIsDone = False
                print("This is word guessin game".center(50,'-'))
                secret_word=random.choice(s_word)
            else:
                 break
