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
    292.0, 350.0, 292.0+584, 350.0+700,
    fill = "#000000",
    outline = "")

canvas.create_text(
    292.5, 191.5,
    text = "Welcome to Tkinter Designer",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    292.5, 326.0,
    text = "Nisl, enim euismod morbi ac. Lorem feugiat mi, in morbi. Auctor aliquet lorem lorem sed scelerisque. Malesuada urna, eget dignissim aenean. Felis felis aliquam eget dictum sed scelerisque faucibus tellus.",
    fill = "#000000",
    font = ("None", int(26.0)))

canvas.create_text(
    110.0, 651.5,
    text = "How to use it ",
    fill = "#000000",
    font = ("None", int(18.0)))

canvas.create_text(
    782.5, 93.0,
    text = "Enter the Details",
    fill = "#f17154",
    font = ("None", int(36.0)))


canvas.create_rectangle(
    878.0, 632.0, 878.0+302, 632.0+52,
    fill = "#000000",
    outline = "")


canvas.create_rectangle(
    878.5, 533.0, 878.5+301, 533.0+52,
    fill = "#000000",
    outline = "")


canvas.create_rectangle(
    878.5, 445.5, 878.5+301, 445.5+53,
    fill = "#000000",
    outline = "")

window.resizable(False, False)
window.mainloop()
