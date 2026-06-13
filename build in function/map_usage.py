#========= usage =====
name =[ 'mizan','sizan','banane','apple'
]



#make all upper
res = list(map(str.upper,name))
print(res)




#=========== extractin workd
res = list(map(lambda x : x[0],name))
print(res)


res = list(map(lambda x : x[0:3],name))
print(res)







# removein white space
s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))






#========= calculating
s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))

