from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])


    username: str = input('What is your name? =>')
    print(f'welcome to hangman, {username}!')


    # Set up
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else: 
                print('_', end='')
                blanks+=1
        print() # Adds a blank line

        if blanks == 0:
            print('you got it!')
            break
