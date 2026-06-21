def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    target = int(input_data[0])
    stack=[]
    arr=[0]*target
    list1=list(map(int, input_data[1:]))
    for i in range(len(list1)):
        if not stack:#stack is empty
            arr[i]=0
            stack.append(i)
        else:
            top_item=stack[-1]
            if list1[i]>list1[top_item]:
                arr[i]=top_item+1
                stack.append(i)
            else:
                skip_to_next=False
                while list1[i]<=list1[top_item]:
                    if stack:
                        top_item=stack.pop()
                    else:
                        arr[i]=0
                        stack.append(i)
                        skip_to_next = True  # Signal that we want to skip the FOR loop
                        break
                if skip_to_next:
                    continue
                stack.append(top_item) # This safely continues the OUTER FOR loop!    
                arr[i]=top_item+1
                stack.append(i)
    print(*arr) 