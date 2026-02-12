n=100
arr=[10,20,30,40,50]
n = n%5
arrlen = len(arr)

for j in range(n):
#1 shift
   last =arr[-1]
   for i in range(arrlen -1, -1, -1):
      arr[i]= arr [i-1]
      arr[0] =last
print(arr)