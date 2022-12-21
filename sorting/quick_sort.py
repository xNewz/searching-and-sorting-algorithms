def quick_sort(arr):
  # Base case: if the list has 0 or 1 elements, it is already sorted
  if len(arr) <= 1:
    return arr

  # Choose the pivot element as the middle element of the list
  pivot = arr[len(arr) // 2]

  # Partition the list into three sublists:
  #  - elements less than the pivot
  #  - elements equal to the pivot
  #  - elements greater than the pivot
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  # Recursively sort the left and right sublists
  left = quick_sort(left)
  right = quick_sort(right)

  # Return the sorted list
  return left + middle + right

print(quick_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
