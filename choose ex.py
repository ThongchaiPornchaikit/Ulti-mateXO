from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Game")
root.geometry("900x700+300+50")

# กำหนดชุดสี
bg_color = "#2E2E2E"  # พื้นหลังสีเทาเข้ม
button_fg = "#FFFFFF"  # ตัวอักษรปุ่มสีขาว
button_bg = "#1A1A1A"  # พื้นหลังปุ่มสีดำ
button_hover = "#333333"  # สีปุ่มเมื่อชี้เมาส์

root.configure(bg=bg_color)

# หัวข้อ
heading = Label(root, text="Choose Your Mode", fg="white", font=("Courier New", 50), bg=bg_color)
heading.pack(pady=50)

# เฟรมสำหรับปุ่ม
ButtonType = Frame(root, bg=bg_color)
ButtonType.pack(pady=60)

# ฟังก์ชันสำหรับเอฟเฟกต์เมื่อเมาส์ผ่านปุ่ม
def on_enter(e):
    e.widget.config(bg=button_hover, font=("Courier New", 26), width=22)  # ขยายปุ่มขึ้นเล็กน้อย

def on_leave(e):
    e.widget.config(bg=button_bg, font=("Courier New", 25), width=20)  # คืนค่าปุ่มเมื่อเมาส์ออก

# ปุ่ม General Mode
general = Button(ButtonType, text="General Mode", fg=button_fg, bg=button_bg, font=("Courier New", 25),
                 activebackground=button_hover, activeforeground=button_fg)
general.pack(side=TOP, pady=20)
general.bind("<Enter>", on_enter)
general.bind("<Leave>", on_leave)

# ปุ่ม Advance Mode
advance = Button(ButtonType, text="Advance Mode", fg=button_fg, bg=button_bg, font=("Courier New", 25),
                 activebackground=button_hover, activeforeground=button_fg)
advance.pack(side=TOP, pady=20)
advance.bind("<Enter>", on_enter)
advance.bind("<Leave>", on_leave)

# ปุ่ม Back
back = Button(ButtonType, text="Back", fg=button_fg, bg=button_bg, font=("Courier New", 25),
              activebackground=button_hover, activeforeground=button_fg, width=8)
back.pack(side=TOP, pady=30)
back.bind("<Enter>", on_enter)
back.bind("<Leave>", on_leave)

mainloop()
