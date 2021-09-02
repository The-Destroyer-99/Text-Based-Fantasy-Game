#made by TheSuperDevTeam
import random
import Plots
from Plots import Intro, firstplot
import os
import sys
import time
from time import sleep as slp
import cursor
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.hello = tk.Button(self)
		self.hello["text"] = "CREDITS"
		self.hello["command"] = self.sayHello
		self.hello.pack(side="top")
		self.quit = tk.Button(self,text="START GAME",command=self.master.destroy)
		self.quit.pack(side="bottom")
	def sayHello(self):
		self.display = tk.Label(self,text="Made by TheSuperDevTeam")
		self.display.pack()
#Made by IndyRishi

#Made by ChristopherDai
def fasttype(a):
	for b in a:
		slp(0.005)
		sys.stdout.write(b)
		sys.stdout.flush()

def midtype(a):
	for b in a:
		slp(0.05)
		sys.stdout.write(b)
		sys.stdout.flush()

def slowtype(a):
	for b in a:
		time.sleep(0.1)
		sys.stdout.write(b)
		sys.stdout.flush()
cursor.hide()

#Made by ChristopherDai

#Made by IndyRishi
root = tk.Tk()
app = Application(master=root)
app.mainloop()

slp(1)
#Made by IndyRishi

Strength = 0
Speed = 0
Endurance = 0
Perceive = 0
Intelligence = 0

#Made by TheDestroyer99
Intro.spin_animate()
slp(1)
os.system("clear")
#Made by No me
cursor.show()
Intro.startmemu()
Intro.intro()
Intro.jobs()

