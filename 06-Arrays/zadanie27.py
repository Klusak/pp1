arr=[5,1,9,6,1]
min=9999
for i in range(0,len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)
max=0
for i in range(0,len(arr)):
    if max<arr[i]:
        max=arr[i]
print(max)
print(max-min)