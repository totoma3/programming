def g_year(byear):
    if byear<=10:
        byear=byear+2000
    else:
        byear=byear+1900
    print("단신이 태어난 해",byear)

a=input("당신이 태어난 년도(두 자리)를 입력")
byear=int(a)
g_year(byear)
print("당신이 태어난 년도",byear)
