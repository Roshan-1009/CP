def solve():
    #SHIFTING THE BITS IS THE KEY TO THIS PROBLEM,RIGHT SHIFT
    # 1. Fast I/O: Gulp the entire input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    
    idx = 1
    out = [] # Store all our answers here to print all at once (super fast!)
    
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        # --- IMPOSSIBLE CONDITIONS ---
        
        # 1. You cannot have more mismatches than the size of the array
        if b + c > a:
            out.append("NO")
            continue
            
        # 2. The "Conservation of Sum" rule: 
        # If permutations have the same sum, you cannot have 'greater' elements 
        # without balancing them out with 'lesser' elements somewhere else.
        if (b == 0 and c > 0) or (c == 0 and b > 0):
            out.append("NO")
            continue
            
        out.append("YES")
        
        # --- THE ARRAY SHIFT TRICK ---
        
        # List 1 is always just a straight line from 1 to a
        list1 = list(range(1, a + 1))
        
        # List 2 starts identical to List 1
        list2 = list(range(1, a + 1))
        
        if b + c > 0:
            ties = a - (b + c)
            
            # We grab the part of list2 that needs to be scrambled
            suffix = list2[ties:]
            
            # The Magic: Shift the suffix to the right by 'c' positions.
            # We do this by taking the last 'c' elements, and moving them to the front.
            shifted_suffix = suffix[-c:] + suffix[:-c]
            
            # Put the shifted chunk back into list2
            list2[ties:] = shifted_suffix
        
        # Format the arrays nicely into space-separated strings
        out.append(" ".join(map(str, list1)))
        out.append(" ".join(map(str, list2)))
        
    # Print everything at the very end
    print("\n".join(out))