def solve():
    import itertools
    s=input().strip()
    myset=set()
    s1=list(s)
    for i in itertools.permutations(s1):#this is a generator and can be only invoked all the words using the for loop
        #i is a tuple containing randome characvters as list
        word="".join(i)#you cant seperate this line
        myset.add(word)#only add words that are unique
    print(len(myset))
    # sorted(myset) this wont 
    for i in sorted(myset):
         print(i)