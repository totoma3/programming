def v_t(a1,a2,a3):
    return int(a1)*int(a2)*int(a3)

a=input("가로값")
b=input("세로값")
c=input("높이값")
test=v_t(a,b,c)
print("직육면체 부피는 %d세제곱센티미터"%test)
