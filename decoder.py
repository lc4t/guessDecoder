#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'
DEBUG = True

import sys
from functions import * 


class Decode:
    def __init__(self, guessString):
        self.guessString = guessString
        self.method = ['Base16', 'Base32', 'Base64']
        self.method.sort()
        self.echo()

    def echo(self):
        total = 0
        for seq in range(0, len(self.method), 1):
                answer = eval(self.method[seq])(self.guessString, DEBUG)
                if (len(answer) == 0):
                    continue
                else:
                    print (self.method[seq] + ':' + answer)
                total += 1
        print ('all answer:', total)


def main():
    if (len(sys.argv) < 2):
        usage = '''
    Usage:
            python3 decoder.py stringYouWantToDecode
        '''
        print (usage)
        exit(0)
    guessString = sys.argv[1]
    
    Decode(guessString)



if __name__ == '__main__':
    main()