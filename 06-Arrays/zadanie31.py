arr=[4,5,2,7,9,12,7]
tab=[]
for i in arr:
    if int(i)%2==0:
        tab.append(i)
for i in arr:
    if int(i)%2!=0:
        tab.append(i)
        
print(tab)