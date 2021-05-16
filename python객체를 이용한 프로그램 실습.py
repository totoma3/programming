import random
class Datain:
    def __init__(self,data):
        self.data=data
#핵심클래스 구현
class Process:
    #리스트 자료형 선언/그 안에 각각의 객체를 추가
    def __init__(self):
        self.datalist=[]
        for i in range(1,46):
            self.datalist.append(Datain(i))
    #리스트 순서를 섞기
    def choice_data(self):
        random.shuffle(self.datalist)
        return self.datalist[0:6]

class Inout:
    def __init__(self):
        self.pro=Process()
    def play_start(self):
        choice=self.pro.choice_data()
        for info in choice:
            print("%d"%(info.data),end=" ")
#메인프로그램
a=Inout()
print("로또번호를 알려드릴께요.")
a.play_start()
