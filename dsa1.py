arr= [100,20,20,2,1]
arrlen = len(arr)
input = 143

for i in range (arrlen):
  while input >= arr[i]:
       print(arr[i])
       input-= arr[i]