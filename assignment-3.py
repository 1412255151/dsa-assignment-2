def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

arr = list(map(int, input("Enter an array separated by spaces: ").split()))
sorted_arr = quick_sort_recursive(arr)
print("Sorted Array:", sorted_arr)