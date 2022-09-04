from time import strftime
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("DIGITAL CLOCK")
root.resizable(0, 0)  # sets the window to NO resizeble mode
root['bg'] = "lightblue"

Label(root, text="Digital CLOCK", font=('Calibri', 12, 'bold'), bg='lightblue').pack(side=BOTTOM)


def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text=string)  # first change text='start' to local time, and keeps updating every call
    mark.after(1000, time)  # after 1000 milliseconds calls function time() again


mark = Label(root, text='start',
             font=('ARIAL', 25, 'bold'),
             pady=150,
             bg='lightblue')

mark.pack(anchor="center")

time()

mainloop()
