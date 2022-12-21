def comb_sort(arr):
  # Initialize the gap between elements to compare
  gap = len(arr)
  # Initialize the shrink factor
  shrink = 1.3
  # While the gap is greater than 1:
  while gap > 1:
    # Iterate through the list, starting at index 0
    for i in range(len(arr)-gap):
      # If the current element is greater than the element gap positions to the right:
      if arr[i] > arr[i+gap]:
        # Swap the elements
        arr[i], arr[i+gap] = arr[i+gap], arr[i]
    # Reduce the gap using the shrink factor
    gap = int(gap / shrink)
  # Return the sorted list
  return arr

print(comb_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
