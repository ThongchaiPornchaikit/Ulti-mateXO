from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

root= Tk()
root.title("GamesXO")

#กำหนดขนาดหน้าจอและสี
root.geometry("900x700+300+50")
root.configure(background='black')

#Function
def menu():
    root.withdraw() #ซ่อนหน้าจอหลัก
    windowmode = Toplevel(root) #สร้างหน้าจอส่วนเสริม
    windowmode.title("Menu")

    #ขนาดหน้าจอ
    windowmode.geometry("900x700+300+50")
    windowmode.configure(bg="black") #สีพื้นหลัง

    #ข้อความ
    heading = Label(windowmode, text="Choose Your Mode", fg="white", font=("Helvetica", 35), bg="black")
    heading.pack(pady=50)

    #รูปแบบปุ่ม
    ButtonType = Frame(windowmode, bg="black")
    ButtonType.pack(pady=60)

    #ปุ่มเลือกโหมด
    general = Button(ButtonType, text="General Mode", fg="white", bg="black", font=("Helvetica", 25),command=lambda: generalmode(windowmode))
    general.pack(side=LEFT, padx=50)

    advance = Button(ButtonType, text="Advance Mode", fg="white", bg="black", font=("Helvetica", 25))
    advance.pack(side=LEFT, padx=50)

def generalmode(windowmode):
    windowmode.withdraw()
    game1 = Toplevel(root)
    game1.geometry("510x455+500+200")
    game1.title("General Mode")

    #Button click function
    def b_click(b):
        pass

    #สร้างปุ่มกกดXO
    b1 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b1))
    b2 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b2))
    b3 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b3))

    b4 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b4))
    b5 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b5))
    b6 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b6))

    b7 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b7))
    b8 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b8))
    b9 = Button(game1, text="", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b9))

    #สร้างGridสำหรับหน้าจอเกม
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


#image main
image_bgmain = PhotoImage(file=r"C:\Users\mcmcm\OneDrive\เดสก์ท็อป\Project PSCP\image\background.png")
imgaebg = Label(root,image=image_bgmain).place(relheight=1,relwidth=1)

#title Game main
titlegame = Label(root,text="Ulti-mateXO",
                  font=("Helvetica",60),
                  fg="White",
                  bg="black").pack(pady=80)

#buttonplayinmain
bpm = Button(root,
             text="Play",
             font=("Helvetica",24),
             width=20,
             height=2,
             command=menu,
             fg="White",
             bg="black").pack(pady=150)

root.mainloop()
