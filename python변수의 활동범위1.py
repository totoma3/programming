def dep_money(m):
    pay=[5000,1000,500,100,50,10]
    for i in pay:
        a=m/i
        m=m%i
        print(i,"원 짜리 %d"%(a))
    print("최종 m 값=%d"%(m))
    
money=input("금액을 입력하세요")
m=int(money)
print("금액 분류결과")
dep_money(m)
