"""
Hangman.

Authors: Ben Hawkins and John Neil.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def starthang():
    print("Welcome to hang")
    input1 = int(input("Please pick a minimum word length (integer)"))
    """if input1 is type(str):
        print("Please pick an integer")
        starthang()
    elif input1 is type(float):
        print("Please pick an integer")
        starthang()
    number = int(input1) """
    while True:
        item = wordselect()
        if len(item) >= input1:
            break
    print("A word has been selected")
    print("The word is", len(item), "letters long")
    #print(item)
    return item


def wordselect():
    with open('words.txt') as f:
        string = f.read()
        words = string.split()
        item = words[random.randrange(2, len(words))]
    return item


def startboard(string):
    boris = []
    for k in range(len(string)):
        boris.append("_")
    print(boris)
    return boris


def playhang(board, string):
    #print(string)
    #print(board)
    tries = 0
    used = []
    state = 0
    while True:
        print('You have ', 5 - tries, 'left')
        #previousstate = board
        input1 = getuserinput()
        previousstate = state
        state = boardstate(board, string, input1, state)
        #print(previousstate == board)
        if state == previousstate:
            tries = tries + 1
            used.append(input1)
            print('You have used the following letters: ', used)
            if tries >= 5:
                break
        if wincond(state, string) is True:
            print("Conglaturations, You weren't hung")
            return
    print("The Hang has been hung")
    print("The Word was: ", string)


def boardstate(board, string, input1, state):
    totalwrong = 0
    totalright = state
    for k in range(len(string)):
        if input1 == string[k]:
            board[k] = " " + input1 + " "
            totalright += 1
        else:
            totalwrong = totalwrong + 1
    print(board)
    return totalright


def getuserinput():
    input1 = input('Guess a letter: ')
    if len(input1) > 1:
        print("Pick one letter")
        input1 = getuserinput()
    return input1


def wincond(totalright, string):
    if totalright == len(string):
        return True
    return False

def playagain():
    inputt = input('Do you want to play again? uwu (y/n)')
    if inputt == 'y':
        main()
    elif inputt == 'n':
        print('Thank you for playing!')
    else:
        print('learn to read')
        playagain()

def main():
    string = starthang()
    board = startboard(string)
    playhang(board, string)
    playagain()

main()
