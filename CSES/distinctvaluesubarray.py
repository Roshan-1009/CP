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
    i=0
    j=0
    idx={}
    idx[numbers[0]]=0
    #formula used
    while i<=j and j<n-1:
        j+=1
        if numbers[j] in idx and idx[numbers[j]]+1>=i:    
            i=idx[numbers[j]]+1
        idx[numbers[j]]=j
        count+= j-i+1
    print(count)       

    #no of arrays in a limit of i,j of sliding window is j-i+1

    

    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING