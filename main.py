from tkinter import *
from tkinter import PhotoImage

mainui= Tk()
mainui.title("GamesXO")

#กำหนดขนาดหน้าจอและสี
mainui.geometry("900x700+300+50")
mainui.configure(background='black')

#Function
def windowmode():
    windowmode = Tk()
    windowmode.title("Chose Mode Game")
    windowmode.geometry("900x700+300+50")
    mainui.destroy()

#image
image_bgmain = PhotoImage(file=r"C:\Users\mcmcm\OneDrive\เดสก์ท็อป\Project PSCP\Ulti-mateXO\background.png.png")
imgaebg = Label(mainui,image=image_bgmain).place(relheight=1,relwidth=1)

#title Game
titlegame = Label(mainui,text="Ulti-mateXO",
                  font=("Helvetica",60),
                  fg="White",
                  bg="black").pack(pady=80)

#buttonplayinmain
bpm = Button(mainui,
             text="Play",
             font=("Helvetica",24),
             width=20,
             height=2,
             command=windowmode,
             fg="White",
             bg="black").pack(pady=150)

mainui.mainloop()
