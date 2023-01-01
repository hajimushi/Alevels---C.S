#Iterative
#Recursive
#The recursive method follows the divide and conquer approach.



#search for 4
x = 9
#Array
array = [3, 4, 5, 6, 7, 8, 9]
# Binary Search in python
def binary_iterative(array,x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        elif array[mid] > x:
            right = mid - 1
    return False




output = binary_iterative(array,x)
if output != False:
    print(f"Item found at position {output}")
else: print("number not present")




