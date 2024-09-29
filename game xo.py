import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

player = "X"
sizes = {"small": 1, "medium": 2, "big": 3}
board = [[None for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}
selected_size = None

def check_winner():
    for row in board:
        if row[0] and row[1] and row[2] and row[0][0] == row[1][0] == row[2][0]:
            return row[0][0]
    for col in range(3):
        if board[0][col] and board[1][col] and board[2][col] and board[0][col][0] == board[1][col][0] == board[2][col][0]:
            return board[0][col][0]
    if board[0][0] and board[1][1] and board[2][2] and board[0][0][0] == board[1][1][0] == board[2][2][0]:
        return board[0][0][0]
    if board[0][2] and board[1][1] and board[2][0] and board[0][2][0] == board[1][1][0] == board[2][0][0]:
        return board[0][2][0]
    return None

def check_tie():
    if all(pieces[player][size] == 0 for size in sizes):
        messagebox.showinfo("Game Over", "It's a tie!")
        show_replay_button()

def on_click(row, col):
    global player, selected_size
    if selected_size and (board[row][col] is None or (sizes[selected_size] > sizes[board[row][col][1]] and board[row][col][0] != player)) and not check_winner():
        if pieces[player][selected_size] > 0:
            board[row][col] = (player, selected_size)
            buttons[row][col].config(text=f"{player} ({selected_size})")
            pieces[player][selected_size] -= 1
            selected_size = None
            winner = check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                show_replay_button()
            elif all(all(cell is not None for cell in row) for row in board):
                messagebox.showinfo("Game Over", "It's a tie!")
                show_replay_button()
            else:
                player = "O" if player == "X" else "X"
                check_tie()
        else:
            messagebox.showwarning("Invalid Move", f"No more {selected_size} pieces left for player {player}!")
    elif not selected_size:
        messagebox.showwarning("Invalid Move", "Please select a size first!")
    elif board[row][col] and board[row][col][0] == player:
        messagebox.showwarning("Invalid Move", "You cannot place a piece on top of your own piece!")

def select_size(size):
    global selected_size
    selected_size = size

def reset_game():
    global player, board, pieces, selected_size
    player = "X"
    board = [[None for _ in range(3)] for _ in range(3)]
    pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}
    selected_size = None
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
    replay_button.grid_forget()

def show_replay_button():
    replay_button.grid(row=4, column=1)

def start_game():
    menu_frame.grid_forget()
    game_frame.grid(row=0, column=0)

menu_frame = tk.Frame(root)
menu_frame.grid(row=0, column=0)
play_button = tk.Button(menu_frame, text="Play", command=start_game)
play_button.grid(row=0, column=0)

game_frame = tk.Frame(root)

for row in range(3):
    for col in range(3):
        button = tk.Button(game_frame, text="", width=10, height=3, command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

size_buttons = {}
for size in sizes:
    size_buttons[size] = tk.Button(game_frame, text=size.capitalize(), command=lambda s=size: select_size(s))
    size_buttons[size].grid(row=3, column=sizes[size]-1)

replay_button = tk.Button(game_frame, text="Replay", command=reset_game)

root.mainloop()
