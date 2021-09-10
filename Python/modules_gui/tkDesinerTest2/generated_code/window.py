from tkinter import *


import tkinter.font as font
def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1152x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    0, 0, 0+584, 0+700,
    fill = "#fcaf3b",
    outline = "")

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    878.5, 533.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

entry0.place(
    x = 751.957218170166, y = 507,
    width = 253.08556365966797,
    height = 50)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    878.5, 445.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

entry1.place(
    x = 751.957218170166, y = 419,
    width = 253.08556365966797,
    height = 51)

canvas.create_text(
    292.5, 191.5,
    text = "Welcome to Tkinter Designer",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    782.5, 93.0,
    text = "Enter the Details",
    fill = "#f17154",
    font = ("None", int(36.0)))

canvas.create_text(
    110.0, 651.5,
    text = "How to use it ",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    292.5, 346.0,
    text = "feugiat mi, in morbi. Auctor aliquet lorem Nisl, enim euismod morbi ac. Lorem faucibus tellus. aliquam eget dictum sed scelerisque lorem sed scelerisque. Malesuada urna, eget dignissim aenean. Felis felis",
    fill = "#000000",
    font = ("None", int(26.0)))

button_img_0 = PhotoImage(file = f"button_img_0.png")
button_text_font_0 = font.Font(family='Rubik-Medium', size=int(21.56149673461914))
b0 = Button(
    image = button_img_0,
    text = 'Sign In',
    compound = 'center',
    fg = '#ffffff',
    font = button_text_font_0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b0.place(
    x = 726, y = 605,
    width = 303,
    height = 53)

window.resizable(False, False)
window.mainloop()
