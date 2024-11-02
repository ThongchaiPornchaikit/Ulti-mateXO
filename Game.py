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
                  font=("Helvetica",60),
                  fg="White",
                  bg="black").pack(pady=80)

homepage.pack(fill=BOTH, expand=True)

"""จบส่วนhomepage"""

"""chose_frame"""

chose_frame = Frame(main_frame,bg="black")

#ข้อความ
heading = Label(chose_frame, text="Choose Your Mode", fg="white", font=("Helvetica", 35), bg="black")
heading.pack(pady=50)

#รูปแบบปุ่ม
ButtonType = Frame(chose_frame, bg="black")
ButtonType.pack(pady=60)

"""จบส่วนของchose_frame"""

"""gamemode general"""

game1 = Frame(main_frame,bg="black")


# Button Click function

def b_click(b):
    pass

#สร้างตาราง 3x3

b1 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b1))
b2 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b2))
b3 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b3))

b4 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b4))
b5 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b5))
b6 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b6))

b7 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b7))
b8 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b8))
b9 = Button(game1, text=" ", font=("Helvetica",20),height=4,width=8,bg="black",fg="white", command= lambda: b_click(b9))

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

"""ส่วนการไปmodegameหริอไปหน้าอื่นๆ"""

#game1
page_all = [homepage, chose_frame, game1] #ต้องมาเพิ่มตลอดถ้าเพิ่มหน้า

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
             font=("Helvetica",24),
             width=20,
             height=2,
             fg="White",
             bg="black",
             command=next_page).pack(pady=150)

#ปุ่มเลือกโหมดของchoseframe
general = Button(ButtonType, text="General Mode", fg="white", bg="black", font=("Helvetica", 25),command=move_game1)
general.pack(side=TOP, pady=20)

advance = Button(ButtonType, text="Advance Mode", fg="white", bg="black", font=("Helvetica", 25))
advance.pack(side=TOP, pady=30)

back = Button(ButtonType, text="Back", fg="white", bg="black", font=("Helvetica", 25), command=back_page , width=8)
back.pack(side=TOP, pady=40)

#ปุ่มกลับไปหน้าเลือกโหมดของgamemodegeneral
back_bt_game1 = Button(game1, text="Back", fg="white", bg="black", font=("Helvetica", 20), command=move_page_chose)
back_bt_game1.grid(row=3, column=1, pady=10)

back_bt_game2 = Button(game1, text="Back", fg="white", bg="black", font=("Helvetica", 20), command=move_page_chose)
back_bt_game2.grid(row=4, column=1, pady= 10)


"""จบส่วนปุ่ม"""

mainloop()