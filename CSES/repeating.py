def solve():
    s=input().strip()
    prev_count=1
    count=1
    for i in range(1,len(s)):
        if s[i-1]!=s[i]:
            if count>=prev_count:
                prev_count=count
            count=1#be very careful of identation 
        else:
            count=count+1
    print(max(count,prev_count))