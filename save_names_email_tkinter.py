from tkinter import *

root = Tk()

# Defining the structure and name of the window
root.geometry("450x400")
root.title("Save Names and E-mails")
root.maxsize(width="450", height="400")
root.minsize(width="450", height="400")

# Change background color
root['bg'] = "lightblue"



def show():
    content = "Name: " + entry_name.get() + "\n" + "E-mail:" + entry_email.get() + "\n"
    output.insert(1.0, content)

def delete_output_text():
    output.delete(0.0, END)

def save_to_file():
    delete_output_text()
    with open("names_and_emails.txt", "a") as file:
        file.write(entry_name.get() + "\n")
        file.write(entry_email.get() + "\n")
        show()

# Creating a label(text in the window)
label_name = Label(text="Name")
label_name.grid(row=0, column=0, pady="5", padx="4")

label_email = Label(text="E-mail")
label_email.grid(row=1, column=0, pady="5", padx="4")

# Creating entry text boxes
entry_name = Entry(root)
entry_email = Entry(root)

entry_name.grid(row=0, column=1, pady=5 )
entry_email.grid(row=1, column=1, pady=5)

# Creating a BUTTON
button2 = Button(root, text='Delete', command=delete_output_text)
button2.grid(row=0, column=3, pady=5)

button3 = Button(root, text="Quit", command=quit)
button3.grid(row=0, column=4, pady=5)

button4 = Button(root, text="Save", command=save_to_file)
button4.grid(row=0, column=2, pady=5)

# Create a textbox
output = Text(width=40, height=10)
output.grid(row=2, column=0, columnspan=6, pady=5, padx=10)

# Start the program and show the window
root.mainloop()
