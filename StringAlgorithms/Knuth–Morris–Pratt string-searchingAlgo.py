## Read input as specified in the question.
## Print output as specified in the question.

def getLps(p):
    n=len(p)
    frwd=1
    check=0
    lps=[0]*n
    while frwd<n:
        if p[frwd]==p[check]:
            lps[frwd]=check+1
            check+=1
            frwd+=1
        else:
            if check==0:
                lps[frwd]=0
                frwd+=1
            else:
                check=lps[check-1]      
    return lps

def KMPSearch(s,p):
    ls=len(s)
    lp=len(p)
    lps=getLps(p)
    strPtr=0
    patPtr=0
    while strPtr<ls and patPtr<lp:
        if s[strPtr]==p[patPtr]:
            strPtr+=1
            patPtr+=1
        else:
            if patPtr==0:
                strPtr+=1
            else:
                patPtr=lps[patPtr-1]
        if patPtr==lp:
            return strPtr-lp
    return -1
s=input()
p=input()

# if p in s:
#     print(s.index(p))
# else:
#     print(-1)
print(KMPSearch(s,p))
