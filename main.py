from tkinter import *
from Func import *



root = Tk()
root.geometry("950x800")

frameTop = Frame(master = root, relief = SUNKEN, borderwidth = 10,bg = "red", width = 200, height = 100 )
frameTop.pack(fill = X, side = TOP)

labelSteel = Label(frameTop, fg = "black", text="hello", font = "Helvetica 18 bold")
labelSteel.grid(column = 0, row = 0)


frameRight = Frame(root, relief = SUNKEN, borderwidth = 10, bg = "yellow", width = 300)
frameRight.pack(fill = Y, side = RIGHT)
butHire = Button(frameRight, text = "HIRE CREW")
butHire.pack()

frameBottom = Frame(root, relief = SUNKEN, borderwidth = 10, bg="blue", height = 200)
frameBottom.pack(fill = X, side = BOTTOM)

frameLeft = Frame(root, borderwidth = 10,  width =root.winfo_reqwidth())
frameLeft.pack(fill = Y, side= LEFT)

trueSteelTime(labelSteel)


root.mainloop()
