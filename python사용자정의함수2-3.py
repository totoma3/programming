def calc_pro(optr,a1,a2):
    if int(optr)==1:
        return int(a1)+int(a2)
    elif int(optr)==2:
        return int(a1)-int(a2)
    elif int(optr)==3:
        return int(a1)*int(a2)
    elif int(optr)==4:
        return int(a1)/int(a2)
    else:
        return "연산이 성립하지 않아요"

#메인프로그램부분
v1=input("처음값")
v2=input("다음값")
print("연산기호선택 1.덧셈(+),2.뺄셈(-),3.곱셈(*),4.나누기(/)")
a=input("메뉴에서 번호를 선택하세요")
result=calc_pro(a,v1,v2)
#print("계산결과=%d"%(result))
print("계산결과=%f"%(result))
