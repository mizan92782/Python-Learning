import re
'''
Rule:

একসাথে group করে treat করা
'''

text ='ababa abc ab'

res  = re.findall(r"(ab)+",text)

print(res)