from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])


    username: str = input('What is your name? =>')
    print(f'welcome to hangman')
