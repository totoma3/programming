a=input("첫번째 입력값")
b=input("두번째 입력값")
if int(a)>int(b):
    print(a,"가",int(a)-int(b),"만큼 큽니다.")
elif int(a)<int(b):
    print(b,"가",int(b)-int(a),"만큼 큽니다.")
else:
    print("값이 같습니다.")
