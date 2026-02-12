n1=7889
n2=8987

hashtable = [0 for i in range (10)]

temp_n1 = n1
temp_n2 = n2

while temp_n1 !=0 or temp_n2 != 0:
    if temp_n1 != 0:
        last1 = temp_n1 % 10
        hashtable[last1] += 1
        temp_n1 = temp_n1 // 10
    if temp_n2 != 0:
        last2 = temp_n2 % 10
        hashtable[last2] += 1
        temp_n2 = temp_n2 // 10

print(f"Constructed Hashtable: {hashtable}")