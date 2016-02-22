#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'

import base64
def Base16(guessString, DEBUG = False):
    ans = ''
    try:
        ans = base64.b16decode(guessString).decode()
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base16-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans



def Base32(guessString, DEBUG = False):
    ans = ''
    try:
        ans = base64.b32decode(guessString).decode()
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base32-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans

def Base64(guessString, DEBUG = False):
    ans = ''
    try:
        ans = base64.b64decode(guessString).decode()
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base64-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans