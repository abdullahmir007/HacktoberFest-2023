def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Take user input for the array
input_array = input("Enter numbers separated by space: ").split()
# Convert input strings to integers
input_array = [int(num) for num in input_array]

print("Original array:", input_array)

# Perform selection sort
selection_sort(input_array)

print("Sorted array:", input_array)
