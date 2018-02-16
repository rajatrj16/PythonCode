import re

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_pharse = 'sdsd..sssddd..sdddsddd...dsds...sdddd...dssss'
test_pattern1 = ['sd*']
test_pattern2 = ['sd']
test_pattern3 = ['sd+']
test_pattern4 = ['sd?']
test_pattern5 = ['sd+?']
test_pattern6 = ['sd{3}']
test_pattern7 = ['sd{1,3}']
test_pattern8 = ['s[sd]+']

multi_re_find(test_pattern1,test_pharse)
multi_re_find(test_pattern2,test_pharse)
multi_re_find(test_pattern3,test_pharse)
multi_re_find(test_pattern4,test_pharse)
multi_re_find(test_pattern5,test_pharse)
multi_re_find(test_pattern6,test_pharse)
multi_re_find(test_pattern7,test_pharse)
multi_re_find(test_pattern8,test_pharse)

test_pharse = 'This is a string! But is has a punctuation. And how can we remove it? and $symbols# like 1 and 2'
test_patterns1 = ['[ ^!.?]+']
test_patterns2 = ['[^!.?]+']
test_patterns3 = ['[a-z]']
test_patterns4 = ['[A-Z]']
test_patterns5 = ['[A-Z]+']
test_patterns6 = [r'\d+'] #digit
test_patterns7 = [r'\D+'] #non digit
test_patterns8 = [r'\s+'] #non white space
test_patterns9 = [r'\S+'] #white space
test_patterns10 = [r'\w+'] #alphanumeric
test_patterns11 = [r'\W+'] # non alphanumeric
multi_re_find(test_patterns1,test_pharse)
multi_re_find(test_patterns2,test_pharse)
multi_re_find(test_patterns3,test_pharse)
multi_re_find(test_patterns4,test_pharse)
multi_re_find(test_patterns5,test_pharse)
multi_re_find(test_patterns6,test_pharse)
multi_re_find(test_patterns7,test_pharse)
multi_re_find(test_patterns8,test_pharse)
multi_re_find(test_patterns9,test_pharse)
multi_re_find(test_patterns10,test_pharse)
multi_re_find(test_patterns11,test_pharse)
