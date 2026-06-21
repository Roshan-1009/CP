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
    target = int(input_data[1])
    coins=list(map(int,input_data[2:]))
    dp=[10**9]*(target+1)
    dp[0]=0   
    coins.sort()
    for i in range(1,target+1):
        for coin in coins:
            if i-coin>=0:
                if dp[i]>dp[i-coin]+1:
                    mini=dp[i-coin]+1
                else:
                    mini=dp[i]  
                dp[i]=mini
            else:
                break    
                
    if dp[target]==10**9:
        print(-1)
    else:    
        print(dp[target])            
    

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING