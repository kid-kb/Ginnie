from tkinter import *
import wikipedia
from tkinter.font import Font


def get_data():
    srch_data = data.get()
    ans.delete(1.0, END)
    try:
        ans_val = wikipedia.summary(srch_data)
        ans.insert(INSERT, ans_val)
    except:
        ans.insert(INSERT,"Please check your string or internet connection")


root = Tk()
my_font = Font(family="Comic Sans Ms",size=16)
root.title("Ginnie")
root.geometry("300x350+500+200")
topframe = Frame(root)

data=Entry(topframe)
data.pack()

but = Button(topframe,text="Search",command=get_data,fg='green')
but.pack()

bottomframe = Frame(root)
scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

ans = Text(bottomframe, width=30, height=15, yscrollcommand=scroll.set, wrap=WORD,font=my_font,bg="#f1f1f1")
scroll.config(command=ans.yview())
ans.pack(side=LEFT)

topframe.pack(side=TOP)
bottomframe.pack()
root.mainloop()
