# Maintainer: RobotAstray
# Copyright (c) RobotAstray
# Usage: python3 is_palindrome.py --phrase "enter your string here"

import argparse
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-phrase", action="store",dest="phrase", type=str, help="enter a phrase" )
    output = parser.parse_args()
    s = output.phrase
    # strip all the spaces and punctuation
    s = s.replace(' ','')
    print(s)
    table = str.maketrans(dict.fromkeys(string.punctuation))
    print(s)
    s = s.translate(table) 
    s = s.lower()
    print(is_palindrome(s))



def is_palindrome(s: str) -> bool:
     if s[0] == s[len(s)-1]:
        s= s[1:-1]
        if len(s) <=1:
           return True
        else:
            return is_palindrome(s)
     else:
         return  False


        
if __name__ == "__main__":
    main()

