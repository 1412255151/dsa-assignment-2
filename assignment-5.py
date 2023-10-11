def basic_sort(strings):
    return sorted(strings)

strings = input("Enter a list of strings (comma-separated): ").split(',')
sorted_strings = basic_sort(strings)
print("Sorted Strings:", sorted_strings)