from tkinter import *

root = Tk()
root.geometry('300x300')

say_hello = lambda: print("Hello")
say_ola = lambda: print("Olá")

#adding a Menubutton

menu_button = Menubutton(root, text='MENU')
menu_options = Menu(menu_button)

menu_button.config(menu=menu_options)

menu_options.add_command(label='Quit', command=quit)
menu_options.add_command(label='Hello', command=say_hello)
menu_options.add_command(label='Olá', command=say_ola)

menu_button.config(bg='Cyan', bd=5, relief=RAISED)
menu_button.pack()


#adding menu side by side at the top of the window

menu = Menu(root)

root.config(menu=menu)
testing_salute = Menu(menu)
menu.add_cascade(label='Salute', menu=testing_salute)
testing_salute.add_command(label='Hello', command=say_hello)
testing_salute.add_command(label='Olá', command=say_ola)

menu.add_cascade(label='Quit', command=quit)

root.mainloop()
