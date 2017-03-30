#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'
DEBUG = False
# DEBUG = True
ENCODING = 'utf-8'

import sys
from functions import *


class Decode:
    def __init__(self, guessString):
        self.guessString = guessString
        self.method = ['Base16Decode', 'Base32Decode', 'Base64Decode', 'Base64DecodeWithoutCaps', 'caser']
        # self.method = ['Base64DecodeWithoutCaps']
        self.method.sort()
        self.total = 0
        # self.echo()
        self.ans = set()

    def count(self):
        print ('all answer:', self.total)

    def echo(self):
        self.total = 0
        for seq in range(0, len(self.method), 1):
                answer = eval(self.method[seq])(self.guessString, DEBUG)
                if (len(answer) == 0):
                    continue
                else:
                    for ans in answer:
                        print (self.method[seq] + '->' + ans)
                        self.total += 1
        self.count()

    def DFS(self, string, method=None, encryption = ''):
        if method is None:
            method = self.method
        if (len(string) == 0):
            return
        # try:
        #     if 'caser' in encryption:
        #         self.method.remove('caser')
        # except ValueError:
        #     pass
        for one in range(0, len(method), 1):
            # print(one)
            func = method[one]
            answer = eval(func)(string, DEBUG, ENCODING)
            if method[one] == 'caser':
                method.remove('caser')
            if (len(answer) > 0):
                # print (answer)
                for ans in answer:
                    if (len(ans) != 0):
                        # if (type(ans) == type([1])):
                            # print(ans)
                            # print (self.method[one])
                            # exit(0)
                        # print (ans)
                        # print(self.method, one)
                        # print (self.method[one])
                        answer_one = encryption + func + ' -> ' + ans
                        # print(answer_one)
                        self.ans.add(answer_one)
                        self.total += 1

                        self.DFS(ans, method, encryption + func + ' -> ')
                    else:
                        continue
            else:
                continue

    def print_ans(self):
        for i in self.ans:
            print(i)


def main():
    if (len(sys.argv) < 2):
        usage = '''
    Usage:
            python3 decoder.py stringYouWantToDecode
        '''
        print (usage)
        exit(0)
    guessString = sys.argv[1]

    d = Decode(guessString)
    d.DFS(guessString)
    d.count()
    d.print_ans()



if __name__ == '__main__':
    main()
