#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'
DEBUG = True
ENCODING = 'utf-8'

import sys
from functions import * 


class Decode:
    def __init__(self, guessString):
        self.guessString = guessString
        self.method = ['Base16Decode', 'Base32Decode', 'Base64Decode']
        self.method.sort()
        self.total = 0
        # self.echo()

    def count(self):
        print ('all answer:', self.total)

    def echo(self):
        self.total = 0
        for seq in range(0, len(self.method), 1):
                answer = eval(self.method[seq])(self.guessString, DEBUG)
                if (len(answer) == 0):
                    continue
                else:
                    print (self.method[seq] + '->' + answer)
                self.total += 1
        self.count()

    def DFS(self, string, encryption = ''):
        if (len(string) == 0):
            return
        for one in range(0, len(self.method), 1):
            answer = eval(self.method[one])(string, DEBUG, ENCODING)
            
            if (len(answer) > 0):
                self.total += 1
                encryption = encryption + self.method[one] + ' -> '
                print (encryption + answer)
                self.DFS(answer, encryption)
            else:
                continue
        


def main():
    if (len(sys.argv) < 2):
        usage = '''
    Usage:
            python3 decoder.py stringYouWantToDecode
        '''
        print (usage)
        exit(0)
    guessString = sys.argv[1]

    Decode(guessString).DFS(guessString)



if __name__ == '__main__':
    main()