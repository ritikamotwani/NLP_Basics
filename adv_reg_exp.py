import re
my_str = "match lowercases spaces nums like 12, but no commas"
t = re.match('[a-z0-9 ]+', my_str)
print(t)
