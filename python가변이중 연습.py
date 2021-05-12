import time
a=input("하트가 몇 줄 나오길원해?")
for i in range(1,int(a)+1):
    print()
    for j in range(1,i+1):
        time.sleep(1)
        print("♥",end="")
        
