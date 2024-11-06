from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Game")
root.geometry("900x700+300+50")

main_frame = Frame(root,bg="black")
main_frame.pack(fill=BOTH, expand=True)

"""homepage"""

homepage = Frame(main_frame,bg="black")

titlelbmain = Label(homepage,text="Ulti-mateXO",
                  font=("Courier New",60,"bold"),
                  fg="White",
                  bg="black").pack(pady=80)

homepage.pack(fill=BOTH, expand=True)

"""จบส่วนhomepage"""

"""chose_frame"""

chose_frame = Frame(main_frame,bg="black")

#ข้อความ
heading = Label(chose_frame, text="Choose Your Mode", fg="white", font=("Courier New", 35,"bold"), bg="black")
heading.pack(pady=50)

#รูปแบบปุ่ม
ButtonType = Frame(chose_frame, bg="black")
ButtonType.pack(pady=60)

"""จบส่วนของchose_frame"""

"""gamemode general"""

game1 = Frame(main_frame,bg="black")


# Button Click function

player = "X"

def b_click_general(b):
    global player
    if b["text"] == " ":
        b["text"] = player
        if check_winner_general():
            messagebox.showinfo("Winner!", f"Player {player} wins!")
            reset_game_general()
        elif is_draw_general():
            messagebox.showinfo("Draw!", "It's a draw!")
            reset_game_general()
        player = "O" if player == "X" else "X"

def check_winner_general():
    # Winning combinations: rows, columns, and diagonals
    winning_combinations = [
        (b1, b2, b3),
        (b4, b5, b6),
        (b7, b8, b9),
        (b1, b4, b7),
        (b2, b5, b8),
        (b3, b6, b9),
        (b1, b5, b9),
        (b3, b5, b7)
    ]
    
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != " ":
            return True
    return False

def is_draw_general():
    # Check if all buttons are filled
    return all(button["text"] != " " for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9])

def reset_game_general():
    for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        button["text"] = " "
    global player
    player = "X"

#สร้างตาราง 3x3

b1 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b1))
b2 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b2))
b3 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b3))

b4 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b4))
b5 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b5))
b6 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b6))

b7 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b7))
b8 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b8))
b9 = Button(game1, text=" ", font=("Courier New",20,"bold"),height=4,width=8,bg="#444444",fg="white", command= lambda: b_click_general(b9))

#Grid our buttons to the screen

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

"""จบส่วนgamemode general"""

"""gamemode advand"""

player_advand = "X"  # ผู้เล่นเริ่มต้นเป็น X
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

# Colors
colors = {
    "X": "#ff6666",
    "O": "#66b3ff",
    "bg": "#222222",
    "b": "#444444",
    "highlight": "#ffaa00",
    "text": "#ffffff"
}

def check_tie():
    # ตรวจสอบว่าผู้เล่นได้ทำการเล่นครบทุกช่องแล้วหรือไม่
    if all(pieces[player_advand][size] == 0 for size in sizes):
        messagebox.showinfo("Game Over", "It's a tie!")  # แจ้งผลเสมอ
        show_replay_button()  # แสดงปุ่มรีเพลย์

def update_turn_label():
    turn_label.config(text=f"Player: {player_advand}")  # อัปเดตป้ายผู้เล่น

def on_click(row, col):
    global player_advand, selected_size  # ใช้ตัวแปร global
    # ตรวจสอบเงื่อนไขก่อนวางชิ้นส่วน
    if selected_size and (board[row][col] is None or (sizes[selected_size] > sizes[board[row][col][1]] and board[row][col][0] != player_advand)) and not check_winner():
        if pieces[player_advand][selected_size] > 0:
            board[row][col] = (player_advand, selected_size)  # วางชิ้นส่วน
            buttons[row][col].configure(text=f"{player_advand} ({selected_size})",fg=colors[player_advand])  # อัปเดตปุ่ม
            pieces[player_advand][selected_size] -= 1  # ลดจำนวนชิ้นส่วนที่เหลือ
            selected_size = None  # รีเซ็ตขนาดที่เลือก
            update_pieces_label()  # อัปเดตป้ายจำนวนชิ้นส่วน
            winner = check_winner()  # ตรวจสอบผู้ชนะ
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")  # แจ้งผู้ชนะ
                show_replay_button()  # แสดงปุ่มรีเพลย์
            elif all(all(cell is not None for cell in row) for row in board):
                messagebox.showinfo("Game Over", "It's a tie!")  # แจ้งผลเสมอ
                show_replay_button()  # แสดงปุ่มรีเพลย์
            else:
                player_advand = "O" if player_advand == "X" else "X"  # เปลี่ยนผู้เล่น
                update_turn_label()  # อัปเดตป้ายชื่อผู้เล่น
                check_tie()  # ตรวจสอบเสมอ           
        else:
            messagebox.showwarning("Invalid Move", f"No more {selected_size} pieces left for player {player_advand}!")  # แจ้งว่าชิ้นส่วนหมด
    elif not selected_size:
        messagebox.showwarning("Invalid Move", "Please select a size first!")  # แจ้งให้เลือกขนาดก่อน
    elif board[row][col] and board[row][col][0] == player_advand:
        messagebox.showwarning("Invalid Move", "You cannot place a piece on top of your own piece!")  # แจ้งไม่สามารถวางชิ้นส่วนทับชิ้นส่วนของตัวเองได้

def select_size(size):
    global selected_size  # ใช้ตัวแปร global
    selected_size = size  # ตั้งค่าขนาดที่เลือก

def reset_game():
    global player_advand, board, pieces, selected_size  # ใช้ตัวแปร global
    player_advand = "X"  # รีเซ็ตผู้เล่นเป็น X
    board = [[None for _ in range(3)] for _ in range(3)]  # รีเซ็ตบอร์ด
    pieces = {"X": {"small": 2, "medium": 2, "big": 2}, "O": {"small": 2, "medium": 2, "big": 2}}  # รีเซ็ตชิ้นส่วน
    selected_size = None  # รีเซ็ตขนาดที่เลือก
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ",bg=colors["b"])  # ล้างข้อความในปุ่ม
    update_pieces_label()  # อัปเดตป้ายจำนวนชิ้นส่วน
    replay_button.grid_forget()  # ซ่อนปุ่มรีเพลย์

def show_replay_button():
    replay_button.grid(row=4,column=0,pady=10)  # แสดงปุ่มรีเพลย์

def start_game():
    page_all = [homepage, chose_frame]
    for i in page_all:
        i.pack_forget()
    game_frame.pack(fill=BOTH, expand=True, pady=50, padx= 240)  # แสดงบอร์ดเกม+เซ็ตไว้ตรงกลาง
    update_pieces_label()


game_frame = Frame(main_frame,bg="#333333")  # สร้างเฟรมสำหรับเกม

def update_pieces_label():
    x_small = pieces['X']['small']
    x_medium = pieces['X']['medium']
    x_big = pieces['X']['big']
    o_small = pieces['O']['small']
    o_medium = pieces['O']['medium']
    o_big = pieces['O']['big']
    
    pieces_label.config(text=(
        f"X - Small : {x_small}   Medium : {x_medium}   Big : {x_big}"
    ))

    pieces_label1.config(text=(
        f"O - Small : {o_small}   Medium : {o_medium}   Big : {o_big}"
    ))

# สร้างปุ่มสำหรับบอร์ดเกม
for row in range(3):
    for col in range(3):
        button = Button(game_frame, text="", width=19, height=7,bg=colors["b"], fg=colors["text"], command=lambda r=row, c=col: on_click(r, c))  # ปุ่มสำหรับวางชิ้นส่วน
        button.grid(row=row, column=col)  # วางปุ่มในบอร์ด
        buttons[row][col] = button  # บันทึกปุ่มในลิสต์

size_buttons = {}  # สร้างลิสต์สำหรับปุ่มขนาด
for size in sizes:
    size_buttons[size] = Button(game_frame, text=size.capitalize(),width=7,bg=colors["b"],font=("Courier New",15,"bold"), fg=colors["text"], command=lambda s=size: select_size(s))  # ปุ่มเลือกขนาด
    size_buttons[size].grid(row=3, column=sizes[size]-1,pady = 15)  # วางปุ่มเลือกขนาด

replay_button = Button(game_frame, text="Replay", command=reset_game,bg=colors["highlight"], fg=colors["text"],width=7,font=("Courier New",15,"bold"))  # ปุ่มรีเพลย์

turn_label = Label(game_frame, text=f"Player: {player_advand}",bg="#333333",fg=colors["text"],font=("Courier New",12,"bold"))  # ป้ายเพื่อแสดงผู้เล่นปัจจุบัน
turn_label.place(relx=0.5,rely=0.85,anchor=CENTER)  # วางมันไว้ด้านล่างบอร์ดเกม

pieces_label = Label(game_frame, text=f"X Pieces: {pieces['X']}",bg="#333333",fg=colors["text"],font=("Courier New",12,"bold"))  # ป้ายเพื่อแสดงจำนวนชิ้นส่วนที่เหลือ
pieces_label.place(relx=0.5,rely=0.9,anchor=CENTER)  # วางป้ายไว้ด้านล่าง

pieces_label1 = Label(game_frame, text=f"O Pieces: {pieces['O']}",bg="#333333",fg=colors["text"],font=("Courier New",12,"bold"))  # ป้ายเพื่อแสดงจำนวนชิ้นส่วนที่เหลือ
pieces_label1.place(relx=0.5,rely=0.95,anchor=CENTER)  # วางป้ายไว้ด้านล่าง

"""จบส่วนgamemode advand"""

"""ส่วนการไปmodegameหริอไปหน้าอื่นๆ"""

page_all = [homepage, chose_frame, game1, game_frame] #ต้องมาเพิ่มตลอดถ้าเพิ่มหน้า

def move_game1():
    for i in page_all:
            i.pack_forget()
    game1.pack(fill=BOTH, expand=True, pady=50, padx= 240)

def move_page_chose():
    for i in page_all:
            i.pack_forget()
    chose_frame.pack(fill=BOTH, expand=True)

"""จบส่วนการไปmodegame"""

"""ส่วนการสลับหน้า"""

pages = [homepage, chose_frame]
count = 0

def next_page():
    global count
    if count < len(pages) - 1:
        for i in pages:
            i.pack_forget()
        count += 1
        pages[count].pack(fill=BOTH, expand=True)

def back_page():
    global count
    if count != 0:
        for i in pages:
            i.pack_forget()
        count -= 1
        pages[count].pack(fill=BOTH, expand=True)

"""จบส่วนของการสลับหน้า"""

"""ส่วนปุ่น"""

#ปุ่มของhomepage
bpm = Button(homepage,
             text="Play",
             font=("Courier New",24,"bold"),
             width=20,
             height=2,
             fg="White",
             bg="black",
             command=next_page).pack(pady=150)

#ปุ่มเลือกโหมดของchoseframe
general = Button(ButtonType, text="General Mode", fg="white", bg="black", font=("Courier New", 25,"bold"), command=move_game1)
general.pack(side=TOP, pady=20)

advance = Button(ButtonType, text="Advance Mode", fg="white", bg="black", font=("Courier New", 25,"bold"), command=start_game)
advance.pack(side=TOP, pady=30)

back = Button(ButtonType, text="Back", fg="white", bg="black", font=("Courier New", 25,"bold"), command=back_page , width=8)
back.pack(side=TOP, pady=40)

#ปุ่มกลับไปหน้าเลือกโหมดของgamemodegeneral

reset_game1 = Button(game1, text="Reset", fg="white", bg="#444444", font=("Courier New", 20,"bold"), command=reset_game_general)
reset_game1.grid(row=3, column=0, pady=30)

back_bt_game1 = Button(game1, text="Back", fg="white",bg="#444444", font=("Courier New", 20,"bold"), command=move_page_chose)
back_bt_game1.grid(row=3, column=2, pady=30)

#ปุ่มกลับไปหน้าเลือกโหมดของgamemodeadvand
back_bt_game2 = Button(game_frame, text="Back", fg="white",bg=colors["b"], width=7, font=("Courier New", 15,"bold"), command=move_page_chose)
back_bt_game2.grid(row=4, column=2, pady=10)


"""จบส่วนปุ่ม"""
mainloop()
