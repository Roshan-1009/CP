def solve():
    t=int(input().strip())
    for _ in range(t):
        k=int(input().strip())
        count=0
        i=0 
        while(k-count>0):#whiule loop will give true even if the the answer is negative
            possible_count=count
            count+=9*(pow(10,i))*(i+1)#9
            i+=1#1
        digit_offset=k-possible_count#10
        #you still writing 9*x as 9x
        #exact_offset=math.ceil(digit_offset+i-1/i)#divide into digit chunks
        exact_offset=(digit_offset+i-1)//i
        #exact_offset=5
        base_address=int((i-1)*"9") if i>1 else 0
        actual_value=base_address+exact_offset
        #7,any digit %1 is 
        array_offset=(digit_offset%i)-1
        answer=str(actual_value)[array_offset]
        print(answer)
    return 