import sys
import os
import math

# 1. The Local Environment Check
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return 
        
    # Create the iterator
    data = iter(input_data)
    
    try:
        # Grab the total number of test cases (e.g., 4)
        t = int(next(data))
        
        # Loop through each test case
        for _ in range(t):
            
            # 2. Scoop out exactly 'n' elements for this test case's list
            n = int(next(data))
            list1 = [int(next(data)) for _ in range(n)]
            count=0
            for i in range(n-1):
                if list1[i]>list1[i+1]:
                    list1[i]+=list1[i+1]
                    list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1[n-1])     



    except StopIteration:
        pass

if __name__ == '__main__':
    solve()            