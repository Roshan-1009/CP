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
    
    # 1. Build an array of tuples: (value, original_index)
    # The original index is i + 1 because CSES wants 1-based indexing!
    arr = []
    for i in range(n):
        arr.append((int(input_data[i + 2]), i + 1))
        
    # 2. Sort the array. Python naturally sorts by the first item in the tuple (the value).
    arr.sort()
    
    # 3. Lock in the first number (it only needs to go up to the 3rd to last element)
    for i in range(n - 2):
        
        # The sum we need our two pointers to find
        rem = target - arr[i][0]
        
        # 4. Set up the Two Pointers
        left = i + 1
        right = n - 1
        
        # 5. Squeeze!
        while left < right:
            current_sum = arr[left][0] + arr[right][0]
            
            if current_sum == rem:
                # We found it! Print the original indices of all three numbers.
                print(arr[i][1], arr[left][1], arr[right][1])
                return
                
            elif current_sum < rem:
                # Sum is too small, move the left pointer up to get a bigger number
                left += 1
                
            else:
                # Sum is too big, move the right pointer down to get a smaller number
                right -= 1
                
    # If the loop finishes without returning, it's impossible.
    print("IMPOSSIBLE")

if __name__ == '__main__':
    solve()      
