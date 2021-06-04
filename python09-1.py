from tkinter import *
def clear():
    txt1.delete(1.3,END) #처음부터 3글자만 놔두고 뒤를 지우는것 delete(0.0,end)은 첨부터 마지막까지 지우는것
    return
top=Tk()
top.title("연습창")
top.geometry("200x200")
lbl1=Label(top,text="여러분 반가워요. 소감을 써주세요")
lbl1.pack()
txt1=Text(top,height=2,width=30,bg="pink")
txt1.pack()
btn1=Button(top,text="클릭하세요",bg="orange",fg="gray",command=clear)
btn1.pack()
top.mainloop()
