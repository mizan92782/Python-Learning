


""" Rule : Character class মানে: “এই list-এর যেকোনো একটা character match কর”"""

import re

text ="apple banaan cat dog"
res = re.findall(f"[ac]",text)

print(res)





#! match word a to z :
text = "A1b2C3d4"
print(re.findall(r"[a-z]", text))