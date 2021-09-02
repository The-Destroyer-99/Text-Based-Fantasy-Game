import time
import sys
import os
import cursor

def fasttype(a):
	for b in a:
		time.sleep(0.003)
		sys.stdout.write(b)
		sys.stdout.flush()

def midtype(a):
	for b in a:
		time.sleep(0.03)
		sys.stdout.write(b)
		sys.stdout.flush()

def slowtype(a):
	for b in a:
		time.sleep(0.08)
		sys.stdout.write(b)
		sys.stdout.flush()

#here is the animation
def spin_animate():
	for i in range(5):
		sys.stdout.write('\rloading |')
		time.sleep(0.03)
		sys.stdout.write('\rloading /')
		time.sleep(0.03)
		sys.stdout.write('\rloading -')
		time.sleep(0.03)
		sys.stdout.write('\rloading \\')
		time.sleep(0.03)

	os.system('clear')

	sys.stdout.write('\rDone!')

skipped_1 = True


def intro():
	midtype('Do you want to see the intro? (Press any key for yes, \"no\" for no) --> ')
	intro_choise = input()
	if intro_choise.lower() != 'no':
		os.system("clear")
		cursor.show()
		slowtype("Crisis Year 284, in front of the Demon’s Palace:")
		input()
		midtype("Luya: Neve has fainted already... We have to hurry up... Rudolph... I'm afraid he won't last long...")
		input()
		midtype("Carter: No, Vic, you teleport them back first. The Demon is weak now, I think I can kill It!")
		input()
		midtype("Viclow: See you at the resurrection stone! Good luck!")
		input()
		midtype("Viclow: ")
		slowtype("Incantaion - RAIN OF BLOOD!!!")
		input()
		midtype("Hackma: Oww...")
		input()
		midtype("Carter: Watch! I can defidently finish him this time!")
		input()
		midtype("Carter: ")
		slowtype("DIE!!!")
		input()
		slowtype("Crisis Year 86, Three Empires of Mankind United and counter attacked the Demon and opened the prelude of the Fifth World War...")
		input()
		midtype("At the beginning of the war, humans advanced layer by layer with the help of anicent ruins, and recovered a large area of lost ground in just one hundred years.")
		input()
		midtype("The front line approached the Lair of Demon in year 284.")
		input()
		midtype("However, when the soldiers approached the Vocalno and the victory was in sight, the Demon made a desperate effort to summon the tyrannical ancient evil god")
		slowtype("... turning the whole world into scorched wasteland...")
		input()
		slowtype("Humans,\n")
		slowtype("Monsters,\n")
		slowtype("Angels,\n")
		slowtype("Elements,")
		input()
		midtype("Even including the small species that haven't even participated in the war, all lives are not spared...")
		input()
		midtype("Hundreds of years have passed in the chaos...")
		input()
		midtype("After everything settled down again, the surviving broken souls returned to the circle. ")
		slowtype("Ready to start building a new life.")
		input()
		midtype("You: Damn monsters, dare to oppress mankind this far...")
		input()
		midtype("You: Thanks to my goddess for rebirth, this time we must completely eliminate the monsters and save the world!")
		input()
		skipped_1 = False
		os.system('clear')
		return

def jobs():
	while True:
		if skipped_1 == False:
			midtype("As for you, what's your job before your rebirth?\n")
		elif skipped_1 == True:
			midtype("What's your job?\n")
		midtype("""1) Warrior
2) Priest
3) Wizard
4) Paladin
5) Assassin
(Please enter the corrsponding number) --> """)
		job_number = input()
		os.system("clear")
		if job_number == '1':
			Strength = 2
			Speed = 1
			slowtype("Now, you become a whole new being, with Full of Strength and Speed, as known as...")
			input()
			midtype("Slime")
			input()
			os.system("clear")
			break
		elif job_number == '2':
			Endurance = 1
			Perceive = 2
			slowtype("Now, you become a whole new being, with Full of Perceive and Endurance, as known as...")
			input()
			midtype("Slime")
			input()
			os.system("clear")
			break
		elif job_number == '3':
			Perceive = 1
			Intelligence = 2
			slowtype("Now, you become a whole new being, with Full of Intelligence and Perceive, as known as...")
			input()
			midtype("Slime")
			input()
			os.system("clear")
			break
		elif job_number == '4':
			Strength = 1
			Endurance = 2
			slowtype("Now, you become a whole new being, with Full of Endurance and Strength, as known as...")
			input()
			midtype("Slime")
			input()
			os.system("clear")
			break
		elif job_number == '5':
			Strength = 1
			Speed = 2
			slowtype("Now, you become a whole new being, with Full of Speed and Strength, as known as...")
			input()
			midtype("Slime")
			input()
			os.system("clear")
			break
		else:
			print('Please enter the corrsponding number')
			input()
			os.system("clear")
def startmemu():
	while True:
		midtype("""Welcome to the game!
1)Start your story
2)Time Skip (If you played before)
3)Caution
4)Credits
5)Dev Help Page
""")
		startchoice = input()
		if startchoice == '1':
			os.system("clear")
			break
		elif startchoice == '2':
			print()
			midtype("In process")
			input()
			os.system("clear")
		elif startchoice == '3':
			print()
			midtype('There are in-game tips. DO NOT SPAM ENTER. We didn\'t use any (not a lot) time.sleep(A technical term.) in this game, plots are proceed with enter. So please don\'t spam it.')
			input()
			os.system("clear")
		elif startchoice == '4':
			midtype("somebody fill this gap")
			input()
			os.system("clear")
		elif startchoice == '5':
			startPassword = str(input("Dev password:\t"));
			if startPassword == os.environ['StartMenuPasswordSecret']:
				print("Thank you Devs!")
		else:
			print('Please enter the corrsponding number')
			input()
			os.system("clear")