import sys
import os

# 1. The Local Environment Check
# This automatically routes files if you are coding locally, 
# but ignores them when submitted to the online judge.
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

# 2. Fast I/O (Crucial for Python in CP to avoid Time Limit Exceeded)
input = sys.stdin.readline 

def solve():
    s=int(input().strip())#removes any hidden newline characters
    n=2**s
    o=1
    if s==0:
        print(0)
        return
    for l in range(n):
        result=""
        i=l
        while(i!=0):
            m=i%2
            i=i//2
            result=str(m)+result#taking 1+0 as 10
        padded_result=result.zfill(s)
        print(padded_result)
# s = input().split() $\rightarrow$ Python sees no spaces, so it creates a list with one item: ["aabbc"]


if __name__ == '__main__':
    # #1. Read the very first number (T) and convert it to an integer
    # T = int(input().strip())
    
    # # 2. Loop T times
    # for _ in range(T):
        solve()