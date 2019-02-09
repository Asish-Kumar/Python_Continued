"""
Some Useful links:
http://www.tkdocs.com
https://docs.python.org/3/library/tk.html
"""
import tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()
########################=========Pack Geometry Manager======###########################
# mainWindow = tkinter.Tk()
# mainWindow.title("Main Window")
# mainWindow.geometry('640x480')
#
# label = tkinter.Label(mainWindow, text="Hello python")
# label.pack(side='top')
#
# frameA = tkinter.Frame(mainWindow)  # creating an empty frame to hold other widgets
# frameA.pack(side='left', anchor='n')  # anchor to the north, other options are: n,s,w,e,nw,se,sw,ne
#
# button = tkinter.Button(frameA, text="Button")  # Button will be put on the frameA
# button.pack(side='top')
#
# mainWindow.mainloop()  # give the control to Tk for displaying the mainWindow

########################=========Grid Geometry Manager======###########################
mainWindow = tkinter.Tk()
mainWindow.title("Main Window")
mainWindow.geometry("1920x1080")

frameA = tkinter.Frame(mainWindow)
frameA.grid(row=0, column=0)

frameB = tkinter.Frame(mainWindow)
frameB.grid(row=0, column=1, sticky='ne')  # use sticky='n' or 's' or 'e' or 'w' or 'ne' etc.

label1 = tkinter.Label(frameA, text="Hello World")
label1.grid(row=0, column=0)  # use label1.grid() for auto alignment

label2 = tkinter.Label(frameA, text="Howdy World")
label2.grid(row=2, column=0)  # the coulumn number are relative, try setting column=8 and column=0

button1 = tkinter.Button(frameB, text="Click1")
button1.grid()

button2 = tkinter.Button(frameB, text="Click2")
button2.grid()

mainWindow.grid_columnconfigure(0, weight=0)

mainWindow.mainloop()
