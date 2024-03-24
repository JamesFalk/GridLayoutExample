from datetime import datetime
from tkinter import Tk, Frame, Canvas, Label, BooleanVar, Checkbutton
from tkinter import Entry, StringVar, ttk, Button
from PIL import Image, ImageTk
from pygame import mixer
from gtts import gTTS
import time

# Initializing the Sound Mixer
mixer.init()

# Creating the Main Window
master = Tk(); master.title("Grid Layout Example")
master.geometry("800x500+200+200")

# Create the master_grid with 10 rows and 10 columns
mstr_grid = Frame(master, width=800, height=500)
mstr_grid.grid()
for i in range(10):  # Create 10 rows
    mstr_grid.grid_rowconfigure(i, weight=1, minsize=50)
for i in range(10):  # Create 10 columns
    mstr_grid.grid_columnconfigure(i, weight=1, minsize=80)
mstr_grid.grid_propagate(False)

### Example Widgets: ###
# 1. Static Label
lbl_1 = Label(mstr_grid, text="Here is a clock label:")
lbl_1.grid(row=0, column=0, columnspan=2, sticky='nw')

# 2. Clock_Label
def clock_time():
    new_date = datetime.now().strftime("%m-%d-%Y")
    new_time = datetime.now().strftime("%H:%M:%S %p")
    date_time = (f'Date is ' + new_date + '\nTime is ' + new_time)
    lbl_Clock_Label.config(text=date_time)
    lbl_Clock_Label.after(1000, clock_time)
lbl_Clock_Label = Label(mstr_grid, font=('calibri', 12, 'bold'))
lbl_Clock_Label.grid(row=1, column=1, columnspan=2, sticky='nw'); clock_time()

# 3. Checkbox
checkvar = BooleanVar()
checkbox = Checkbutton(mstr_grid, text="Check This Out!", variable=checkvar)
checkbox.grid(row=2, column=2, columnspan=2, sticky='nw')

# 4. Image on Canvas inside a box_grid on mstr_grid
# Create a box_grid frame on mstr_grid
box_grid = Frame(mstr_grid, width=300, height=300)
box_grid.grid_propagate(False)
box_grid.grid(row=3, column=3, rowspan=4, columnspan=4, sticky='nw')
# Create the Canvas
canvas = Canvas(box_grid); canvas.grid()
image = Image.open("GitHubProfile.jpg")
image = image.resize((250, 200), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=img)

# 5. Entrybox
entered_text = StringVar()
entrybox = Entry(mstr_grid, textvariable=entered_text)
entrybox.grid(row=7, column=7, columnspan=3, sticky='nw')

# 6. Combobox
optn_select = StringVar()
size_ddbox = ttk.Combobox(mstr_grid, width=15, textvariable=optn_select)
size_ddbox['values'] = ('Small', 'Medium', 'Large', 'Extra Large')
size_ddbox.grid(row=8, column=8, sticky='nw'); size_ddbox.current(1)

# 7. Button
btn_button = Button(mstr_grid, text="Press Button", bg="green", fg="orange")
btn_button.grid(row=9, column=9, sticky='news')
# Making A Button Function that Plays Sound if Checkbox is Checked
def btn_button_click(yo):
    global entered_text
    entrytext = entered_text.get()
    if checkvar.get():
        tts = gTTS(entrytext); tts.save('g_speech.mp3'); mixer.music.load('g_speech.mp3')
    else:    mixer.music.load('YoYoYoBuddy.wav')
    mixer.music.play()

# Triggering The Button Event
btn_button.bind("<Button-1>", btn_button_click)
# note - there is a big array of button bindings to choose from such as
# <Enter> Hover In, <Leave> Hover Out <Button-3> Right Mouse

# 8. Making a display_label that Displays text entered in the Entrybox
dsply_lbl = Label(mstr_grid, textvariable=entered_text, font=('Courier', 12, 'italic'))
dsply_lbl.grid(row=8, column=1, columnspan=5, sticky='nw')
def update_size(hi):
    size_mtrx = [8, 12, 18, 26]; size = size_mtrx[size_ddbox.current()]
    dsply_lbl.config(font=('Courier', size, 'italic'))
size_ddbox.bind('<<ComboboxSelected>>', update_size)

master.mainloop()
