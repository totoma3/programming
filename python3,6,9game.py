import time
import winsound
for i in range(1,11):
    if i==3 or i==6 or i==9:
        winsound.Beep(600,250)
        time.sleep(2)
        continue
    print(i)
    


