#!/usr/bin/python3.5
#coding: utf-8
Author = 'lc4t'


import base64


def concatListSeq(seq):
    ans = []
    def BFS(seq, ack = '', start = 0):
        if (start == len(seq)):
            if (start == 0):
                return
            ans.append(ack)
            return
        for i in seq[start]:
            BFS(seq, ack + i, start + 1)

    BFS(seq)
    return (ans)  

def checkAcceptableCharacter(ans, function, ENCODING = 'utf-8'):
    AcceptableList = [9, 10, 13]
    if (ENCODING == 'utf-8'):
            for i in ans:
                # print (i)
                if ((ord(i) in AcceptableList) == False and (32 <= ord(i) <= 126) == False):
                    raise ValueError('Not Acceptable Character in ' + function + ':' + i)
                    return False
    return True

def Base16Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = []
    try:
        ansSeq = base64.b16decode(guessString).decode(ENCODING)
        if (not checkAcceptableCharacter(ans, 'Base16Decode', ENCODING = 'utf-8')):
            return ans
        ans.append(ansSeq)
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base16Decode-----')
            print (e)
            print ('-------------------------<<<<<<')
        else:
            pass
        return ans
    return ans

def Base32Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = []
    try:
        ansSeq = base64.b32decode(guessString).decode(ENCODING)
        if (not checkAcceptableCharacter(ans, 'Base32Decode', ENCODING = 'utf-8')):
            return ans
        ans.append(ansSeq)
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base32Decode-----')
            print (e)
            print ('-------------------------<<<<<<')
        else:
            pass
    return ans

def Base64Decode(guessString, DEBUG = False, ENCODING = 'utf-8'):
    ans = []
    try:
        ansSeq = base64.b64decode(guessString).decode(ENCODING)
        if (not checkAcceptableCharacter(ans, 'Base64Decode', ENCODING = 'utf-8')):
            return ans
        ans.append(ansSeq)
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base64Decode-----')
            print (e)
            print ('-------------------------<<<<<<')
        else:
            pass
    return ans


# This is auto upper and lower case in base64 decode.
##START


def Base64DecodeWithoutCaps(guessString, DEBUG = False, ENCODING = 'utf-8'):
    if (guessString.lower() != guessString and guessString.upper() != guessString):
        return []
    def Base64DecodeWithoutCapsGetAnsSeq(seq, ENCODING = 'utf-8'):
        ansList = []
        for a in [seq[0].lower(), seq[0].upper()]:
            for b in [seq[1].lower(), seq[1].upper()]:
                for c in [seq[2].lower(), seq[2].upper()]:
                    for d in [seq[3].lower(), seq[3].upper()]:
                        string = a + b + c + d
                        try:
                            ansSeq = base64.b64decode(string).decode(ENCODING)
                            # print (string,ansSeq)
                            if (checkAcceptableCharacter(ansSeq, 'Base64DecodeWithoutCapsGetAnsSeq', ENCODING = 'utf-8')):
                                ansList.append(ansSeq)
                        except Exception as e:
                            pass
        return list(set(ansList))

    ans = []
    try:
        for seqID in range(0, len(guessString), 4):
            seq = guessString[seqID:seqID + 4]
            ansseq = Base64DecodeWithoutCapsGetAnsSeq(seq, ENCODING)
            
            # cnt = len(ansseq)
            if (len(ansseq) == 0):
                raise ValueError('None @', seq)
                return ans
            else:
                ans.append(ansseq)
        return concatListSeq(ans)
    except Exception as e:
        if (DEBUG):
            print ('-----Error in Base64DecodeWithoutCaps-----')
            print (e)
            print ('-------------------------<<<<<<<<<<<<<<<<<')
        else:
            pass
        return []
    return []
###END

