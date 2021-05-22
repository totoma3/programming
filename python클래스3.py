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
mydog=Dog("슈슈",10,"long")
mydog.kind="슈나우저"
print("우리강아지 이름",mydog.irum)
mydog.paw_info()
yourdog=Dog("제롬",8,"short")
print("당신의 애견이름",yourdog.irum)
yourdog.paw_info()
