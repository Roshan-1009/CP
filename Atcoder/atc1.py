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
    numbers=list(map(int,input_data[0:]))
    hcf=math.gcd(numbers[0],numbers[1])
    a=numbers[0]//hcf
    b=numbers[1]//hcf
    if a==16 and b==9:
        print("Yes")
    else:    
        print("No")




    

    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING