from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Working on Canvas using Function")
root.geometry("600x600")

color_label = Label(root, text = "Enter a Colour:")
color_label.place(relx = 0.6, rely = 0.9, anchor = CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx = 0.8, rely = 0.9, anchor = CENTER)

canvas = Canvas(root, width = 590, height = 510, bg = "white", highlightbackground = "lightgray")
canvas.pack()

img = ImageTk.PhotoImage(Image.open ("start_point1.png"))
my_image = canvas.create_image(50, 50, image = img)

direction = ""
oldx = 50
oldy= 50
newx = 50
newy = 50

def draw( direction, oldx, oldy, newx, newy):
    fill_color = input_box.get()
    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()