import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.title("hwllo world app")
window.geometry("200x100")

def say_hello():
    print("hello there")

hello_button=ttk.Button(window,text="say hello",command=say_hello)
hello_button.pack()
window.mainloop()