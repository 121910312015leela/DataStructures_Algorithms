## Read input as specified in the question.
## Print output as specified in the question.
# Given a string S, count and return the number of substrings of S that are palindrome.
# Single length substrings are also palindromes. You just need to calculate the count, not the substrings.
s=input()
n=len(s)
def check(s,l,r):
    # curInd=l-1
    count=0
    while l>=0 and r<n and s[l]==s[r]:
        l-=1
        r+=1
        count+=1  
    return count
def traverse(s):
    ans=0
    for i in range(0,n):
        ans+=check(s,i-1,i+1)
        ans+=check(s,i,i+1)
    return ans
print(traverse(s)+n)
    
