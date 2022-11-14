arr=[-15, 8, -31, 47, -2, 19]
min=0
for i in range(0,len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)
max=0
for i in range(0,len(arr)):
    if max<arr[i]:
        max=arr[i]
print(max)

#inny przyklad
maks=arr[0]
for i in arr:
    if i>maks:
        maks=i
print(maks)

