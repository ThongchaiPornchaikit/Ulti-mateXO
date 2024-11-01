from tkinter import *

root = Tk()
root.title("Menu")

#ขนาดหน้าจอ
root.geometry("900x700+300+50")
root.configure(bg="lightblue") #สีพื้นหลัง

#ข้อความ
heading = Label(root, text="Choose Your Mode", fg="red", font=("Times New Roman", 35), bg="lightblue")
heading.pack(pady=50)

#รูปแบบปุ่ม
ButtonType = Frame(root, bg="lightblue")
ButtonType.pack(pady=60)

#ปุ่มเลือกโหมด
general = Button(ButtonType, text="General Mode", fg="white", bg="red", font=("Times New Roman", 25))
general.pack(side=LEFT, padx=50)

advance = Button(ButtonType, text="Advance Mode", fg="white", bg="red", font=("Times New Roman", 25))
advance.pack(side=LEFT, padx=50)

root.mainloop()
