def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = list(map(int, input("Enter a sorted array separated by spaces: ").split()))
target = int(input("Enter the element to search: "))
result = binary_search_iterative(arr, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")