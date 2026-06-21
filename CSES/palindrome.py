def solve():
    s=input().strip()#removes any hidden newline characters
    #string is already iteratable,so no use of converting it into a list
    palindrome=set()
    for i in s:
        if(i not in palindrome):
            palindrome.add(i)
        else:
            palindrome.discard(i)
    if len(palindrome)!=0 and len(palindrome)!=1:#CONTRADICTORY CASES SHOULDNT BELONG TO "OR"
        print("NO SOLUTION")
    else:
        print(palindrome)
        print("YES")
# s = input().split() $\rightarrow$ Python sees no spaces, so it creates a list with one item: ["aabbc"]        
                           
