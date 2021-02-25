n=int(input())
prime=[False,False]+[True]*(n-1)
for i in range(2,int(n**(0.5)+1)):
    if prime[i]:
        for j in range(i*i,n+1,i): prime[j]=False     
print(prime.count(True))
