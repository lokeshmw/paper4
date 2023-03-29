import re

input_ = input("enter a gmail_id: ")
pattern = "\W"
a = re.sub(pattern, " ", input_)
print(a)
