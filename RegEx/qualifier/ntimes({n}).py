# a{n} : a appear al leart n times
import re
text = "aaaa aa a"
print(re.findall(r"a{3}", text))