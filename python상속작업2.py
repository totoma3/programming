class Terranimal:
    def __init__(self,irum,age,gender):
        self.irum=irum
        self.age=age
        self.gender=gender
    def food_func(self):
        print(self.irum +"는(은) 먹이를 먹습니다.")
    def sleep_func(self):
        print(self.irum +"는(은) 낮에 1~3시간 낮잠을 잡니다.")

#강아지 클래스 Dog 생성
class Dog(Terranimal):
    def __init__(self,irum,age,gender,kind):
        Terranimal.__init__(self,irum,age,gender)
        self.kind=kind
    def sleep_func(self):
        Terranimal.sleep_func(self)
        print(self.kind + "인 "+self.irum+"는(은) 밤에 집을 지킵니다.")
    def gubun_func(self):
        Terranimal.food_func(self)
        if self.kind=="도베르만" or self.kind=="쉐퍼드":
            print("대형견-사료외에 영양분 2가지를 더 추가하여 먹이세요")
      

#강아지 객체생성
mydog=Dog("쮸니",3,"female","도베르만")
mydog.sleep_func()
mdog=Dog("장군",10,"male","치와와")
mydog.gubun_func()
