age=input("당신의 나이를 입력하세요")
if int(age)>=65:
    print("경로우대 대상입니다.")
else:
    print("경로우대 대상이 아닙니다.")
    print("65세가 되려면 앞으로",65-int(age),"년 남았습니다.")
    
