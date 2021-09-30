def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at position: ",result)
else:
    print("Element is not present in array")
