# This is python program to produce the list ['a','b','c',......,'z'], but without having to type all 26 such character literals.

charater_list = [chr(n) for n in range(97,123)]    # by using the chr(ascii value) function.

print("character list:",charater_list)