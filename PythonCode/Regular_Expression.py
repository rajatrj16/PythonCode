import re

#text = 'This is string with term1 but not with term2'
split_term = '@'
email = 'rajatrj16@gmail.com'
print(re.split(split_term,email))
# match = re.search('term1',text)
# print(match.start())
# if match == 'term1':
#     print('Yuhu Match!')
# else:
#     print('no match')
print("\nThis is another********************************************************")
import re

patterns = ['term1', 'term2']

text = 'This is string with term1 but not with term2'

for pattern in patterns:
    print('I am searching for: '+pattern)

    if re.search(pattern,text):
        print('Yuhu Match!')
    else:
        print('Uh oH no Match!')

print("\nThis is another********************************************************")


import re
print(re.findall('match','test phrase match in the match middle'))
