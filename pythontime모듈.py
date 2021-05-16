import time
t1=time.time()
time.sleep(3)
t2=time.time()
waittime=t2-t1
print("프로그램 초기시간",t1)
print("프로그램 실행 후 시간",t2)
print("동작정지시간 %3.2f 초"%(waittime))
