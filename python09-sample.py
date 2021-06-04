from tkinter import *
root=Tk()
root.title("작업화면")
root.geometry("200x200")
button=Button(root,text="종료하기",command=quit)
button.pack()
root.mainloop()
