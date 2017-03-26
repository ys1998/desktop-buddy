from Tkinter import *
import ttk
def display_score(l,output):
    root = Tk()
    root.title("Cricket Score")

    mainframe = ttk.Frame(root, padding="3 4 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    if l==0:
        Title = ttk.Label(mainframe, text="No Running Match").grid(column=1, row=1 ,sticky=E)
    else:
        for i in range(0,l):
            #print l
            Title = ttk.Label(mainframe, text="Match"+str(i+1)).grid(column=1, row=(4*i+1) ,sticky=E)
            #print i
            Teams = ttk.Label(mainframe, text=output[i][0]).grid(column=1, row=(4*i+2) ,sticky=E)
            Score = ttk.Label(mainframe, text=output[i][1]).grid(column=2, row=(4*i+3) ,sticky=E)
            Overs = ttk.Label(mainframe, text=output[i][2]).grid(column=1,columnspan=2, row=(4*i+4) ,sticky=E)

            #ttk.Label(mainframe, text="Enter Your message").grid(column=1, row=1, sticky=W)
            ttk.Label(mainframe, text="Score").grid(column=1, row=(4*i+3), sticky=E)
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    root.mainloop()
