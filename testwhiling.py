total=0
while 1:
    a=input("값을 입력하세요")
    if int(a)==0:
        break
    total+=int(a)
print("누적값:",total)
