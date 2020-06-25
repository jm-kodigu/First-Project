from app import *

root = Tk()

root.title("Random JM")
root.geometry("260x160")

# object
app = Rdm(master=root)
root["bg"] = "lightblue"
root.mainloop()