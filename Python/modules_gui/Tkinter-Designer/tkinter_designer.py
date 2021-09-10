# Required in order to add data files to Windows executable
import os
import sys
import backend
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox

path = getattr(sys, "_MEIPASS", os.getcwd())
os.chdir(path)


def btn_clicked():
    token = token_entry.get()
    URL = URL_entry.get()
    output_path = path_entry.get()
    output_path = output_path.strip()

    if not token:
        messagebox.showerror(title="Empty Fields", message="Please enter Token")

    elif not URL:
        messagebox.showerror(title="Empty Fields", message="Please enter URL")

    elif not output_path:
        messagebox.showerror(title="invalid path", message="Enter a valid output path")

    else:
        backend.generate_code(token, URL, output_path)


def select_path():
    path_entry.delete(0, END)
    path_entry.insert(0, filedialog.askdirectory())


def know_more_clicked(event):
    url = "https://github.com/ParthJadhav/Tkinter-Designer/blob/master/instructions.md"
    webbrowser.open_new(url)


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)

    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)

    return label


window = Tk()
logo = PhotoImage(file="images/iconbitmap.gif")
window.call("wm", "iconphoto", window._w, logo)
window.title("Tkinter Designer")
output_path = ""

window.geometry("862x519")
window.configure(bg="#3A7FF6")
canvas = Canvas(
    window,
    bg="#3A7FF6",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")

text_box_bg = PhotoImage(file=f"images/TextBox_Bg.png")
token_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
URL_entry_img = canvas.create_image(650.5, 248.5, image=text_box_bg)
filePath_entry_img = canvas.create_image(650.5, 329.5, image=text_box_bg)

token_entry = Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
token_entry.bind("<Return>", lambda event: URL_entry.focus())
token_entry.place(x=490.0, y=137 + 25, width=321.0, height=35)
token_entry.focus()

URL_entry = Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
URL_entry.bind("<Return>", lambda event: path_entry.focus())
URL_entry.place(x=490.0, y=218 + 25, width=321.0, height=35)

path_entry = Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
path_entry.bind("<Return>", lambda event: btn_clicked())
path_entry.place(x=490.0, y=299 + 25, width=321.0, height=35)

canvas.create_text(
    519.0, 156.0, text="Token ID", fill="#515486", font=("Arial-BoldMT", int(13.0))
)
canvas.create_text(
    518.5, 234.5, text="File URL", fill="#515486", font=("Arial-BoldMT", int(13.0))
)
canvas.create_text(
    529.5, 315.5, text="Output Path", fill="#515486", font=("Arial-BoldMT", int(13.0))
)
canvas.create_text(
    646.5, 428.5, text="Generate", fill="#FFFFFF", font=("Arial-BoldMT", int(13.0))
)
canvas.create_text(
    573.5,
    88.0,
    text="Enter the details.",
    fill="#515486",
    font=("Arial-BoldMT", int(22.0)),
)

title = Label(
    text="Welcome to Tkinter Designer",
    bg="#3A7FF6",
    fg="white",
    font=("Arial-BoldMT", int(20.0)),
)
title.place(x=27.0, y=120.0)

info_text = Label(
    text="Tkinter Designer uses the Figma API\n"
    "to analyse a design file, then creates\n"
    "the respective code and files needed\n"
    "for your GUI.\n\n"
    "Even this GUI was created\n"
    "using Tkinter Designer.",
    bg="#3A7FF6",
    fg="white",
    justify="left",
    font=("Georgia", int(16.0)),
)

info_text.place(x=27.0, y=200.0)

know_more = Label(
    text="Click here for instructions", bg="#3A7FF6", fg="white", cursor="hand2"
)
know_more.place(x=27, y=400)
know_more.bind("<Button-1>", know_more_clicked)

generate_btn_img = PhotoImage(file="./images/generate.png")

generate_btn = Button(
    text="Generate",
    compound="center",
    fg="white",
    image=generate_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat",
)
generate_btn.place(x=557, y=401, width=180, height=55)

path_picker_img = PhotoImage(file = f"./images/path_picker.png")
path_picker_button = Button(
    image = path_picker_img,
    text = '',
    compound = 'center',
    fg = 'white',
    borderwidth = 0,
    highlightthickness = 0,
    command = select_path,
    relief = 'flat')

path_picker_button.place(
    x = 783, y = 319,
    width = 24,
    height = 22)

window.resizable(False, False)
window.mainloop()
