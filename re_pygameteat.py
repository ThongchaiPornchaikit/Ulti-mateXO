import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x300+100+100")
root.configure(bg="#333333")
root.resizable(True, True)

player = "X"
sizes = {"small": 1, "medium": 2, "big": 3}
board = [[None for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}
selected_size = None

colors = {
    "X": "#ff6666",
    "O": "#66b3ff",
    "bg": "#222222",
    "b": "#444444",
    "highlight": "#ffaa00",
    "text": "#ffffff"
}

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
    # Check if both players are out of moves
    if all(pieces["X"][size] == 0 for size in sizes) and all(pieces["O"][size] == 0 for size in sizes):
        messagebox.showinfo("Game Over", "It's a tie!")
        show_replay_button()

def on_click(row, col):
    global player, selected_size
    if selected_size and (board[row][col] is None or (sizes[selected_size] > sizes[board[row][col][1]] and board[row][col][0] != player)) and not check_winner():
        if pieces[player][selected_size] > 0:
            board[row][col] = (player, selected_size)
            buttons[row][col].config(text=f"{player} ({selected_size})", fg=colors[player])
            pieces[player][selected_size] -= 1
            selected_size = None
            update_pieces_label()
            winner = check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                show_replay_button()
            elif all(all(cell is not None for cell in row) for row in board):
                messagebox.showinfo("Game Over", "It's a tie!")
                show_replay_button()
            else:
                player = "O" if player == "X" else "X"
                update_turn_label()
                check_tie()  # Check if both players are out of moves
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
            buttons[row][col].config(text="", bg=colors["b"])
    update_pieces_label()
    replay_button.grid_forget()

def show_replay_button():
    replay_button.grid(row=4, column=1)

def update_turn_label():
    turn_label.config(text=f"Player: {player}")

def update_pieces_label():
    pieces_label.config(text=(
        f"X - เล็ก: {pieces['X']['small']}, กลาง: {pieces['X']['medium']}, ใหญ่: {pieces['X']['big']} | "
        f"O - เล็ก: {pieces['O']['small']}, กลาง: {pieces['O']['medium']}, ใหญ่: {pieces['O']['big']}"
    ))

game_frame = tk.Frame(root, bg="#333333")
for row in range(3):
    for col in range(3):
        button = tk.Button(game_frame, text="", width=10, height=3, bg=colors["b"], fg=colors["text"], command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

size_buttons = {}
for size in sizes:
    size_buttons[size] = tk.Button(game_frame, text=size.capitalize(), bg=colors["b"], fg=colors["text"], command=lambda s=size: select_size(s))
    size_buttons[size].grid(row=3, column=sizes[size] - 1)

replay_button = tk.Button(game_frame, text="Replay", command=reset_game, bg=colors["highlight"], fg=colors["text"])
turn_label = tk.Label(game_frame, text=f"Player: {player}", bg="#333333", fg=colors["text"])
turn_label.grid(row=1, column=4)

pieces_label = tk.Label(game_frame, text=f"X Pieces: {pieces['X']}, O Pieces: {pieces['O']}", bg="#333333", fg=colors["text"])
pieces_label.grid(row=2, column=4)

game_frame.grid(row=0, column=0, padx=55, pady=50)
update_pieces_label()

root.mainloop()
