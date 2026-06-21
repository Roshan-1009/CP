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
            list1 = [int(next(data)) for _ in range(3)]
            maxi=list1[0]
            mini=list1[1]
            divisor=list1[2]
            if mini > maxi:
                maxi, mini = mini, maxi
            print(maxi,mini)    
            difference=abs(maxi-mini)    
            if abs(maxi-mini) <= 2:
                print(difference)
            else:
                if divisor > maxi:
                    print(2)
                else:
                    times = math.log(maxi / mini, divisor) +  1e-9
                    up=math.ceil(times)
                    down=math.floor(times)
                    divided1 = maxi // (divisor**up)
                    divided2 = maxi // (divisor**down)

                    answer1 = up+abs( divided1 - mini) 
                    answer2 =  down+ abs(divided2 - mini) 
                    print(min(answer1,answer2))
                    
                    


            
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()