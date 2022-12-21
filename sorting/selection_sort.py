def selection_sort(arr):
  # Iterate through each element in the list
  for i in range(len(arr)):
    # Initialize the minimum index to the current index
    min_idx = i
    # Iterate through the remaining elements in the list
    for j in range(i+1, len(arr)):
      # If the current element is less than the minimum element, update the minimum index
      if arr[min_idx] > arr[j]:
        min_idx = j
    # Swap the current element with the minimum element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  # Return the sorted list
  return arr

print(selection_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
