#!/usr/bin/env python3
#
# Name: Warren Mo
#
# mm.py
# Mental Math Games! (Based loosely on the types of problems posed in Secrets of Mental Math by Arthur Benjamin and Michael Shermer)

import sys
from random import randint
from timeit import default_timer as timer
from tabulate import tabulate
import operator
from abc import ABCMeta, abstractmethod


class MMGame(metaclass=ABCMeta):

    opchar = ''

    def __init__(self, amin, amax, bmin, bmax):
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

            a = randint(self.amin, self.amax)
            b = randint(self.bmin, self.bmax)

            number = '\n(' + str(self.qcount) + ') '
            problem = str(a) + ' ' + self.opchar + ' ' + str(b)
            answer = '\nAnswer: '
            prompt = number + problem + answer

            start = timer()

            ans = input(prompt)

            end = timer()
            self.time += end - start

            cor = ch_to_op(self.opchar, a, b)

            if ans.isdigit():
                if int(ans) == cor:
                    print('\nCorrect! :D')
                    l.append('correct')
                else:
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
                        continue
                else:
                    print('Sorry, I don\'t know what that means.')
                    continue

            l += [self.qcount, problem, int(ans), cor, end-start]
            self.summary.append(l)
            self.qcount += 1

    def output(self):
        return self.summary

    @abstractmethod
    def game_type():
        pass


class AddGame(MMGame):

    opchar = '+'

    def game_type(self):
        return 'You\'ve chosen: Addtion!'


class SubGame(MMGame):

    opchar = '-'

    def game_type(self):
        return 'You\'ve chosen: Subtraction!'


class MulGame(MMGame):

    opchar = 'x'

    def game_type():
        return 'You\'ve chosen: Multiplication!'


def ch_to_op(c, x, y):

    if c == '+':
        return operator.add(x, y)
    elif c == '-':
        return operator.sub(x, y)
    elif c == 'x':
        return operator.mul(x, y)


def menu(g):

    print('\n Welcome to the mental math game!\nSelect a game mode:\n')

    return g.game_type()
    return g.game()


def main():
    
    g = MulGame(2,9,11,99)
    g.game()
    
    table = tabulate(g.output(), headers=['Result', 'Question Number', 'Problem', 'Your Answer', 'Correct Answer', 'Time Taken'])
    print(table)

    cornum = 0
    incnum = 0
    time   = 0
    num    = 0
    for i in g.output():
        if i[0] == 'correct':
            cornum += 1
        else:
            incnum += 1
        time += i[5]
        num  += 1
    acc = cornum / (cornum + incnum) * 100
    tim = time / num
    print ('Accuracy: ', acc,'%\t','Avg. Time per Question: ', tim)     


if __name__ == "__main__":
    main()
