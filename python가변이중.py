a=input("하트가 몇 줄 나오길 원해?")
b=input("한줄에 몇개의 하트를 표시해줄까?")
for i in range(1,int(a)+1):
    print()  
    for j in range(1,int(b)+1):
        print("♥",end="")
