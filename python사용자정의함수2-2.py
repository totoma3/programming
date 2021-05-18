#함수프로그램부분
def calc_fun(a):
    ratio=0.9
    return (a-100)*ratio


#메인프로그램부분
h=input("당신의 키를 입력하세요")
height=int(h)
result=calc_fun(height)
print("사용자님의 표준 체중은",result,"Kg입니다.")
