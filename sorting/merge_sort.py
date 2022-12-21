def merge_sort(arr):
  # Base case: if the list has 0 or 1 elements, it is already sorted
  if len(arr) <= 1:
    return arr
  
  # Split the list into two equal-sized sublists
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  
  # Recursively sort the left and right sublists
  left = merge_sort(left)
  right = merge_sort(right)
  
  # Merge the sorted sublists
  return merge(left, right)

def merge(left, right):
  # Initialize an empty result list
  result = []
  # Initialize indices for the left and right sublists
  left_idx = 0
  right_idx = 0
  # Iterate until one of the sublists is exhausted
  while left_idx < len(left) and right_idx < len(right):
    # If the current element in the left sublist is smaller than the current element in the right sublist:
    if left[left_idx] < right[right_idx]:
      # Append the current element from the left sublist to the result list
      result.append(left[left_idx])
      # Move to the next element in the left sublist
      left_idx += 1
    # Otherwise:
    else:
      # Append the current element from the right sublist to the result list
      result.append(right[right_idx])
      # Move to the next element in the right sublist
      right_idx += 1
  # Append the remaining elements from the left sublist, if any
  result.extend(left[left_idx:])
  # Append the remaining elements from the right sublist, if any
  result.extend(right[right_idx:])
  # Return the merged and sorted list
  return result

print(merge_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
