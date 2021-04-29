dic={"A":90,"B":95,"C":94,"D":85,"E":97}

for i,j in dic.items():
        print(i,":",j)
  
a=sum(dic.values())
b=sum(dic.values())/len(dic)

print("합계:",a,",","평균:","{:.2f}".format(b))

