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
		self.pack()
		# call method
		self.all_here()

	# method
	def all_here(self):
		# create label widget inside the object attribute
		self.index = Label(self)
		self.index["text"] = "Jogu Sasik Numeru"
		self.index["fg"] = "white"
		self.index["bg"] = "lightblue"
		self.index["font"] = ("fira code", 15)
		self.index.pack()

		# separator
		self.separator = Frame(self, height=4, bd=2, relief=GROOVE)
		self.separator.pack(fill=X,expand=1)

		# input from user
		self.inputuser = Entry(self)
		self.inputuser["justify"] = "center"
		self.inputuser.pack()

		# button confirm to verify
		self.confirm = Button(self)
		self.confirm["text"] = "konfirma"
		self.confirm["bg"] = "green"
		self.confirm["fg"] = "white"
		self.confirm["command"] = self.checked
		self.confirm.pack()

		# button delete number of user
		self.delete = Button(self, text="delete", fg="white", bg="red", command=self.delt)
		self.delete.pack()

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
		except Exception as err:
			self.inputuser.insert(END, ' --> laos numeru!')

	def delt(self):
		self.inputuser.delete(0, END)