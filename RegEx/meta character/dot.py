

# যেকোনো একটিমাত্র character match করবে (newline ছাড়া)
#খানে . যেকোনো 1 character replace করছে


import re

text = 'cat cit cet c@t'

# find a wrod that start witl s and t and a word in between them
res1= re.findall(r'c.t',text)
print(res1)

#find wot that middle word in 'i'

res2 = re.findall(f".i.",text)
print(res2)
