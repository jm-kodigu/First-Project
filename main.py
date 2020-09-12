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
		self.config(bg="white")
		self.all_here()

	def all_here(self):
		# this is info for project
		self.info = Toplevel()
		self.info.geometry("240x100")

		self.m = Message(self.info, text="This is program built with Tk 8.5 and Random Choice module.", fg="blue", bg="white")
		self.m.pack()

		self.dismiss = Button(self.info, text="DISMISS", bg="red", fg="white", command=self.info.destroy)
		self.dismiss.pack()

		self.info.config(bg="white")
		# end of this is info for project

		# all here user need
		self.heading = Label(self)
		self.heading["text"] = "Random JM"
		self.heading["bg"] = "white"
		self.heading["fg"] = "blue"
		self.heading["font"] = ("Cooper Black",30)
		self.heading.pack(pady=20)

		self.info_here = Label(self)
		self.info_here["text"] = "\"your lucky is good to choice right number in application.\"\n\nnumber start by 0 to 10!"
		self.info_here["bg"] = "white"
		self.info_here["font"] = ("Times New Roman Italic",14)
		self.info_here.pack(pady=5)

		# promt to user insert a number
		self.user_number = Entry(self, justify=CENTER, width=15)
		self.user_number.pack(pady=10)
		# end of prompt to user insert a number

		# button here
		self.button_frame = Frame(self, bg="white")
		self.button_frame.pack(pady=8)

		self.b1 = Button(self.button_frame, text="Insert", bg="green", fg="white", command=self.tested_number)
		self.b1.grid(row=0, column=0, padx=8)

		self.b2 = Button(self.button_frame, text="Delete", bg="red", fg="white", command=self.deleted)
		self.b2.grid(row=0, column=1, padx=8)
		# end of button here

		self.result = Label(self)
		self.result["text"] = "Info Here!"
		self.result["bg"] = "white"
		self.result["font"] = ("Fira Code Regular",12)
		self.result.pack(pady=20)

		# end of all here user need

	def tested_number(self):
		try:
			a = [0,1,2,3,4,5,6,7,8,9,10]
			your_number = int(self.user_number.get())
			if( your_number == choice(a) ):
				self.result.config(text="You Won. you very lucky today!", fg="blue")
			elif( your_number > choice(a) ):
				self.result.config(text="your number is a BIG!", fg="red")
			elif( your_number < choice(a) ):
				self.result.config(text="your number is a SMALL!", fg="blue")
			else:
				self.result.config(text="This is not a number!", fg="white", bg="red")
		except Exception as err:
			print("error :", err)

	def deleted(self):
		self.user_number.delete(0, END)
		self.result.config(text="Info Here!", fg="black", bg="white")

root = Tk()
root.iconbitmap("icon.ico")
root.title("JM-Kodigu")
root.geometry("600x400")

app = App(master=root)

root.config(bg="white")
root.mainloop()