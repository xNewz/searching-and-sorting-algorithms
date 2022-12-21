def shell_sort(arr):
  # Initialize the gap between elements to sort
  gap = len(arr) // 2
  # While the gap is greater than 0:
  while gap > 0:
    # Iterate through the list, starting at the gap
    for i in range(gap, len(arr)):
      # Save the current element as a temporary variable
      temp = arr[i]
      # Initialize the index of the previous element
      j = i
      # While the previous element is greater than the current element and we are not at the beginning of the list:
      while j >= gap and arr[j - gap] > temp:
        # Shift the previous element gap positions to the right
        arr[j] = arr[j - gap]
        # Update the index of the previous element
        j -= gap
      # Insert the current element into its correct position
      arr[j] = temp
    # Reduce the gap between elements to sort
    gap //= 2
  # Return the sorted list
  return arr

print(shell_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
