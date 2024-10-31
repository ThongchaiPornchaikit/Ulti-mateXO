from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

root= Tk()
root.title("GamesXO")

#กำหนดขนาดหน้าจอและสี
root.geometry("900x700+300+50")
root.configure(background='black')

#Function
def windowmode():
    windowmode = Tk()
    windowmode.title("Chose Mode Game")
    windowmode.geometry("510x456+500+150")
    root.destroy()
    #gametest

    #Button click function
    def b_click(b):
        pass

    #สร้างปุ่มกกดXO
    b1 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b1))
    b2 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b2))
    b3 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b3))

    b4 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b4))
    b5 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b5))
    b6 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b6))

    b7 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b7))
    b8 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b8))
    b9 = Button(windowmode, text=" ", font=("Helvetica" , 20), height=4,width=10,bg="black", command=lambda:b_click(b9))

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


#image
image_bgmain = PhotoImage(file=r"C:\Users\mcmcm\OneDrive\เดสก์ท็อป\Project PSCP\Ulti-mateXO\background.png.png")
imgaebg = Label(root,image=image_bgmain).place(relheight=1,relwidth=1)

#title Game
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
             command=windowmode,
             fg="White",
             bg="black").pack(pady=150)

root.mainloop()
