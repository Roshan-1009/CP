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
    n = int(input_data[0])
    numbers=list(map(int,input_data[1:]))
    count=1
    myset=set()
    for i in numbers:
        if i+1 in myset:
            count+=1
        myset.add(i)
    print(count)            


    

    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING