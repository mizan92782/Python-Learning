
import re

text = "I love bangladesh,bangladesh is a south asian country"


result= re.search('bangladesh',text)

print(result.group())