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
 
def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    numbers = list(map(int, input_data[1:]))
    
    # We initialize our trackers with the absolute lowest possible values
    max_sum = -float('inf')
    current_sum = 0
    
    for i in numbers:
        # Add the current number to our running total
        current_sum += i
        
        # Did we just hit a new high score?
        if current_sum > max_sum:
            max_sum = current_sum
            
        # Is our backpack dead weight? Dump it.
        if current_sum < 0:
            current_sum = 0
            
    print(max_sum)
 
if __name__ == '__main__':
    solve()