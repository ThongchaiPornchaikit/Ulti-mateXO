from tkinter import *

root = Tk()
root.title("Game")
root.geometry("900x700+300+50")

# กำหนดชุดสี
bg_color = "#2E2E2E"  # พื้นหลังสีเทาเข้ม
button_fg = "#FFFFFF"  # ตัวอักษรปุ่มสีขาว
button_bg = "#1A1A1A"  # พื้นหลังปุ่มสีดำ
button_hover = "#333333"  # สีปุ่มเมื่อชี้เมาส์

main_frame = Frame(root, bg=bg_color)
main_frame.pack(fill=BOTH, expand=True)

homepage = Frame(main_frame, bg=bg_color)
homepage.pack(fill=BOTH, expand=True)

titlelbmain = Label(homepage, text="Ulti-mateXO",
                    font=("Courier New", 60),
                    fg=button_fg,
                    bg=bg_color)
titlelbmain.pack(pady=80)

# ฟังก์ชันสำหรับเอฟเฟกต์เมื่อเมาส์ผ่านปุ่ม
def on_enter(e):
    bpm.config(bg=button_hover, font=("Courier New", 26), width=22)  # ขยายปุ่มขึ้นเล็กน้อย

def on_leave(e):
    bpm.config(bg=button_bg, font=("Courier New", 24), width=20)  # คืนค่าปุ่มเมื่อเมาส์ออก

bpm = Button(homepage,
             text="Play",
             font=("Courier New", 24),
             width=20,
             height=2,
             fg=button_fg,
             bg=button_bg,
             activebackground=button_hover,
             activeforeground=button_fg,
             borderwidth=2,
             relief="raised")
bpm.bind("<Enter>", on_enter)
bpm.bind("<Leave>", on_leave)
bpm.pack(pady=150)

root.mainloop()
