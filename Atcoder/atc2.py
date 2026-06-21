import math
import sys
import os
from bisect import bisect_right
# 1. The Local Environment Check

# This automatically routes files if you are coding locally,

# but ignores them when submitted to the online judge.

if os.path.exists('input.txt'):

    sys.stdin = open('input.txt', 'r')

    sys.stdout = open('output.txt', 'w')

import random
from collections import defaultdict

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n=int(input_data[0])
    character=(input_data[1])
    seats=input_data[2:]
    total=5*n
    mymap={}
    mymap['A']=1
    mymap['B']=2
    mymap['C']=3
    mymap['D']=4
    mymap['E']=5
    k=mymap[character]
    for i in range(n):
        if seats[i][k-1]=='o':
            print("Yes")
            return
    print("No")








    

    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING