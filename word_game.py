import random
s_word="ant camel cat cobra parrot pigeon rabbit salmon shark sheep".split()
#function for choose a random word
def choose_secret_word(wordlist):
    word_index=random.randint(0,len(wordlist)-1)
    return (wordlist[word_index])
#Function for check if the input character by user is correct
def check_guess_char(char):
    while True:
        print("Enter your guess:")
        guess_char=input()
        guess_char=guess_char.lower()
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
secret_word=choose_secret_word(s_word)
gameIsDone = False
blanks = '_' * len(secret_word)
print("This is word guessin game".center(50,'-'))
print("The secreet word is:",secret_word,"(for test)")
while True:
    guess1=check_guess_char(c_word+m_word)
    if guess1 in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] in guess1:
                blanks=blanks[:i]+secret_word[i]+blanks[i+1:]
                print("The secret word is:\n",blanks)
                if "_" not in blanks:
                    print('Yes! The secret word is "' + secret_word + '"! You have won!')
                    break
    else:
        m_word=m_word+guess1
        print("you have only",(len(secret_word)-len(m_word)),"chance left")
        if len(m_word)==len(secret_word):
            print('You have run out of guesses')
            print("Do you want to play again?")
            x=input("Enter yes or no!!\n")
            if x=="yes":
                m_word=""
                agameIsDone = False
            else:
                gameIsDone = True
                break