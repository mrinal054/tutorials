"""
Merge sort
"""

def mergesort(arr):
    
    if len(arr) == 1: return arr # stopping criterion
    else:   
        mid = len(arr)//2 # divide array into approx halves
        l_arr = arr[:mid] # left array
        r_arr = arr[mid:] # right array
        
        l_arr_sort = mergesort(l_arr) # recursive 
        r_arr_sort = mergesort(r_arr) # recursive
        
        # Start combining 
        i, j, k = 0, 0, 0 # three pointers
        
        # Compare left and right arrays
        while i < len(l_arr_sort) and j < len(r_arr_sort):
            if l_arr_sort[i] <= r_arr_sort[j]:
                arr[k] = l_arr_sort[i]
                i += 1 # increment pointer i
            else:
                arr[k] = r_arr_sort[j]
                j += 1 # increment pointer j
                
            k += 1 # increment pointer k
            
        # Check remaining elements
        while i < len(l_arr_sort):
            arr[k] = l_arr_sort[i]
            i += 1 # increment pointer i
            k += 1 # increment pointer k
                
        while j < len(r_arr_sort):
            arr[k] = r_arr_sort[j]
            j += 1 # increment pointer j
            k += 1 # increment pointer k
                
        return arr

# Test
if __name__ == '__main__':    
    arr = [15, 9, 5, 5, 11, 7, 21]
    mergesort(arr)
    print(arr)
                    
            
