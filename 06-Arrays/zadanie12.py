arr=[[2,5,4],[9,0,3]]
print(arr)
print(len(arr),len(arr[0]))
print(arr[0][1])
print(arr[1][-1])
for i in arr[1]:
    print(i,end=" ")
print()
for i in arr:
    print(i)
for i in arr:
    print(i[len(i)-1])