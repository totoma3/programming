import random
import time
play=["종이접기","우크렐레 배우기","샌드아트","풍선아트","오카리나"]
print(play)
print("여러분에게 추천할 놀이는? 1초 후에 알려줄께요")
time.sleep(1)
print("바로바로",random.choice(play))
random.shuffle(play)
print(play)
