#sorting is the key to this question
    #IF ELSE CONDTIONS SHOULD NOT BE CONTRICTING COMPLELTY

    # s=int(input().strip())
    # datas=input()
    # n=[int(x) for x in datas.split()]
    # k=sum(n)
    # difference1=k//2
    # difference2=k-difference1
    # limit1=difference1
    # limit2=difference2
    # n.sort(reverse=True)
    # for i in n:
    #     if i >= k//2:
    #         print(abs(2*i-k))
    #         return
    # if len(set(n))==1:
    #     if len(n)%2==0:
    #          print(0)
    #          return
    #     elif len(n)%2!=0:
    #          print(n[0])
    #          return
    # for i in n:
    #     if difference1==0 or difference2 == 0:
    #         print(abs(limit1-limit2))      
    #         return
    #     else:
    #         if difference1>=i:
    #             difference1-=i
    #         elif difference2>=i:
    #             difference2-=i
    #         else:
    #             if difference1>=difference2:
    #                 difference1+=i
    #                 sum1=k-difference1
    #                 print(sum1)
    #                 return
    #             else:
    #                 difference2+=i
    #                 sum2=k-difference2    
    #                 print(sum2)
    #                 return