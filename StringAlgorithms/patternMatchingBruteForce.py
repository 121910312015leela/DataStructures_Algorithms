# pattern matching algorithm
# O(n*m)

# given a string s and a pattern p
# we need to find . check if the pattern is present in the given string
 
s= input()
p= input()
 
print(s)
print(p)
def match(s,p):
    Ls=len(s)
    Lp=len(p)
    for i in range(Ls-Lp+1):
        found=True
        for j in range(Lp):
            if s[i+j]!=p[j]:
                print(s[i+j],p[j],i,j)
                found=False
                break
        if found:return True
    return False
re=match(s,p)

if re:print("match found")
else:print('not found')
