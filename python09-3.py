from tkinter import *
def co():
    txt1.config(bg="red")
    return
root=Tk()
root.title("실습화면")
txt1=Text(root,height=2,width=30)
txt1.pack()
button1=Button(root,text="빨간색",command=co)
button1.pack()
button=Button(root,text="종료하기",command=quit)
button.pack()
root.mainloop()
