

# a{n,m} : a can be appear n to m times


import re


text = "a aa aaa aaaa"
print(re.findall(r"a{2,3}", text))