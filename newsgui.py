from Tkinter import *
import ttk
def news_print(dicto):
    root = Tk()
    root.title("News For U")
    l = (len (dicto))

    mainframe = ttk.Frame(root, padding="3 4 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    if l==0:
        Title = ttk.Label(mainframe, text="Nothing Important Going On").grid(column=1, row=1 ,sticky=W)
    else:
        for i in range(0,l):
            if (i < 3):
                Title = ttk.Label(mainframe, font="ARIAL 14 bold" ,text=dicto[i]["author"]).grid(column=1, row=(4*i+1) ,sticky=W)
                Teams = ttk.Label(mainframe, text=dicto[i]["title"]).grid(column=1, row=(4*i+2) ,sticky=W)
                Score = ttk.Label(mainframe, text=dicto[i]["description"]).grid(column=1, row=(4*i+3) ,sticky=W)
                Overs = ttk.Label(mainframe, text=dicto[i]["publishedAt"]).grid(column=1,columnspan=2, row=(4*i+4) ,sticky=W)

                #ttk.Label(mainframe, text="Enter Your message").grid(column=1, row=1, sticky=W)
                #ttk.Label(mainframe, text="Score").grid(column=1, row=(4*i+3), sticky=E)
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    root.mainloop()
    return True
