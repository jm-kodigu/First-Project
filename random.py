from tkinter import *
import random as rdm

# template
class Random(Frame):
	# const __init__
	def __init__(self,master=None):
		# call const __init__ in superclass
		super().__init__(master)
		# override 
		self.master = master
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



root = Tk()
root.title("Random JM")

# object
app = Random(master=root)
root["bg"] = "lightblue"
root.mainloop()