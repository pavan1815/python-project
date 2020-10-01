from wordslist import words_list
import random



def getRandom():
    word=random.choice(words_list)
    return word.upper()


def play(word):
    word_completion='_'*len(word)
    guessed=False
    tries=6
    guessed_letters=[]
    guessed_words=[]


    print("Let's Play Hangman Game")
    print(displayHangman(tries))
    print(word_completion)
    print("\n")


    while not guessed and tries > 0:

        guess  =input('Enter your guess: ').upper()
        print(displayHangman(tries))
        print("\n")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you have already guessed the letter",guess)
            elif guess not in word:
                print(guess,"is not in word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job,",guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list =list(word_completion)
                indices =[i for i, letter in enumerate(word) if letter ==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in  word_completion:
                    guessed=True
            print(word_completion)

        elif len(guess) == len(word):
            if guess in guessed_words:
                print("you already guessed the word",guess)
            elif guess!=word:
                print(guess,"is not in word.") 
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_completion=word
            print(word_completion)

        else:
            print(guess,'not a valid guess')
            print(displayHangman(tries))
            if guessed:
              print("congrats, you guessed the correct word! you won!")
            else:
              print("sorry ,you ran out of tries.The word was ",word)
def displayHangman(tries):
    stages=[
        # 6th try
        '''
           --------
           |    |
           |    o
           |   \\|/
           |    |
           |   / \\
           -
        ''',
        # 5th try
        '''
           --------
           |    |
           |    o
           |   \\|/
           |    |
           |   /
           -
        ''',
        # 4th try
        '''
           --------
           |    |
           |    o
           |   \\|/
           |    |
           |   
           -
        ''',
        # 3rd try
        '''
           --------
           |    |
           |    o
           |   \\|
           |    |
           |   
           -
        ''',
        # 2nd try
        '''
           --------
           |    |
           |    o
           |    |
           |    |
           |   
           -
        ''',
        # 1st try
        '''
           --------
           |    |
           |    o
           |   
           |    
           |   
           -
        ''',
        # intial
        '''
           --------
           |    |
           |    
           |   
           |    
           |   
           -
        ''',

    ]
    return stages[tries]
    

def main():
    word = getRandom()
    print(word)
    play(word)

    
    while input('do you want to play again(Y/N): ').upper()=='Y':
        word= getRandom()
        play(word)


main()

