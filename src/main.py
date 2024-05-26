'''
This program will translate a Roman Numeral input into a Hindu-Arabic output.
Currently it is illegal to input more than 3 of the same characters in a row
There are other contraints that have yet to be implemented
Such as the ordering of a much larger character
(E.g. LXM = 1040 in my program, but this is incorrect grammar.
    1040 should be written as MXL) 
'''

from roman_numeral_parser import parser

def main():
    flag : int = 1
    invalid : bool = True
    while flag:
        numeral = input("Give me a Roman Numeral to Translate: ")
        if numeral == "no":
            flag = 0
            continue
        a = parser(numeral)
        a.go()
        if a.valid == True:
            print(f"\nParsed input : {a.parsed_input}\nTranslation : {a.translation}\n")
        else:
            print(f"your input : {numeral}\nGive me a better input\n")
        a.reset()

main()