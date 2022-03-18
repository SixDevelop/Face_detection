from tkinter import *
from tkinter import ttk

from matplotlib.pyplot import title

root = Tk()
root.title('task2')
root.geometry('2000x1400')

tmeth = Label(root, text='Метод').grid(row = 1, column=2)
r_var = IntVar()
r_var.set(0)
zero = Radiobutton(root, text = 'Not chosen', variable=r_var, value=0)
thyst = Radiobutton(root, text = 'Hystogram', variable=r_var, value=1).grid(row=2,column=2,sticky="w")
tdft = Radiobutton(root, text = 'DFT', variable=r_var, value=2).grid(row=3,column=2,sticky="w")
tdct = Radiobutton(root, text = 'DCT', variable=r_var, value=3).grid(row=4,column=2,sticky="w")
tscale = Radiobutton(root, text = 'Scale', variable=r_var, value=4).grid(row=5,column=2,sticky="w")
tgrad = Radiobutton(root, text = 'Gradient', variable=r_var, value=5).grid(row=6,column=2,sticky="w")

root.mainloop()