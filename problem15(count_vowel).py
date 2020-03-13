# This is python program to count the number of vowels in given string.

import re          # regular expression module.

def count_vowel(string):
    vowel_regex = re.compile(r"[aeiouAEIOU]")

    vowel_list = vowel_regex.findall(string)

    return len(vowel_list) 

sentence = "I love my India"      # input sentence.

output = count_vowel(sentence)

print("sentence: I love India")
print("number of vowel:",output)