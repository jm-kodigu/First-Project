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
		self.info = Toplevel()
		self.info.geometry("240x100")

		self.m = Message(self.info, text="This is program built with Tk 8.5 and Random Choice", fg="blue")
		self.m.pack()

		self.dismiss = Button(self.info, text="DISMISS", bg="red", fg="white", command=self.info.destroy)
		self.dismiss.pack()



root = Tk()
root.iconbitmap("icon.ico")
root.title("JM-Kodigu")
root.geometry("600x400")

app = App(master=root)

root.mainloop()