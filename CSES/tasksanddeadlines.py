import math
import sys
import os
from bisect import bisect_right
import heapq
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
    actual=list(map(int,input_data[2:]))
    nums=actual+[0]+[n]
    nums.sort()
    myset=set()
    answer=[0]*target
    myheap=[]
    right={}
    left={}
    idx={}
    for i in range(1,len(nums)):
        difference=nums[i]-nums[i-1]
        heapq.heappush(myheap,-difference)
        right[nums[i-1]]=nums[i]
        left[nums[i]]=nums[i-1]
    i=1
    maximum=myheap[0] * -1
    for num in reversed(actual):
        answer[target-i]=maximum
        if maximum<right[num]-left[num]:
            maximum=right[num]-left[num]
        left[right[num]]=left[num]
        right[left[num]]=right[num]
        i+=1
    print(*answer)

if __name__ == '__main__':
    solve()      
#SORTING SAVES LIVES, AND UNNNECESSARY LOOPING