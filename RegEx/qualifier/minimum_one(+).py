import re

# a+ : a must be one

text = "a aa aaab abaa"
print(re.findall(r"a+", text))

