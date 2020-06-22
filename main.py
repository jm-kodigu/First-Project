from app import *

root = Tk()

root.title("Random JM")
root.geometry("270x175")

# object
app = Rdm(master=root)
root["bg"] = "lightblue"
root.mainloop()