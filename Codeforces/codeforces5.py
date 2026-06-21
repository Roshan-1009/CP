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
            list2 = [int(next(data)) for _ in range(n)]
            mymap={}
            list3=list1[:]#simply copying is not easy,this is a pointer trap
            for i in range(n):
                mymap[list1[i]]=i
            no_ofturns=0
            swaps=0
            list1.sort()
            isvalid=False
            for i in range(n):
                if list1[i]>list2[i]:
                    print(-1)
                    isvalid=True
                    break
            if isvalid==True:
                continue    
                    
            for i in range(n):
                if list3[i]>list2[i]:
                    swaps+=mymap[list2[i]]-i+  no_ofturns
                    no_ofturns+=1

            print(swaps)
                              






    except StopIteration:
        pass

if __name__ == '__main__':
    solve()            