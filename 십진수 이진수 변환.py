a=int(input("10진수를 입력하세요:"))
b=[]

while a!=0:       #a가 0이 아닌동안에 반복한다.
    b.append(a%2) #a를 2(이진수이므로 2)로 나눈 나머지를 리스트에 넣는다.
    a=a//2        #a를 2로 나눈 몫으로 a값을 다시 정의해준다.

#리스트에 저장된 값을 뒤에서부터 출력한다.
for i in range(len(b)-1,-1,-1):  #for문을 사용하여 반복, 범위는 뒤에서부터 출력
    print(b[i],end="")           #end로 값을 이어서 출력한다.
    
