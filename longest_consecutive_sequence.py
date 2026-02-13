nums=[100,4,200,1,3,2,4,5,6,7,200,340,400,500,12,13,14,16,17,18,20,21,22,23,24,25,26]
s=set(nums)
longest=0
best=[]

for n in s:
    if n-1 not in s:
        cur=n
        seq=[cur]
        while cur+1 in s:
            cur+=1
            seq.append(cur)
        if len(seq)>longest:
            longest=len(seq)
            best=seq

print("Length:",longest)
print("Sequence:",best)
