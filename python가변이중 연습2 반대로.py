a=input("하트가 몇 줄 나오길원해?")
for i in range(int(a),0,-1):
    print()
    for j in range(1,i+1):
        print("♥",end="")
