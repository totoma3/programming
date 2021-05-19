class Terranimal:
    def __init__(self,irum,age,gender):
        self.irum=irum
        self.age=age
        self.gender=gender
    def food_func(self):
        print(self.irum +"는(은) 먹이를 먹습니다.")
    def sleep_func(self):
        print(self.irum +"는(은) 낮에 1~3시간 낮잠을 잡니다.")

#고양이 클래스 Cat 생성
class cat(Terranimal):
    def __init__(self,irum,age,gender,kind):
        Terranimal.__init__(self,irum,age,gender)
        self.kind=kind
    def food_func(self):
        Terranimal.food_func(self)
        if self.age <=2:
            print("어린 고양이용 kitten을 먹이세요")
        else:
            print("indoor용을 먹이세요")

#고양이 객체생성
mycat=cat("미고",3,"male","러시안블루")
mycat.food_func()
wecat=cat("샤이니",1,"female","터키쉬")
wecat.food_func()
