#!/usr/bin/env python3
#
# Name: Warren Mo
#
# mm.py
# Mental Math Games! (Based loosely on the types of problems posed in Secrets of Mental Math by Arthur Benjamin and Michael Shermer

import sys
import random
from timeit import default_timer as timer

def main():

    tt = 0

    while 1:

        a = random.randint(10,99)
        b = random.randint(10,99)

        out = str(a) + ' x ' + str(b) + '\n'

        start = timer()

        ans = input( out )

        if int(ans) == (a * b):
            print('\nCorrect! :D\n')
        else:
            cor = str(a * b)
            print('\nIncorrect :(\nThe correct answer is:', cor, '\n')
        
        end = timer()
        
        tt += end - start
        
        wait = input( 'Continue or quit? (c or q)\n' )

        if wait == 'q':
            print('Goodbye!\n')
            break
        elif wait == 'c':
            print('Cool! Moving on!\n')
        else:
            print('Sorry, I do not know what that means.')

    print(tt)

if __name__ == "__main__":
    main()
