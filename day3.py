def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # element to be placed
        j = i - 1

        # Move elements that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift right
            j -= 1

        arr[j + 1] = key  # place key in the correct spot

# Example usage:
arr = [7, 3, 5, 2]
insertion_sort(arr)
print("Sorted array:", arr)
