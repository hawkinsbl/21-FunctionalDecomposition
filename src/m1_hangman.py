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
    #print(len(item))
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
    print(string)
    print(board)
    tries = 0
    used = []
    while True:
        print('You have ', 5 - tries, 'left')
        previousstate = board
        input1 = getuserinput()
        boardstate(board, string, input1)
        print(previousstate == board)
        if previousstate == board:
            tries = tries + 1
            used.append(input1)
            print('You have used the following letters: ', used)
            if tries >= 5:
                break
    print("The Hang has been hung")


def boardstate(board, string, input1):
    for k in range(len(string)):
        if input1 == string[k]:
            board[k] = " " + input1 + " "
    print (board)
    return board


def getuserinput():
    input1 = input('Guess a letter owo')
    if len(input1) > 1:
        print("Pick one letter")
        input1 = getuserinput()
    return input1


def main():
    string = starthang()
    board = startboard(string)
    game = playhang(board, string)

main()
