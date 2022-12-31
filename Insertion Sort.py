#Insertion Sort
"""
list swapping
Divide the list into 2 parts, sorted and unsorted then compare and sort out the unsorted list
"""
list = [0,12,4,5,1,23,2]
def insertionsort(list):
    for x in range(len(list)):
        j = x
        while list[j-1] > list[j] and x > 0:
            temp = list[j]
            temp2 = list[j-1]
            list[j] = temp2
            list[j-1] = temp
            j = j -1

    return list

output = insertionsort(list)
print(output)



