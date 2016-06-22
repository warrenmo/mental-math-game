#!/usr/bin/env python3
#
# Name: Warren Mo
#
# mm.py
# Mental Math Games! (Based loosely on the types of problems posed in Secrets of Mental Math by Arthur Benjamin and Michael Shermer)

import sys
import random
from timeit import default_timer as timer
from tabulate import tabulate

class Results(object):
    def __init__(self):
        self.array = []

    def append(self,x):
        self.array += x

    def printR(self):
        table = tabulate(self.array, headers=['Question Number', 'Prompt', 'Your Answer', 'Correct Answer', 'Time Taken'])
        print(table)

class Question(object):
    
    def __init__(self, number, prompt, correct, proposed, solution, time):
        self.number   = number
        self.prompt   = prompt
        self.proposed = proposed
        self.solution = solution
        self.correct  = (self.proposed == self.solution)
        self.time     = time

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

            number   = '\n(' + str(self.qcount) + ') '
            problem  = str(a) + ' x ' + str(b) + '\nAnswer: '
            prompt   = number + problem

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

        print('Total time: ', self.time)
       
def main():    
        
    #g = MMGame(10,99,10,99)
    #g.game()
    ex = Question(1, '30 x 15', True, 450, 450, 1.2)
    ex.printQ()

if __name__ == "__main__":
    main()
