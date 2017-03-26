import Tkinter
import sr_final
import parser
import music

#functions to be called when buttons are clicked
def onMic():
	sr_final.startRecognizer()
	return

def onChangeBG():
	return

def onPlayMusic():
	music.get_link("angry")
	return


#application window
root=Tkinter.Tk()
root.title("Desktop Buddy")
root.geometry("400x120")
root.resizable(width=False,height=False)

def onSubmit(obj1,obj2):
	parser.UniversalParser(obj1.get("1.0",'end-1c'))
	del(obj2)
	return


def onManualEntry():
	f1=Tkinter.Tk()#height=200,width=380)
	etext=Tkinter.Text(f1,height=5,width=50)
	submit=Tkinter.Button(f1,command=lambda: onSubmit(etext,f1),text="Submit",height=2,width=10)
	etext.pack(side=Tkinter.TOP)
	submit.pack(side=Tkinter.TOP)
	f1.mainloop()
	return
	


#parent frame
frame1=Tkinter.Frame(root)
#Tkinter.Frame(root,bg="black",bd=40,highlightbackground="blue",highlightcolor="yellow",highlightthickness=40)
frame1.pack(side=Tkinter.BOTTOM)

#buttons frame
bframe=Tkinter.LabelFrame(root,height=110,width=390,text="Pick an action",bd=4)
bframe.pack()
#accessory frame
frame2=Tkinter.Frame(bframe,height=90,width=280)

#buttons
b1=Tkinter.Button(frame2, command=onManualEntry,text="Manual entry", activeforeground="white",activebackground="gray",bd=4,fg="black",height=2,highlightcolor="green",relief=Tkinter.RAISED,width=30)
img=Tkinter.PhotoImage(file="mic.gif").subsample(8,8)
b2=Tkinter.Button(bframe,command=onMic,image=img,height=100,width=100,bd=4,relief=Tkinter.RAISED)
b2.pack(side=Tkinter.LEFT)
b3=Tkinter.Button(frame2,command=onPlayMusic,text="Play Mood-dependent Music",activeforeground="white",activebackground="gray",bd=4,fg="black",height=2,highlightcolor="green",relief=Tkinter.RAISED,width=30)
b3.pack(side=Tkinter.TOP)
b4=Tkinter.Button(frame2,command=onChangeBG,text="Change background",activeforeground="white",activebackground="gray",bd=4,fg="black",height=2,highlightcolor="green",relief=Tkinter.RAISED,width=15)
b4.pack(side=Tkinter.LEFT)
b1.pack(side=Tkinter.TOP,expand=False)
frame2.pack(side=Tkinter.LEFT)












root.mainloop()
