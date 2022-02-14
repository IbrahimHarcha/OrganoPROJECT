
import tkinter as tk

class Root:
	def __init__(self):
		self.root = tk.Tk()
		self.widgets()

	def widgets(self):
	
		button = tk.Button(self.root,text="jouer", bg="blue", fg = "white", font=("Pristina", 20))
		button.place(anchor=tk.W, relheight=0.25, relwidth=0.25, relx=0.4, rely= 0.4)


def main():
	app = Root()
	app.root.mainloop()

main()
