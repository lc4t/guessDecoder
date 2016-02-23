#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'


# def okChar(t):


#     if t in [9, 10, 13]:
#         return True

#     if (32 <= i <= 126):
#         return True

#     return False

import base64

def checkAcceptableCharacter(ans, function, ENCODING = 'utf-8'):
    AcceptableList = [9, 10, 13]
    if (ENCODING == 'utf-8'):
            for i in ans:
                if ((ord(i) not in AcceptableList) or not (32 <= i <= 126)):
                    raise ValueError('Error in ' + function + ':' + i)
                    return False


def Base16Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = ''
    try:
        ans = base64.b16decode(guessString).decode(ENCODING)
        checkAcceptableCharacter(ans, 'Base16Decode', ENCODING = 'utf-8')
        # if (ENCODING == 'utf-8'):
        #     for i in ans:
        #         if (not okChar(ord(i))):
        #             raise ValueError('Error in Base16Decode:'+i)
        #             return ''
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base16Decode-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans



def Base32Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = ''
    try:
        ans = base64.b32decode(guessString).decode(ENCODING)
        # if (ENCODING == 'utf-8'):
        #     for i in ans:
        #         if (not okChar(ord(i))):
        #             raise ValueError('Error in Base32Decode:'+i)
        #             return ''
        checkAcceptableCharacter(ans, 'Base32Decode', ENCODING = 'utf-8')
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base32Decode-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans

def Base64Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = ''
    try:
        ans = base64.b64decode(guessString).decode(ENCODING)
        # if (ENCODING == 'utf-8'):
        #     for i in ans:
        #         if (not okChar(ord(i))):
        #             raise ValueError('Error in Base64Decode:'+i)
        #             return ''
        checkAcceptableCharacter(ans, 'Base64Decode', ENCODING = 'utf-8')
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base64Decode-----')
            print (e)
            print ('-------------------------')
        else:
            pass
    return ans