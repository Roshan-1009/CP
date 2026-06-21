import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    sticks = list(map(int, input_data[1:]))
    
    # 1. Sort the array so the median is exactly in the middle
    sticks.sort()
    
    # 2. Grab the median stick (n // 2 handles both odd and even arrays perfectly)
    median_stick = sticks[n // 2]
    
    # 3. Calculate the total cost using absolute difference
    total_cost = 0
    for stick in sticks:
        total_cost += abs(stick - median_stick)
        
    print(total_cost)

if __name__ == '__main__':
    solve()