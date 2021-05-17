save_money=5000
def calc_money():
    global save_money
    in_money=2000
    rate=0.03
    save_money=save_money+in_money
    return save_money*rate

print("당신의 이전예금액 %d"%(save_money))
result=calc_money()
print("당신의 예금액 %d"%(save_money))
print("이자=%d"%(result))
