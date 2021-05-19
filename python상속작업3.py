class Sample:
    def __init__(self,val1):
        self.val1=val1
    def __add__(self,val1):
        self.val1+=val1
    def __sub__(self,val1):
        self.val1-=val1
        
a=Sample(100)
a-50
print("결과=",a.val1)
