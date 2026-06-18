

# a* : a can be 0 or unlimited times

#empty string আসবে (important behavior)


import re 

text ="aaabaaaaa aba aa"

res = re.findall(r'a*',text)
print(res)


