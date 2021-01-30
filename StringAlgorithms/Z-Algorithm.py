s=input('enter the text')
p=input('enter the pattern')

newStr=p+'æ'+s
# net string 

def getZarray(newstr):
    left=0
    right=0
    zarr=[0]*len(newstr)
    n=len(newstr)
    k=left=right=0
    for i in range(1,n):
        if right<i:
            left=right=i
            while right<n and newstr[right]==newstr[right-left]:
                right+=1
            zarr[i]=right-left
            right-=1
        else:
            k=i-left
            if k+zarr[k]<=right:
            	zarr[i]=zarr[k]
            else:
                left=i
                while right<n and newstr[right]==newstr[right-left]:
                	right+=1
                zarr[i]=right-left
                right-=1
    return zarr

za=getZarray(newStr)
pl=len(p)
for ind,ele in enumerate(za):
    if ele==pl:
        print(ind-pl-1)
        break
else:
	print(-1)
            
            
            
            
            
        
