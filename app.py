from tkinter import *
from random import choice


# template
class Rdm(Frame):
	# const __init__
	def __init__(self,master=None):
		# call const __init__ in superclass
		super().__init__(master)
		# override 
		self.master=master
		self.grid(padx=30,pady=28)
		# call method
		self.all_here()

	# method
	def all_here(self):
		# create label widget inside the object attribute
		self.index = Label(self)
		self.index["text"] = "Jogu Sasik Numeru"
		self.index["fg"] = "white"
		self.index["bg"] = "lightblue"
		self.index["font"] = ("fira code bold", 15)
		self.index.grid(row=0,columnspan=2)

		self.index2 = Label(self)
		self.index2["text"] = "husi 1 to 10!"
		self.index2["fg"] = "black"
		self.index2["bg"] = "lightblue"
		self.index2["font"] = ("fira code semibold", 12)
		self.index2.grid(row=1,columnspan=2)

		# input from user
		self.inputuser = Entry(self)
		self.inputuser["justify"] = "center"
		self.inputuser.grid(row=3,columnspan=2,pady=9)
		# default value
		self.inputuser.delete(0, END)
		self.inputuser.insert(0, '0')

		# button confirm to verify
		self.confirm = Button(self)
		self.confirm["text"] = "Konfirma"
		self.confirm["bg"] = "green"
		self.confirm["fg"] = "white"
		self.confirm["command"] = self.checked
		self.confirm.grid(row=4,column=0)

		# button delete number of user
		self.delete = Button(self, text="Hamos", fg="white", bg="red", command=self.delt)
		self.delete.grid(row=4,column=1)

	def checked(self):
		try:
			# random number 
			numbs = [1,2,3,4,5,6,7,8,9,10]

			# create local variable to get input
			numberuser = self.inputuser.get()
			# convert to int type
			yournumber = int(numberuser)

			if yournumber == choice(numbs):
				self.inputuser.delete(0, END)
				self.inputuser.insert(0, ':) si\'ik lo\'os!')
			elif yournumber > choice(numbs):
				self.inputuser.insert(END, ' --> bo\'ot liu!')
			elif yournumber < choice(numbs):
				self.inputuser.insert(END, ' --> ki\'ik liu!')
		except ValueError:
			self.inputuser.insert(END, ' --> laos numeru!')

	def delt(self):
		self.inputuser.delete(0, END)