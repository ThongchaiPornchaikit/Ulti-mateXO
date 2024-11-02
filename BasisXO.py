from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("XO")
root.configure(bg="Dark Blue")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="XO", font=("Arial", 30), bg="blue", fg="Orange", width=20)
titleLabel.grid(row=0, column=0)  # ใช้ grid แทน pack()

frame2 = Frame(root)
frame2.pack()

board = {1:" ", 2:" ", 3:" ", 
         4:" ", 5:" ", 6:" ", 
         7:" ", 8:" ", 9:" "}

turn = "X"
game_end = False

def checkForWin(player):
    # ตรวจสอบแนวนอน
    if (board[1] == board[2] == board[3] == player or
        board[4] == board[5] == board[6] == player or
        board[7] == board[8] == board[9] == player):
        return True
    
    # ตรวจสอบแนวตั้ง
    if (board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[3] == board[6] == board[9] == player):
        return True
    
    # ตรวจสอบแนวทแยง
    if (board[1] == board[5] == board[9] == player or
        board[3] == board[5] == board[7] == player):
        return True
    
    return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

resultLabel = None

def play(event):
    global turn, resultLabel, game_end
    if game_end:
        return
    
    button = event.widget
    row = button.grid_info()["row"]
    column = button.grid_info()["column"]
    
    clicked = row * 3 + column + 1

    if button["text"] == " ":
        if turn == "X":
            button["text"] = "X"
            board[clicked] = turn
            if checkForWin("X"):
                titleLabel.config(text="X Win The Game")  # เปลี่ยนข้อความ
                resultLabel = Label(root, text="X Win The Game", font=("Arial", 20), fg="Orange", bg="blue")
                resultLabel.pack(pady=10)
                game_end = True
            turn = "O"

        else:
            button["text"] = "O"
            board[clicked] = turn
            if checkForWin("O"):
                titleLabel.config(text="O Win The Game")  # เปลี่ยนข้อความ
                resultLabel = Label(root, text="O Win The Game", font=("Arial", 20), fg="Orange", bg="blue")
                resultLabel.pack(pady=10)
                game_end = True
            turn = "X"

        # ตรวจสอบว่าเกมเสมอ
        if checkForDraw() and not (checkForWin("X") or checkForWin("O")):
            titleLabel.config(text="Game Draw")  # เปลี่ยนข้อความ
            resultLabel = Label(root, text="Game Draw", font=("Arial", 20), fg="Orange", bg="blue")
            resultLabel.pack(pady=10)

def restartGame():
    global titleLabel, resultLabel, game_end
    game_end = False
    for button in buttons:
        button["text"] = " "
    for i in board.keys():
        board[i] = " "
    
    titleLabel.config(text="XO")  # รีเซ็ตข้อความใน titleLabel

    # ซ่อนผลลัพธ์หากมี
    if resultLabel:
        resultLabel.pack_forget()  # ลบ label เก่าออก
        resultLabel = None
    
# Row 1
button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)

# Row 2
button4 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)

# Row 3
button7 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="blue", relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", play)

restartButton = Button(frame2, text="Restart Game", font=("Arial", 15), bg="blue", fg="orange", height=2, relief=RAISED, command=restartGame)
restartButton.grid(row=4, column=0, columnspan=3, sticky="ew", padx=0, pady=10)

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

root.mainloop()
