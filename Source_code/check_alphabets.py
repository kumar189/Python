import string
#all alphabets are stored into alpha
alpha= set(string.ascii_lowercase)

in_str='The quick brown fox jumps over the lazy dog'
#string is compared with alpha and checks whether all alphabets are present or not
if(set(in_str.lower())>= alpha):
    print('True, it contains all letters in alphabet')
else:
    print("it doesn't contain all letters")
