def minmax(arr):
    tab=[]
    min=9999
    for i in range(0,len(arr)):
        if min>arr[i]:
            min=arr[i]
    tab.append(min)
    max=0
    for i in range(0,len(arr)):
        if max<arr[i]:
            max=arr[i]
    tab.append(max)
    return tab
arr=[4,2,8,4,7,9,5]
print(minmax(arr))
