goldprices=[7,4,9,1,3,2]
arrlen= len (goldprices)

minValue = goldprices[0]
maxprofit=0

for i in range(arrlen):
  if goldprices[i] < minValue:
    minValue = goldprices[i]
  profit = goldprices[i] - minValue
  if profit > maxprofit:
    maxprofit = profit
print(f"max profit: {maxprofit} ")