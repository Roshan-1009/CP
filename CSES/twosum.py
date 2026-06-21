nummap={}
for i,num in enumerate(nums):#for [indexname],[value] in enumerate([list])
    difference = target-num
    if difference in nummap:
        return(nummap[difference],i)
    else:
        nummap[num]=i    