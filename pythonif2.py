p=input("포인트를 입력하세요")
part=input("지점을 입력하세요.")
if int(p)>=1000 and part=="강동":
    print("최우수고객 입니다.")
elif int(p)>=500 and part=="강동":
    print("우수고객 입니다.")
else:
    print("일반 고객입니다.")
    
