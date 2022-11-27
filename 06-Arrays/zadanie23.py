def bubblesort(arr):
    n= len(arr)
    while n>1:
        zamien = False
        for l in range(0, n-1):
            if arr[l] > arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
                zamien = True
                
        n -= 1
        print(arr)
        if zamien == False: break
        
    return arr

arr=[4,36,12,28,9,44,5]
print(bubblesort(arr))