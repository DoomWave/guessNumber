print("Welcome to treasure island.")
print("your mission is to find the treasure")

move = input("you're at a cross road. Where do you want to go? Left or right?")


if move == 'left':
    print('You go to the left, you find a old rotten boat')
    check = input('Do you want to check it?').lower()

elif move == 'right':
    print('A skeleton appears! look out! has a sword!')
    attackRun = input('Do you want to run or attack? (run/attack)').lower()

    if attackRun == 'run':
        print('Oh no! the skeleton catches you!')
        print('Game Over')
    elif attackRun == 'attack':
        attack = print('You destroy that skeleton and find the treasure!')
        print('You win!')
