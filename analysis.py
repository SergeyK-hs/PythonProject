file = open('pushkin.txt', 'r')
f = file.read()\
        .replace("\n"," ")\
        .replace("\t","")\
        .replace("\xa0\xa0\xa0\xa0","")\
        .replace(",","")\
        .replace(".","")\
        .upper().split(" ")
dict = {}
for word in f:
   if dict.get(word):    
       dict[word]+=1
   else:
       dict[word]=1
dict={k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)[:60]}
for key, value in dict.items():
    print(key, ":", value)


