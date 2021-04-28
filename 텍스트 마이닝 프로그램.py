from collections import Counter
import re
#python파일 읽어오기

f=open("python.txt","r")
contents=f.read()
a=contents.lower()
#공백을 기준으로 단어들을 나누기
words = a.split(" ")

pure_word = []
#for문으로 문장의 마침표,쉼표,소괄호를 삭제, 모두 소문자로 변환
for i in range(0, len(words)):
         clean_text = words[i].replace('\n', '')       
         if len(clean_text) > 1:
             pure_word.append(re.sub('[\,\.,()]', '', clean_text))

#Collections의 Counter함수를 사용하여 딕셔너리 형태로 저장
words_dic=Counter(pure_word)


#값 부분을 따로 뽑아 저장하기
values=words_dic.values()
print("* 전체 단어의 개수:",sum(values))
#collections의 Counter함수를 사용
print("* 'python'단어의 개수:",words_dic["python"])
index=1
count=0
#앞서 만든 리스트에서 10자 이상인 단어수를 세기
for k in pure_word:
    if len(k)>=10:         
        print("%d:"%index,k)
        index +=1
        count +=1
print("* 10자 이상인 단어 수:",count)
