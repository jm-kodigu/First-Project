"""
this project, i make with tkinter 8.5 and random module
to make this project

author : https://github.com/jm-kodigu/
"""

from tkinter import *
from tkinter import messagebox
from random import choice 

class App(Frame):

	def __init__(self,master=None):
		super().__init__(master)
		self.pack()
		self.all_here()

	def all_here(self):
		pass


root = Tk()
root.iconbitmap("icon.ico")
root.title("JM-Kodigu")
root.geometry("600x400")

app = App(master=root)

root.mainloop()