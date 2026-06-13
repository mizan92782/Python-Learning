
name = ["Mizan","sizaan", " asif ", "  Akash", "BATAS" , " NODI","NALa"] 



res = list(map(str.title,name))
print(res)
print('\n')
res = list(map(str.strip,name))
print(res)

res = list(map(lambda x: x.find('za'),name))
print(res)


res = list(map(lambda x: x.split('a'),name))
print(res)





res = list(map(lambda x: x.count('a'),name))
print(res)




print(name)


res = list(map(lambda x: x.join('-'),name))
print(res)





name = ["Mizan", "Sizan", "Asif"]

res = "-".join(name)
print(res)




