import time
t1=time.localtime()
#for i in t1:
#    print(i)
#print("현재년도",t1[0])    
#print("현재 월",t1[1])
y=t1[0]
m=t1[1]
print(y,"년",m,"월")
print("%d년"%(y),"%d월"%(m))
