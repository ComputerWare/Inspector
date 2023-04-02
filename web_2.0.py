from tkinter import *
import tkinter.messagebox
import webbrowser
import requests
import os

t = Tk()
t.title('Super Inspector')
t.geometry('802x430')
scrollbar = Scrollbar(t)
scrollbar.pack(side = RIGHT, fill = Y)
menubar = Menu(t)

#Functions
def new_window():
    os.system("./inspector")

def close_window():
    t.destroy()
    
def about():
    tkinter.messagebox.showinfo("About","Super Inspector: 2.0, Developer email: evansergi851@outlook.com")

def inspect_url():
    code = url.get(1.0, "end-1c")
    url.destroy()
    text.destroy()
    inspect.destroy()
    x = requests.get(code)
    inputtxt = Text(t, height = None, width = None, bg = "white")
    inputtxt.pack(expand=True, fill=BOTH)
    inputtxt.insert(INSERT, x.text)
    scrollbar.config(command = inputtxt.yview)

def online_help():
    webbrowser.open('https://sites.google.com/view/superinspector')
# Files Menu Bar
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Window', command = new_window)
file.add_command(label ='Quit', command = close_window)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About', command = about)
help_.add_command(label ='Help', command = online_help)
t.config(menu = menubar)

#Interface
text = Label(t, text="Enter url to inspect")
text.pack()

url = Text(t, height = 1, width = 40, bg = "white")
url.pack()

inspect = Button(t, text = "Inspect", command = inspect_url)
inspect.pack()

t.mainloop()
