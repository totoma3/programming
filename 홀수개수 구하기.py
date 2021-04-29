#1. 입력받은 숫자 나누기
count=0
num=int(input("숫자를 입력하세요:"))
a=[]
for i in str(num):
    a.append(i)
a=list(map(int,a))
#2. 리스트에 들어간 숫자에서 홀수 찾기
   
for j in a:
        if j%2==1:
            count+=1
        else:
            count+=0
print("홀수의 개수:",count,"개")
