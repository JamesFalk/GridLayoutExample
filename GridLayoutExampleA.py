from tkinter import Tk, Frame, Canvas, Label

# Creating the Main Window
master = Tk(); master.title("Grid Layout Example")
master.geometry("800x500+200+200")

# Create the master_grid
mstr_grid = Frame(master, width=800, height=500)
mstr_grid.grid()

for i in range(10):  # Create 10 rows
    mstr_grid.grid_rowconfigure(i, weight=1)
for i in range(10):  # Create 10 columns
    mstr_grid.grid_columnconfigure(i, weight=1)

mstr_grid.grid_propagate(False)
master.grid_columnconfigure(0, minsize=80)
master.grid_rowconfigure(0, minsize=50)

# Create a container box_grid
box_grid = Frame(mstr_grid, width=300, height=200)
box_grid.grid_propagate(False)
box_grid.grid(row=3, column=3, columnspan=3, rowspan=3, sticky='nw')
# Create the Canvas
canvas = Canvas(box_grid, bg="blue"); canvas.grid()

# Example Labels
lbl_1 = Label(mstr_grid, text="label 1")
lbl_1.grid(row=0, column=0, sticky='nw')

lbl_2 = Label(mstr_grid, text="label 2")
lbl_2.grid(row=1, column=1, sticky='nw')

lbl_3 = Label(mstr_grid, text="label 3")
lbl_3.grid(row=2, column=2, sticky='nw')

lbl_4 = Label(mstr_grid, text="label 4")
lbl_4.grid(row=3, column=3, sticky='nw')

lbl_5 = Label(mstr_grid, text="label 5")
lbl_5.grid(row=4, column=4, sticky='nw')

lbl_6 = Label(mstr_grid, text="label 6")
lbl_6.grid(row=5, column=5, sticky='nw')

lbl_7 = Label(mstr_grid, text="label 7")
lbl_7.grid(row=6, column=6, sticky='nw')

lbl_8 = Label(mstr_grid, text="label 8")
lbl_8.grid(row=7, column=7, sticky='nw')

lbl_9 = Label(mstr_grid, text="label 9")
lbl_9.grid(row=8, column=8, sticky='nw')

lbl_10 = Label(mstr_grid, text="label 10")
lbl_10.grid(row=9, column=9, sticky='nw')

master.mainloop()
