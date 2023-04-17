def toh(n,s,a,d):
    if n==1:
        print(n,"move from",s,"to",d)
    else:
        toh(n-1,s,d,a)
        print(n,"move from",s,"to",d)
        toh(n-1,a,s,d)

toh(4,"s","a","d")
