import re
l = re.match('abc', 'abcdef')
print(l)
word_regex = '\w+'
l = re.match(word_regex, 'ritika motwani')
print(l)
t = re.split('\s+', 'Split on spaces')
print(t)

