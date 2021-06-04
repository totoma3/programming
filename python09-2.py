from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.withdraw()
msg.showinfo("업데이트알림","1개의 업데이트 정보알림")
msg.askyesnocancel("종료","현재 프로그램 종료하시겠습니까?")

