def insertion_sort(arr):
  # Iterate through each element in the list, starting at index 1
  for i in range(1, len(arr)):
    # Save the current element as a temporary variable
    temp = arr[i]
    # Initialize the index of the previous element
    j = i - 1
    # While the previous element is greater than the current element and we are not at the beginning of the list:
    while j >= 0 and arr[j] > temp:
      # Shift the previous element one position to the right
      arr[j+1] = arr[j]
      # Update the index of the previous element
      j -= 1
    # Insert the current element into its correct position
    arr[j+1] = temp
  # Return the sorted list
  return arr

print(insertion_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
