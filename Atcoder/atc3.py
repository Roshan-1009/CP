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
    numbers=list(map(int,input_data[1:2*n+1]))
    q=int(input_data[2*n+1])
    for i in range(q):
        list1=[]
        k=int(input_data[2*n+2+i])+0.5
        count=0
        maximum=0
        for j in range(1,2*n,2):
            if numbers[j]>k:
                if maximum<numbers[j-1]:
                    maximum=numbers[j-1]
            else:
                break
        print(maximum)    
                


        

    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING