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


class MMGame(object):

    def __init__(self,amin,amax,bmin,bmax):
        self.time = 0
        self.qcount = 1

        self.amin = amin
        self.amax = amax
        self.bmin = bmin
        self.bmax = bmax

        self.summary = []

    def game(self):
        while True:
            l = []

            a = random.randint(self.amin, self.amax)
            b = random.randint(self.bmin, self.bmax)

            number = '\n(' + str(self.qcount) + ') '
            problem = str(a) + ' x ' + str(b)
            answer = '\nAnswer: '
            prompt = number + problem + answer

            start = timer()

            ans = input(prompt)

            end = timer()
            self.time += end - start

            if ans.isdigit():
                if int(ans) == (a*b):
                    print('\nCorrect! :D')
                    l.append('correct')
                else:
                    cor = str(a*b)
                    print('\nIncorrect :(\nThe correct answer is:', cor)
                    l.append('INCORRECT')
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

            l += [self.qcount, problem, int(ans), a*b, end-start]
            self.rlist.append(l)
            self.qcount += 1

    def output(self):
        return self.rlist


def main():    
    g = MMGame(10,99,10,99)
    g.game()
    
    table = tabulate(g.output(), headers=['Result', 'Question Number', 'Problem', 'Your Answer', 'Correct Answer', 'Time Taken'])
    print(table)


if __name__ == "__main__":
    main()
