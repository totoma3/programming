t=int(input())
for i in range(t):
    R,s=input().split()
    R=int(R)
    s=str(s)
    for i in range(len(s)):
        print(R*s[i],end='')
    print()
