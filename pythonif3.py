a=input("첫번째 값을 입력하세요")
b=input("두번째 값을 입력하세요")
if int(a)>int(b):
    print("큰 값",int(a),"는",int(a)-int(b),"만큼 더 큽니다.")
elif int(a)<int(b):
    print("큰 값",int(b),"는",int(b)-int(a),"만큼 더 큽니다.")
else:
    print("두 값은 같습니다.")
    
