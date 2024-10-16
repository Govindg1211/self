def binary_search(arr, val, start, end):
    """Helper function to perform binary search."""
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binary_insertion_sort(arr):
    """Sorts an array using binary insertion sort."""
    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i - 1)
        
        arr[pos + 1:i + 1] = arr[pos:i]
        
        arr[pos] = val

if __name__ == "__main__":
    sample_array = [5, 2, 9, 1, 5, 6]
    print("Original array:", sample_array)
    
    binary_insertion_sort(sample_array)
    
    print("Sorted array:", sample_array)