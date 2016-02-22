#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'
DEBUG = False

import sys
import base64

class Decode:


    def __init__(self, guessString):
        self.guessString = guessString
        self.method = ['base16', 'base32', 'base64']
        self.method.sort()
        self.echo()

    def base16(self):
        ans = ''
        try:
            ans = base64.b16decode(self.guessString).decode()
        except Exception as e:
            if (DEBUG):
                print ('-----Error in base16-----')
                print (e)
                print ('-------------------------')
            else:
                pass
        return ans



    def base32(self):
        ans = ''
        try:
            ans = base64.b32decode(self.guessString).decode()
        except Exception as e:
            if (DEBUG):
                print ('-----Error in base32-----')
                print (e)
                print ('-------------------------')
            else:
                pass
        return ans

    def base64(self):
        ans = ''
        try:
            ans = base64.b64decode(self.guessString).decode()
        except Exception as e:
            if (DEBUG):
                print ('-----Error in base32-----')
                print (e)
                print ('-------------------------')
            else:
                pass
        return ans


    def echo(self):
        total = 0
        for seq in range(0, len(self.method), 1):
                answer = eval('self.' + self.method[seq])()
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