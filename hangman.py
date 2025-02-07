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

        guess:  str = input('Enter a letter: ')

        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'sorry, that was wrong... ({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining... You lose')
                break



    if __name__ == ' __main__':
        run_game()
