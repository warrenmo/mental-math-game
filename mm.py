#!/usr/bin/env python3
#
# Name: Warren Mo
#
# mm.py
# Mental Math Games! (Based loosely on the types of problems posed in Secrets of Mental Math by Arthur Benjamin and Michael Shermer)

import sys
import random
from timeit import default_timer as timer

class MMGame(object):

    def __init__(self,amin,amax,bmin,bmax):
        self.time   = 0
        self.qcount = 1

        self.amin   = amin
        self.amax   = amax
        self.bmin   = bmin
        self.bmax   = bmax

    def game(self):
        while True:
            a   = random.randint(self.amin, self.amax)
            b   = random.randint(self.bmin, self.bmax)

            qnum  = '\n(' + str(self.qcount) + ') '
            ques  = str(a) + ' x ' + str(b) + '\nAnswer: '
            prompt = qnum + ques

            start = timer()

            ans   = input( prompt )

            end   = timer()
            self.time += end - start

            if ans.isdigit():
                if int(ans) == (a * b):
                    print('\nCorrect! :D')
                else:
                    cor = str(a * b)
                    print('\nIncorrect :(\nThe correct answer is:', cor)
            else:
                if ans == 'q':
                    wait = input( '\nWould you like to quit? (y or n): ' )
                    if wait == 'y':
                        print('Goodbye!\n')
                        break
                    elif wait == 'n':
                        print('Cool! Moving on!')
                    else:
                        print('Sorry, I don\'t know what that means.')

            self.qcount += 1

        print(self.time)
       
def main():    
        
    game = MMGame(10,99,10,99)
    game.game()

if __name__ == "__main__":
    main()
