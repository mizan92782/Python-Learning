

# a? : a can exist or unexist
#here ucan exist

import re

text = "color colour"
print(re.findall(r"colou?r", text))
