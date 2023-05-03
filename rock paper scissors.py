# IMPORT MODULES

import random
import tkinter as tk
from tkinter import ttk
from ctypes import windll

# LETTER VARIABLES

# player vs player
player1_letter = ""
player2_letter = ""

# computer vs computer
player_letter = ""
computer_letter = ""

# FUNCTIONS

# PLAYER VS PLAYER FUNCTIONS

# functions to get rock, paper or scissors input for each player
def player1_option(letter):
    global player1_letter
    player1_letter = letter

def player2_option(letter):
    global player2_letter
    player2_letter = letter

# function determining winner between players 
def print_winner():
    if player1_letter == "" or player2_letter == "":
        winner_display.config(text = "No result", fg="red")
    else:
        if player1_letter == "R" and player2_letter == "S":
            winner_display.config(text = "Player 1 wins", fg="green")
        elif player1_letter == "P" and player2_letter == "R":
            winner_display.config(text = "Player 1 wins", fg="green")
        elif player1_letter == "S" and player2_letter == "P":
            winner_display.config(text = "Player 1 wins", fg="green")
        elif player2_letter == "R" and player1_letter == "S":
            winner_display.config(text = "Player 2 wins", fg="green")
        elif player2_letter == "P" and player1_letter == "R":
            winner_display.config(text = "Player 2 wins", fg="green")
        elif player2_letter == "S" and player1_letter == "P":
            winner_display.config(text = "Player 2 wins", fg="green")
        else:
            winner_display.config(text = "Tie", fg="orange")

# function calling print_winner() to get winner
# resets letters for players

def close_players():
    print_winner()
    global player1_letter
    player1_letter = ""
    global player2_letter
    player2_letter = ""

# PLAYER VS PLAYER WINDOW
def open_player(player1_letter, player2_letter):

    # window set up: title, size, icon image, blur fixing, block resizing from user
    window_a = tk.Toplevel(root)    
    window_a.title("Player VS Player")
    window_a.geometry("375x250")
    window_a.resizable(False, False)
    window_a.iconbitmap("dices.ico")
    windll.shcore.SetProcessDpiAwareness(1)

    # heading text label 
    player_intro = tk.Label(window_a, text="Player VS Player").grid(row=0, column=2, pady=10)

    # heading text labels for players
    player1 = tk.Label(window_a, text="Player1").grid(row=1, column=0, sticky=tk.E, pady=5, padx=10)
    player2 = tk.Label(window_a, text="Player2").grid(row=2, column=0, sticky=tk.E, pady=5, padx=10)

    # PLAYER 1 OPTIONS
    # buttons for player 1 to select input
    
    player1_rock = ttk.Button(window_a, text="Rock", command=lambda:player1_option("R"), takefocus=False)
    player1_rock.grid(row=1, column=1, padx=5)
    
    player1_paper = ttk.Button(window_a, text="Paper", command=lambda:player1_option("P"), takefocus=False)
    player1_paper.grid(row=1, column=2, padx=5)
    
    player1_scissors = ttk.Button(window_a, text="Scissors", command=lambda:player1_option("S"), takefocus=False)
    player1_scissors.grid(row=1, column=3, padx=5)

    # PLAYER 1 OPTIONS
    # buttons for player 1 to select input
    
    player2_rock = ttk.Button(window_a, text="Rock", command=lambda:player2_option("R"), takefocus=False)
    player2_rock.grid(row=2, column=1, padx=5)
    
    player2_paper = ttk.Button(window_a, text="Paper", command=lambda:player2_option("P"), takefocus=False)
    player2_paper.grid(row=2, column=2, padx=5)
    
    player2_scissors = ttk.Button(window_a, text="Scissors", command=lambda:player2_option("S"), takefocus=False)
    player2_scissors.grid(row=2, column=3, padx=5)

    # button to determine winner from close_players() function  
    winner_button = ttk.Button(window_a, text="Winner", command=lambda:close_players(), takefocus=False)
    winner_button.grid(row=3, column=2, sticky=tk.W, padx=5, pady=15)

    # text label displaying winner from close_players() function
    global winner_display
    winner_display = tk.Label(window_a, text="", font=10)
    winner_display.grid(row=4, column=1, columnspan=3, padx=5, pady=15)

    window_a.mainloop()

# PLAYER VS COMPUTER FUNCTIONS

# function to get rock, paper or scissors input for player 
def single_player(letter):
    global player_letter
    player_letter = letter

# function determining winner between player and computer
def computer_winner():
    if player_letter == "" or computer_letter == "":
        comp_win_display.config(text = "No result", fg="black")
        computer_result.config(text = "")
    else:
        if player_letter == "R" and computer_letter == "S":
            comp_win_display.config(text = "Player wins", fg="green")
        elif player_letter == "P" and computer_letter == "R":
            comp_win_display.config(text = "Player wins", fg="green")
        elif player_letter == "S" and computer_letter == "P":
            comp_win_display.config(text = "Player wins", fg="green")
        elif computer_letter == "R" and player_letter == "S":
            comp_win_display.config(text = "Computer wins", fg="red")
        elif computer_letter == "P" and player_letter == "R":
            comp_win_display.config(text = "Computer wins", fg="red")
        elif computer_letter == "S" and player_letter == "P":
            comp_win_display.config(text = "Computer wins", fg="red")
        else:
            comp_win_display.config(text = "Tie", fg="orange")

# function randomly generating rock, paper or scissors choice for computer
# calls computer_winner() function to get winner
# resets player and computer letters

def computer_option():
    global player_letter
    global computer_letter
    value = random.randint(1,3)
    if player_letter != "":
        if value == 1:
            computer_letter = "R"
            computer_result.config(text = "Rock")
        elif value == 2:
            computer_letter = "P"
            computer_result.config(text = "Paper")
        else:
            computer_letter = "S"
            computer_result.config(text = "Scissors")
    computer_winner()
    player_letter = ""
    computer_letter = ""

# PLAYER VS COMPUTER WINDOW 
def open_computer(player1_letter):

    # window set up: title, size, icon image, blur fixing, block resizing from user
    window_b = tk.Toplevel(root)
    window_b.title("Player VS Computer")
    window_b.geometry("375x250")
    window_b.resizable(False, False)
    window_b.iconbitmap("dices.ico")
    windll.shcore.SetProcessDpiAwareness(1)

    # heading text label
    computer_intro = tk.Label(window_b, text="Player VS Player").grid(row=0, column=2, pady=10)

    # heading text labels for player and computer
    player = tk.Label(window_b, text="Player").grid(row=1, column=0, sticky=tk.E, pady=5, padx=10)
    computer = tk.Label(window_b, text="Computer").grid(row=2, column=0, sticky=tk.E, pady=5, padx=10)

    # PLAYER OPTIONS
    # buttons for player to select input
    
    player_rock = ttk.Button(window_b, text="Rock", command=lambda:single_player("R"), takefocus=False)
    player_rock.grid(row=1, column=1, padx=5)   

    player_paper = ttk.Button(window_b, text="Paper", command=lambda:single_player("P"), takefocus=False)
    player_paper.grid(row=1, column=2, padx=5)
    
    player_scissors = ttk.Button(window_b, text="Scissors", command=lambda:single_player("S"), takefocus=False)
    player_scissors.grid(row=1, column=3, padx=5)

    # text label displaying computer result from computer_option() function
    global computer_result
    computer_result = tk.Label(window_b, text="")
    computer_result.grid(row=2, column=1, padx=5, pady=10)

    # button to determine winner from computer_option() function 
    comp_win_button = ttk.Button(window_b, text="Winner", command=lambda:computer_option(), takefocus=False)
    comp_win_button.grid(row=3, column=2, sticky=tk.W, padx=5, pady=15)

    # text label displaying winner from computer_winner() function
    global comp_win_display
    comp_win_display = tk.Label(window_b, text="", font=10)
    comp_win_display.grid(row=4, column=1, columnspan=3, padx=5, pady=15)
    
    window_b.mainloop()

# ROOT WINDOW

# window set up: title, size, user cannot alter size of window 
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x175")
root.resizable(False, False)

# fixes blurs in window
windll.shcore.SetProcessDpiAwareness(1)

# icon image for window 
root.iconbitmap("dices.ico")

# intro text for player
intro = tk.Label(root, text="Rock Paper Scissors")
intro.grid(row=0, columnspan = 2, sticky=tk.N, padx=10, pady=35)
    
# button to play PLAYER VS PLAYER
button_player = ttk.Button(root, text="Player VS Player", command=lambda:open_player(player1_letter, player2_letter), takefocus=False)
button_player.grid(row=1, column=0, padx=40, pady=10)

# button to play PLAYER VS COMPUTER
button_computer = ttk.Button(root, text="Player VS Computer", command=lambda:open_computer(player1_letter), takefocus=False)
button_computer.grid(row=1, column=1, padx=20, pady=10)
