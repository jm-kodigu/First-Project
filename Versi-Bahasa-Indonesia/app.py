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
		self.config(bg="lightblue")
		# call method
		self.all_here()

	# method
	def all_here(self):
		# create label widget inside the object attribute
		self.index = Label(self)
		self.index["text"] = "Game Menebak Angka"
		self.index["fg"] = "white"
		self.index["bg"] = "lightblue"
		self.index["font"] = ("fira code bold", 15)
		self.index.pack()

		self.index2 = Label(self)
		self.index2["text"] = "dari 1 sampai 10!"
		self.index2["fg"] = "black"
		self.index2["bg"] = "lightblue"
		self.index2["font"] = ("fira code semibold", 12)
		self.index2.pack()
	
		# input from user
		self.inputuser = Entry(self)
		self.inputuser["justify"] = "center"
		self.inputuser.pack()
		# default value
		self.inputuser.delete(0, END)
		self.inputuser.insert(0, '0')

		# bottom paned
		bp = Frame(self, bg="lightblue")
		bp.pack(side=BOTTOM)

		# button confirm to verify
		self.confirm = Button(bp)
		self.confirm["text"] = "Konfirmasih"
		self.confirm["bg"] = "green"
		self.confirm["fg"] = "white"
		self.confirm["command"] = self.checked
		self.confirm.pack(side=LEFT,padx=5,pady=10)

		# button delete number of user
		self.delete = Button(bp, text="Hapus", fg="white", bg="red", command=self.delt)
		self.delete.pack(side=LEFT,padx=5,pady=10)


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
				self.inputuser.insert(0, ':) anda benar!')
			elif yournumber > choice(numbs):
				self.inputuser.insert(END, ' --> terlalu BESAR!')
			elif yournumber < choice(numbs):
				self.inputuser.insert(END, ' --> terlalu RENDAH!')
		except ValueError:
			self.inputuser.insert(END, ' --> bukan angka!')

	def delt(self):
		self.inputuser.delete(0, END)