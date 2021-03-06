import tkinter #as tk
def write_slogan():
    print("tkinter is easy to use")
root=tkinter.Tk()
frame=tkinter.Frame(root)
frame.pack()

button=tkinter.Button(frame,text="QUIT",fg="green",bg="red",command=quit)
button.pack(side=tkinter.LEFT)
slogan=tkinter.Button(frame,text="HELLO",command=write_slogan)
slogan.pack(side=tkinter.LEFT)
root.mainloop()
