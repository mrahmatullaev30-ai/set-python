import os
os.system("cls")

set1={2,3,4,5,6}
set2={4,5,6,7,8,9}

set3 = set2.symmetric_difference(set1)
print(set3)

sum = 0

for x in set3:
    sum += x
print(sum)

