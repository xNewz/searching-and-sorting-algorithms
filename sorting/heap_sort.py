def heap_sort(arr):
  # Build a max heap from the input list
  arr = build_max_heap(arr)

  # Iterate through the list, swapping the first and last elements and heapifying the remaining elements
  for i in range(len(arr)-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    arr = heapify(arr, i, 0)

  # Return the sorted list
  return arr

def build_max_heap(arr):
  # Iterate through the list, starting at the middle and working backwards
  for i in range(len(arr)//2, -1, -1):
    # Heapify the element
    arr = heapify(arr, len(arr), i)
  # Return the heapified list
  return arr

def heapify(arr, n, i):
  # Initialize the indices of the left and right children
  left = 2*i + 1
  right = 2*i + 2

  # Initialize the index of the largest element to the current index
  largest = i

  # If the left child exists and is larger than the current element:
  if left < n and arr[left] > arr[largest]:
    # Update the index of the largest element
    largest = left
  # If the right child exists and is larger than the current element:
  if right < n and arr[right] > arr[largest]:
    # Update the index of the largest element
    largest = right
  # If the largest element is not the current element:
  if largest != i:
    # Swap the current element with the largest element
    arr[i], arr[largest] = arr[largest], arr[i]
    # Heapify the sublist starting at the index of the largest element
    arr = heapify(arr, n, largest)
  # Return the heapified list
  return arr

print(heap_sort([3,6,8,10,1,2,1]))  # prints [1, 1, 2, 3, 6, 8, 10]
