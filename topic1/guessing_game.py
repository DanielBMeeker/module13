"""
Program: guessing_game.py
Author: Daniel Meeker
Date: 7/16/2020

This program creates a GUI game where
a random number between 1 and 10 is
chosen and the user tries to guess the
number.
"""
import tkinter
from tkinter import messagebox
import random
from functools import partial

m = tkinter.Tk()
answer = 0


# declared and initialized here so it can be accessed
# all the places it needs to be


class NumberGuesser:
    """
    Number Guesser Class
    """

    def __init__(self, guessed_list):
        """
        Constructor for NumberGuesser class
        :param guessed_list: required - should be blank
        """
        self.guessed_list = guessed_list

    def add_guess(self, guess_made):
        """
        adds a guess to the list of guesses
        :param guess_made: required
        :return: no return
        """
        self.guessed_list.append(guess_made)

    def view_guesses(self):
        """
        Display all the numbers in the list
        used in debugging
        :return: no return - prints to the console
        """
        for x in range(len(self.guessed_list)):
            print(self.guessed_list[x])
        print("\n")

    def __str__(self):
        """
        Overrides built-in function
        :return: a string
        """
        return_list = []
        for x in range(len(self.guessed_list)):
            return_list.append(self.guessed_list[x])
        return str(return_list)

    def __repr__(self):
        """
        Overrides built-in function
        :return: a string
        """
        return_list = []
        for x in range(len(self.guessed_list)):
            return_list.append(self.guessed_list[x])
        return str(return_list)


guess = NumberGuesser([])


def start_game():
    """
    This function will lay out the grid of buttons
    as well as resetting answer to a new random number
    and resetting the NumberGuesser object so that it
    has an empty list to work with
    :return: no return
    """
    global answer  # accesses the global variable
    answer = random.randint(1, 10)
    # changes global variable to random number
    # between 1 and 10 inclusive with each call of start_game()
    label.config(text="Make A Guess")
    global guess  # accesses the global variable
    guess = NumberGuesser([])
    # changes global variable to a NumberGuesser
    # object constructed with an empty list
    tkinter.Button(m, text="1", width=5, state=tkinter.NORMAL, command=partial(make_guess, 1)).grid(row=1, column=0)
    tkinter.Button(m, text="2", width=5, state=tkinter.NORMAL, command=partial(make_guess, 2)).grid(row=1, column=1)
    tkinter.Button(m, text="3", width=5, state=tkinter.NORMAL, command=partial(make_guess, 3)).grid(row=1, column=2)
    tkinter.Button(m, text="4", width=5, state=tkinter.NORMAL, command=partial(make_guess, 4)).grid(row=2, column=0)
    tkinter.Button(m, text="5", width=5, state=tkinter.NORMAL, command=partial(make_guess, 5)).grid(row=2, column=1)
    tkinter.Button(m, text="6", width=5, state=tkinter.NORMAL, command=partial(make_guess, 6)).grid(row=2, column=2)
    tkinter.Button(m, text="7", width=5, state=tkinter.NORMAL, command=partial(make_guess, 7)).grid(row=3, column=0)
    tkinter.Button(m, text="8", width=5, state=tkinter.NORMAL, command=partial(make_guess, 8)).grid(row=3, column=1)
    tkinter.Button(m, text="9", width=5, state=tkinter.NORMAL, command=partial(make_guess, 9)).grid(row=3, column=2)
    tkinter.Button(m, text="10", width=5, state=tkinter.NORMAL, command=partial(make_guess, 10)).grid(row=4, column=1)


def make_guess(number):
    """
    Compares the number param to the global guess.
    If the number is correct then a messagebox pops up
    otherwise it changes the button to have a red background
    and disables the button guessed. It also adds the guess
    to the guessed_list from the NumberGuesser class
    :param number: required
    :return: no return
    """
    global guess
    if number == answer:
        label.config(text="Winner!")
        guess.view_guesses()
        message = str(number) + " was the correct number!"
        messagebox.showinfo('Winner!', message)
        start_game()  # resets the game
    elif number == 1:
        guess.add_guess(1)
        tkinter.Button(m, text="1", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 1)).grid(row=1, column=0)
        # There has to be a more efficient way to do this but I struggled
        # with disabling the buttons without overwriting the entire button.
    elif number == 2:
        guess.add_guess(2)
        tkinter.Button(m, text="2", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 2)).grid(row=1, column=1)
    elif number == 3:
        guess.add_guess(3)
        tkinter.Button(m, text="3", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 3)).grid(row=1, column=2)
    elif number == 4:
        guess.add_guess(4)
        tkinter.Button(m, text="4", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 4)).grid(row=2, column=0)
    elif number == 5:
        guess.add_guess(5)
        tkinter.Button(m, text="5", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 5)).grid(row=2, column=1)
    elif number == 6:
        guess.add_guess(6)
        tkinter.Button(m, text="6", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 6)).grid(row=2, column=2)
    elif number == 7:
        guess.add_guess(7)
        tkinter.Button(m, text="7", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 7)).grid(row=3, column=0)
    elif number == 8:
        guess.add_guess(8)
        tkinter.Button(m, text="8", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 8)).grid(row=3, column=1)
    elif number == 9:
        guess.add_guess(9)
        tkinter.Button(m, text="9", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 9)).grid(row=3, column=2)
    elif number == 10:
        guess.add_guess(10)
        tkinter.Button(m, text="10", width=5, background='red', state=tkinter.DISABLED,
                       command=partial(make_guess, 10)).grid(row=4, column=1)


if __name__ == '__main__':
    '''
    widgets
    '''
    m.title('Guess a Number')
    label = tkinter.Label(m, text="Press Start to Play")
    label.grid(row=0, columnspan=3)
    start_button = tkinter.Button(m, text='Start', width=25, command=start_game).grid(row=5, columnspan=3)
    exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
    exit_button.grid(row=6, columnspan=3)
    '''
    end of widgets
    '''
    m.mainloop()

