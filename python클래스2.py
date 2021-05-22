class Dog:
    #init메소드 이용한 객체 초기화작업
    def __init__(self,irum,age,paw):
        self.irum=irum
        self.age=age
        self.paw=paw
        
    #메소드지정
    def paw_info(self):
        if self.paw=="short":
            print("점프가능높이:30cm")
        else:
            print("점프가능높이:100cm")

#메인부분
mydog=Dog()
mydog.irum="슈슈"
mydog.age=10
mydog.paw="long"
mydog.kind="슈나우저"
mydog.paw_info()
yourdog=Dog()
yourdog.irum="제롬"
yourdog.age=8
yourdog.paw="short"
yourdog.paw_info()
