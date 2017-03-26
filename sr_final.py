import speech_recognition as sr
import os, time
import d,Tkinter
import parser

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "248e4059386e47578fe9f1ad571a59e4" 
# Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings

r=sr.Recognizer()
m=sr.Microphone()


#functions to be used
def termination(str):
	temp=str.split()
	end_strings=["quit","exit","bye","goodbye","seeya","terminate","end","close"]
	for word in end_strings:
		for word1 in temp:
			if word==word1:
				return True
	return False 

def sleeper():
	''' try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		return'''
	try:
		while True:
			with m as source: r.adjust_for_ambient_noise(source)
			with m as source: audio=r.listen(source)
			try:
				value=r.recognize_bing(audio,key=BING_KEY)
				if value=="continue": return
			except sr.UnknownValueError as e:
				pass
	except KeyboardInterrupt: return


def startRecognizer():
	parent=Tkinter.Toplevel(bg="gray",bd=4,height=100,width=300,relief=Tkinter.RAISED)
	parent.title("Mic on")
	parent.resizable(False,False)

	txt=Tkinter.StringVar()
	txt.set("Hi! I am Desktop Buddy.")
	label=Tkinter.Label(parent,anchor=Tkinter.CENTER,textvariable=txt)
	label.pack()

	
	
	try:
		txt.set("A moment of silence, please....configuring energy threshold to ")
		print("1")
		with m as source: r.adjust_for_ambient_noise(source)
		txt.set(r.energy_threshold)
		parent.update_idletasks()
		r.dynamic_energy_threshold=True
		r.dynamic_energy_adjustment_ratio=1.3
		r.pause_threshold=0.5

		while True:
			with m as source: r.adjust_for_ambient_noise(source, duration=0.5)
			txt.set("Hi! How may I help you?")
			parent.update_idletasks()

			with m as source: audio=r.listen(source)
			txt.set("Interpreting...")
			parent.update_idletasks()
			try:
				value=r.recognize_bing(audio,key=BING_KEY)
				if termination(value):
					break
				else:
					txt.set(value)
					parent.update_idletasks()
					if parser.UniversalParser(value)==False:
						txt.set("Sorry, no command found!")
						parent.update_idletasks()
					sleeper()
			except sr.UnknownValueError as e:
						txt.set("Sorry! Unable to recognize!")
						parent.update_idletasks()

		#after the program ends
		txt.set("Have a good time!")
		parent.update_idletasks()
		parent.withdraw()
	except KeyboardInterrupt:
		pass

	



