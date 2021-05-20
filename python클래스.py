class Cat:
    #클래스에 속성지정
    irum="미고"
    age=2
    #클래스에 함수지정(메소드)
    def basic_prnt(self):
        print("야옹야옹")
    def detail_prnt(self):
        print("고양이 이름",self.irum)
        print("고양이 나이",self.age)
        self.basic_prnt()
        
#메인시작
mcat=Cat()
#print("우리집 고양이 이름",mcat.irum)
#mcat.basic_prnt()
mcat.detail_prnt()



