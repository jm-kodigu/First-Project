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
		# this is info for project
		self.info = Toplevel()
		self.info.geometry("240x100")

		self.m = Message(self.info, text="This is program built with Tk 8.5 and Random Choice module.", fg="blue")
		self.m.pack()

		self.dismiss = Button(self.info, text="DISMISS", bg="red", fg="white", command=self.info.destroy)
		self.dismiss.pack()
		# end of this is info for project

		# all here user need
		self.heading = Label(self)
		self.heading["text"] = "Random JM"
		self.heading["fg"] = "blue"
		self.heading["font"] = ("Cooper Black",30)
		self.heading.pack(pady=20)

		self.info_here = Label(self)
		self.info_here["text"] = "\"your lucky is good to choice right number in application.\""
		self.info_here["font"] = ("Times New Roman Italic",12)
		self.info_here.pack(pady=5)

		# promt to user insert a number
		self.user_number = Entry(self, justify=CENTER, width=15)
		self.user_number.pack(pady=10)
		# end of prompt to user insert a number

		# end of all here user need

root = Tk()
root.iconbitmap("icon.ico")
root.title("JM-Kodigu")
root.geometry("600x400")

app = App(master=root)

root.mainloop()