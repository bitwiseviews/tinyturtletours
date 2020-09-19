# Underlying graphics for turtle is Tkinter

#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter

import sys
if sys.version_info.major == 3:
    import tkinter as Tk, tkinter.font as tkFont
else:
    import Tkinter as Tk, tkFont

root = Tk.Tk()

fonts=list(Tk.font.families())
fltr = filter(lambda x: (x.rfind('Noto') != -1), fonts)
fontLst = list(fltr)
fonts = fontLst
fonts.sort()

# https://stackoverflow.com/a/47415907/10645311
def getFonts():
    res = []
    res.append(tkFont.families())
    res.append(tkFont.names())
    return res

def populate(fonts, frame):
    '''Put in the fonts'''
    listnumber = 1
    for item in fonts:
        label = "listlabel" + str(listnumber)
        label = Tk.Label(frame,text=item,font=(item, 17)).pack()
        listnumber += 1

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

# https://stackoverflow.com/a/53717785/10645311    
def listFontsDefined(fontLst = ['Nimbu Sans']):
    root = Tk.Tk()
    
    root.title('Font Families')
    canvas = Tk.Canvas(root, borderwidth=0, background="#ffffff")
    frame = Tk.Frame(canvas, background="#ffffff")
    vsb = Tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(fonts, frame)

    root.mainloop()

