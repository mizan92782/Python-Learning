#  '^' userd for start string

import re

text ="lick kick sick bisk nickels bakles licles"
res = re.findall(r"^\bli\w*",text)
print(res)