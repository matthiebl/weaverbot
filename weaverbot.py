#!/usr/bin/python3

import sys
from words4dict import wordDict

def computeMinDistance(word, end):
    dist = 0
    for l1, l2 in zip(word, end):
        if l1 != l2:
            dist += 1
    return dist

def solve(word, end, lst, collection, length=7):
    if word == end:
        collection.append(lst)
        return
    
    if len(lst) + computeMinDistance(word, end) > length:
        return

    for poss in wordDict[word]:
        if poss not in lst:
            newLst = lst.copy()
            newLst.append(poss)
            solve(poss, end, newLst, collection, length)

def main():
    leng = 7
    if len(sys.argv) >= 2:
        leng = int(sys.argv[1])

    start = input()
    end = input()
    if start not in wordDict:
        print(f'{start} is not in the dictionary')
    elif end not in wordDict:
        print(f'{end} is not in the dictionary')
    else:
        print(f'\nStarting...')
        every = []
        solve(start, end, [], every, length=leng)

        if len(every) > 0:
            print(f'\nHere are all the answers length {leng} or less:')
            for e in sorted(every, key=len, reverse=True):
                print(e)
            
            print(f'\nOne of the best answers is: {" -> ".join(every[-1])}')
        else:
            print(f'\nThere are no solutions of length {leng} or less')
main()
