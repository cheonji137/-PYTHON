sum = 0
start = 1
end = 11
for i in range(1,11):
   sum += i
   if i < 4:
       print(i, end=" + ")
   elif i == end-1:
       print("...+ ",i, end=" = ")

print(sum)