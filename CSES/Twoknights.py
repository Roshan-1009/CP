def solve():
    n=int(input())#do not use split as there is only one input integer
    for i in range(1,n+1):
        print((i*i)*(i*i-1)//2 - 4*(i-1)*(i-2),end="\n")#* us this properly,dont forget here and there
        #Most phenomenal permutation problem