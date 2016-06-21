#!/usr/bin/env python3
#
# Name: Warren Mo
#
# mm.py
# Mental Math Games! (Based loosely on the types of problems posed in Secrets of Mental Math by Arthur Benjamin and Michael Shermer

import sys
import random
from timeit import default_timer as timer

class MMGame(object):

    def __init__(self,amin,amax,bmin,bmax):
        self.time = 0

        self.amin = amin
        self.amax = amax
        self.bmin = bmin
        self.bmax = bmax

    def question(self):
        while 1:
            a   = random.randint(self.amin, self.amax)
            b   = random.randint(self.bmin, self.bmax)
            out = str(a) + ' x ' + str(b) + '\n'

            start = timer()

            ans = input( out )

            if int(ans) == (a * b):
                print('\nCorrect! :D\n')
            else:
                cor = str(a * b)
                print('\nIncorrect :(\nThe correct answer is:', cor, '\n')
            
            end = timer()
            
            self.time += end - start

            wait = input( 'Continue or quit? (c or q)\n' )

            if wait == 'q':
                print('Goodbye!\n')
                break
            elif wait == 'c':
                print('Cool! Moving on!\n')
            else:
                print('Sorry, I don\'t know what that means.')

        print(self.time)
       
def main():    
        
    game = MMGame(10,99,10,99)
    game.question()

if __name__ == "__main__":
    main()
