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

class Summary(object):
    def __init__(self):
        self.array = []

    def assign(self,x):
        self.array = x

    def output(self):
        return self.array

class Question(object):
    
    def __init__(self):
        self.number   = 0
        self.problem  = ''
        self.proposed = 0
        self.solution = 0
        self.result   = ''
        self.time     = 0

    def assign(self, number, problem, proposed, solution, time):
        self.number   = number
        self.problem  = problem
        self.proposed = proposed
        self.solution = solution
        self.time     = time

    def assign_result(self, result):
        self.result = result

    def output(self):
        return [self.number, self.problem, self.proposed, self.solution, self.result, self.time]

class MMGame(object):

    def __init__(self,amin,amax,bmin,bmax):
        self.time   = 0
        self.qcount = 1

        self.amin   = amin
        self.amax   = amax
        self.bmin   = bmin
        self.bmax   = bmax

        self.rlist  = []

    def game(self):
        while True:
            q   = Question()

            a   = random.randint(self.amin, self.amax)
            b   = random.randint(self.bmin, self.bmax)

            number   = '\n(' + str(self.qcount) + ') '
            problem  = str(a) + ' x ' + str(b)
            answer   = '\nAnswer: '
            prompt   = number + problem + answer

            start = timer()

            ans   = input(prompt)

            end   = timer()
            self.time += end - start

            if ans.isdigit():
                if int(ans) == (a*b):
                    print('\nCorrect! :D')
                    q.assign_result('correct')
                else:
                    cor = str(a*b)
                    print('\nIncorrect :(\nThe correct answer is:', cor)
                    q.assign_result('INCORRECT')
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

            q.assign(self.qcount, problem, int(ans), a*b, end-start)
            out = q.output()
            self.rlist.append(out)

            self.qcount += 1

    def output(self):
        return self.rlist
       
def main():    
    g = MMGame(10,99,10,99)
    g.game()
    
    s = Summary()
    s.assign(g.output())
    
    out = s.output()
    table = tabulate(out, headers=['Question Number', 'Problem', 'Your Answer', 'Correct Answer', 'Result', 'Time Taken'])
    print(table)

if __name__ == "__main__":
    main()
