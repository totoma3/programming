class Sample:
    def __init__(self,irum,val1):
        self.irum=irum
        self.val1=val1
    def val_info(self):
        print("이름:"+self.irum+"현재 값: "+str(self.val1))
    def __add__(self,other):
        self.val1+=other.val1
    def __sub__(self,val1):
        self.val1-=val1
        
one=Sample("one",30)
two=Sample("two",50)
one.val_info()
two.val_info()
print()
one+two
one.val_info()
two.val_info()
