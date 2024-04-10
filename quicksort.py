"""
Quicksort
"""

def partition(arr, p):
    # p -> index of the pivot
    # Transfer smaller values to the left and higher values to the right of the pivot
    i = -1 # pointer to the larger value
    
    for j in range(len(arr)-1): # don't need to compare with the pivot
        # Swap if arr[j] is less than the pivot value
        if arr[j] < arr[p]:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
            
    # Swap with the pivot
    i += 1
    (arr[i], arr[p]) = (arr[p], arr[i])
    
    return i # return pivot index
            

def quicksort(arr, l, h):
    # assuming h as the pivot index
    
    if l < h: # stopping criterion
        new_p = partition(arr, h) # partition the array and get new pivot index
        
        # Recursion
        quicksort(arr, l, new_p-1) # parition of the values to the left of pivot
            
        quicksort(arr, new_p+1, h) # parition of the values to the right of pivot


if __name__ == '__main__':            
    arr = [5, 12, 7, 15, 3, 22, 10]    
    l = 0
    h = len(arr) - 1
    
    # x = partition(arr, p)
    quicksort(arr, l, h)
    
    print(arr)


    
