# This program contains rock paper scissors game
# Random library is imported to use for computer's choice, and user can play with the
# computer until user decides to exit the game

# import random library
import random

# initialize Rock, Paper, and Scissor variables
Rock = '1'
Paper = '2'
Scissor = '3'


# main function


def main():
    # variable another is used to determine while loop
    # this program keeps asking for user input until user selects y.
    another = 'y'
    while another == 'y' or another == 'Y':
        intro()
        # take user input and display message to user about the choice
        y = int(input('Please enter your choice:'))
        while y > 3 or y < 1:
            y = int(input('Please enter a valid choice between 1 & 3.'))
        if y == 1:
            print('Your choose Rock.')
        elif y == 2:
            print('You choose Paper.')
        elif y == 3:
            print('You choose Scissors.')

        # computer choice, random int between 1 & 3.
        x = random.randint(1, 3)
        if x == 1:
            print('Computer choose Rock.')
        elif x == 2:
            print('Computer choose Paper.')
        elif x == 3:
            print('Computer choose Scissors.')

        # check and display message who is the winner(computer or user)
        if x == 1 and y == 3:
            print('Computer Won!')
            print('Rock Smashes Scissors.')
        elif x == 3 and y == 2:
            print('Computer Won!')
            print('Scissors cuts Paper.')
        elif x == 2 and y == 1:
            print('Computer Won!')
            print('Paper wraps rock.')
        elif x == 3 and y == 1:
            print('You Won!')
            print('Rock Smashes Scissors.')
        elif x == 2 and y == 3:
            print('You Won!')
            print('Scissors cuts Paper.')
        elif x == 1 and y == 2:
            print('You Won!')
            print('Paper wraps rock.')
        elif x == y:
            print('This is a tie')

        # ask if user wants to play another round and take input from user
        print('Do you want to play again?')
        another = input('Please enter Y for another game or hit enter to quit.')

    # intro method to display  message to the user


def intro():
    print("Welcome to Rock, Paper, Scissors game.")
    print("Pleas enter 1 for Rock, 2 for Paper, and 3 for Scissors")


main()
