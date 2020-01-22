file = open('pushkin.txt', 'r')
f = file.read().replace("\n"," ").replace("\t","").replace("\xa0\xa0\xa0\xa0","").split(" ")
dict = {}
for word in f:
    if dict.get(word) != None:
        dict[word]+=1
    else:
        dict.update([(word,1)])
print(dict)


