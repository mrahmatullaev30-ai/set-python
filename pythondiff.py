import os
os.system("cls")

set1={"Artel","Alif","Yandex", "Google", "Meta"} 
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

umumiy = set1 & set2 & set3
faqat_birimchi = set1 - set2 - set3

for i in umumiy:
    print(i)
for x in faqat_birimchi:
    print("Faqat birinchida bor matnlar", x)