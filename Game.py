import tkinter as tk  # นำเข้าโมดูล tkinter สำหรับสร้าง GUI
from tkinter import messagebox  # นำเข้า messagebox สำหรับแสดงกล่องข้อความ

root = tk.Tk()  # สร้างหน้าต่างหลัก
root.title("Tic-Tac-Toe")  # ตั้งชื่อหน้าต่าง

player = "X"  # ผู้เล่นเริ่มต้นเป็น X
sizes = {"small": 1, "medium": 2, "big": 3}  # ขนาดของชิ้นส่วน
board = [[None for _ in range(3)] for _ in range(3)]  # สร้างบอร์ด 3x3
buttons = [[None for _ in range(3)] for _ in range(3)]  # สร้างปุ่มสำหรับบอร์ด
pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}  # จำนวนชิ้นส่วนที่เหลือของแต่ละผู้เล่น
selected_size = None  # ขนาดที่เลือกของชิ้นส่วน

def check_winner():
    # ตรวจสอบว่าผู้เล่นคนใดชนะหรือไม่
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
    return None  # ไม่มีผู้ชนะ

def check_tie():
    # ตรวจสอบว่าผู้เล่นได้ทำการเล่นครบทุกช่องแล้วหรือไม่
    if all(pieces[player][size] == 0 for size in sizes):
        messagebox.showinfo("Game Over", "It's a tie!")  # แจ้งผลเสมอ
        show_replay_button()  # แสดงปุ่มรีเพลย์

def on_click(row, col):
    global player, selected_size  # ใช้ตัวแปร global
    # ตรวจสอบเงื่อนไขก่อนวางชิ้นส่วน
    if selected_size and (board[row][col] is None or (sizes[selected_size] > sizes[board[row][col][1]] and board[row][col][0] != player)) and not check_winner():
        if pieces[player][selected_size] > 0:
            board[row][col] = (player, selected_size)  # วางชิ้นส่วน
            buttons[row][col].config(text=f"{player} ({selected_size})")  # อัปเดตปุ่ม
            pieces[player][selected_size] -= 1  # ลดจำนวนชิ้นส่วนที่เหลือ
            selected_size = None  # รีเซ็ตขนาดที่เลือก
            winner = check_winner()  # ตรวจสอบผู้ชนะ
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")  # แจ้งผู้ชนะ
                show_replay_button()  # แสดงปุ่มรีเพลย์
            elif all(all(cell is not None for cell in row) for row in board):
                messagebox.showinfo("Game Over", "It's a tie!")  # แจ้งผลเสมอ
                show_replay_button()  # แสดงปุ่มรีเพลย์
            else:
                player = "O" if player == "X" else "X"  # เปลี่ยนผู้เล่น
                check_tie()  # ตรวจสอบเสมอ
        else:
            messagebox.showwarning("Invalid Move", f"No more {selected_size} pieces left for player {player}!")  # แจ้งว่าชิ้นส่วนหมด
    elif not selected_size:
        messagebox.showwarning("Invalid Move", "Please select a size first!")  # แจ้งให้เลือกขนาดก่อน
    elif board[row][col] and board[row][col][0] == player:
        messagebox.showwarning("Invalid Move", "You cannot place a piece on top of your own piece!")  # แจ้งไม่สามารถวางชิ้นส่วนทับชิ้นส่วนของตัวเองได้

def select_size(size):
    global selected_size  # ใช้ตัวแปร global
    selected_size = size  # ตั้งค่าขนาดที่เลือก

def reset_game():
    global player, board, pieces, selected_size  # ใช้ตัวแปร global
    player = "X"  # รีเซ็ตผู้เล่นเป็น X
    board = [[None for _ in range(3)] for _ in range(3)]  # รีเซ็ตบอร์ด
    pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}  # รีเซ็ตชิ้นส่วน
    selected_size = None  # รีเซ็ตขนาดที่เลือก
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")  # ล้างข้อความในปุ่ม
    replay_button.grid_forget()  # ซ่อนปุ่มรีเพลย์

def show_replay_button():
    replay_button.grid(row=4, column=1)  # แสดงปุ่มรีเพลย์

def start_game():
    menu_frame.grid_forget()  # ซ่อนเมนู
    game_frame.grid(row=0, column=0)  # แสดงบอร์ดเกม

menu_frame = tk.Frame(root)  # สร้างเฟรมสำหรับเมนู
menu_frame.grid(row=0, column=0)  # แสดงเมนู
play_button = tk.Button(menu_frame, text="Play", command=start_game)  # ปุ่มเล่น
play_button.grid(row=0, column=0)  # วางปุ่มในเฟรม

game_frame = tk.Frame(root)  # สร้างเฟรมสำหรับเกม

# สร้างปุ่มสำหรับบอร์ดเกม
for row in range(3):
    for col in range(3):
        button = tk.Button(game_frame, text="", width=10, height=3, command=lambda r=row, c=col: on_click(r, c))  # ปุ่มสำหรับวางชิ้นส่วน
        button.grid(row=row, column=col)  # วางปุ่มในบอร์ด
        buttons[row][col] = button  # บันทึกปุ่มในลิสต์

size_buttons = {}  # สร้างลิสต์สำหรับปุ่มขนาด
for size in sizes:
    size_buttons[size] = tk.Button(game_frame, text=size.capitalize(), command=lambda s=size: select_size(s))  # ปุ่มเลือกขนาด
    size_buttons[size].grid(row=3, column=sizes[size]-1)  # วางปุ่มเลือกขนาด

replay_button = tk.Button(game_frame, text="Replay", command=reset_game)  # ปุ่มรีเพลย์

root.mainloop()  # เริ่มต้นลูปหลักของ GUI