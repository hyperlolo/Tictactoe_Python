##########A small GUI Tic Tac Toe Project by Karanjit Gill##########
## This game is meant to be played by 2 players, rather than a player and a computer.

from tkinter import *

"""Initializes the font and Board"""
NORMAL_FONT = ("Open Sans", 12)
BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


class Game:
    def __init__(self):
        self.turn = 1

    """Checks the various combos of X's and O's to see which player won or if it's a tie, checks each round"""
    def check_winner(self):
        if ((cell1['text'] == 'X' and cell2['text'] == 'X' and cell3['text'] == 'X') or
                (cell4['text'] == 'X' and cell5['text'] == 'X' and cell6['text'] == 'X') or
                (cell7['text'] == 'X' and cell8['text'] == 'X' and cell9['text'] == 'X') or
                (cell1['text'] == 'X' and cell5['text'] == 'X' and cell9['text'] == 'X') or
                (cell3['text'] == 'X' and cell5['text'] == 'X' and cell7['text'] == 'X') or
                (cell1['text'] == 'X' and cell4['text'] == 'X' and cell7['text'] == 'X') or
                (cell2['text'] == 'X' and cell5['text'] == 'X' and cell8['text'] == 'X') or
                (cell3['text'] == 'X' and cell6['text'] == 'X' and cell9['text'] == 'X')):
            result['text'] = "Player X Win"
            self.disable_button()

        elif ((cell1['text'] == 'O' and cell2['text'] == 'O' and cell3['text'] == 'O') or
              (cell4['text'] == 'O' and cell5['text'] == 'O' and cell6['text'] == 'O') or
              (cell7['text'] == 'O' and cell8['text'] == 'O' and cell9['text'] == 'O') or
              (cell1['text'] == 'O' and cell5['text'] == 'O' and cell9['text'] == 'O') or
              (cell3['text'] == 'O' and cell5['text'] == 'O' and cell7['text'] == 'O') or
              (cell1['text'] == 'O' and cell4['text'] == 'O' and cell7['text'] == 'O') or
              (cell2['text'] == 'O' and cell5['text'] == 'O' and cell8['text'] == 'O') or
              (cell3['text'] == 'O' and cell6['text'] == 'O' and cell9['text'] == 'O')):
            result['text'] = "Player O Win"
            self.disable_button()

        elif self.turn == 10:
            result['text'] = "Draw"
            self.disable_button()

    """Prompts players to go for their turn"""
    def play_turn(self, button):
        if self.turn % 2 == 0:
            result['text'] = "Player X Turn"
            button.config(text="O", state=DISABLED)
        else:
            result['text'] = "Player O Turn"
            button.config(text="X", state=DISABLED)
        self.turn += 1

        self.check_winner()

    """Disables all button after game end"""
    def disable_button(self):
        for button in button_cells:
            button.config(state=DISABLED)
        reset_btn.config(state=NORMAL)

    # Reset button after game end
    def reset(self):
        result['text'] = "Tic Tac Toe"
        self.turn = 1
        for button in button_cells:
            button.config(text="", state=NORMAL)


if __name__ == '__main__':
    """Creates the game window GUI"""
    game_manager = Game()
    window = Tk()
    window.title("Tic Tac Toe")
    window.config(padx=20, pady=20)

    """Creating the cells for X, O and widget"""
    result = Label(text="Tic Tac Toe", font=("Open Sans", 16, "bold"), pady=20)
    cell1 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell1))
    cell2 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell2))
    cell3 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell3))
    cell4 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell4))
    cell5 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell5))
    cell6 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell6))
    cell7 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell7))
    cell8 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell8))
    cell9 = Button(text="", width=12, height=5, command=lambda: game_manager.play_turn(cell9))
    button_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
    reset_btn = Button(text="Reset", width=12, command=game_manager.reset, state=DISABLED)

    """Game grid"""
    result.grid(row=1, column=1, columnspan=3)
    cell1.grid(row=2, column=1)
    cell2.grid(row=2, column=2)
    cell3.grid(row=2, column=3)
    cell4.grid(row=3, column=1)
    cell5.grid(row=3, column=2)
    cell6.grid(row=3, column=3)
    cell7.grid(row=4, column=1)
    cell8.grid(row=4, column=2)
    cell9.grid(row=4, column=3)
    reset_btn.grid(row=5, column=1, columnspan=3, pady=10)

    window.mainloop()
