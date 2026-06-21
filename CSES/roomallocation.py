import heapq

def solve():
    # 1. Instantly map the entire input file to integers using C-level memory
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
        
    n = data[0]
    
    # 2. THE SPEED HACK: No 'for' loop to build the array!
    # data[1::2] -> All Arrivals
    # data[2::2] -> All Departures
    # zip() glues them to their original index, and sorted() handles it instantly.
    active_rooms = sorted(zip(data[1::2], data[2::2], range(n)))
    
    ordering = [0] * n
    myheap = []
    rooms = 0
    
    # 3. The minimal, perfectly optimized Priority Queue
    for arr, dep, idx in active_rooms:
        
        # If the heap exists AND the smallest departure is strictly less than arrival
        if myheap and myheap[0][0] < arr:
            free_room = myheap[0][1]
            heapq.heapreplace(myheap, (dep, free_room))
            ordering[idx] = free_room
        else:
            rooms += 1
            heapq.heappush(myheap, (dep, rooms))
            ordering[idx] = rooms
            
    # 4. Blazing fast output straight to standard out
    sys.stdout.write(str(rooms) + '\n')
    sys.stdout.write(" ".join(map(str, ordering)) + '\n')