# This is python program to remove the punctuation from given string and produce output string.

def remove_punctuation(string):
    punct = '''!()-[]{}:;'"\/,.<>?@#$%^&*_~`|'''   # punctuation string.
    for x in string:
        if x in punct:
            string = string.replace(x,"")       
        else:
            pass
    return string

sentence = "Welcome ????@@##$%^Geeks &*() for__-{}[]Geeks.;':"  # given sentence.

new_sentence = remove_punctuation(sentence)

print("sentence:",sentence)
print("new sentence:",new_sentence)