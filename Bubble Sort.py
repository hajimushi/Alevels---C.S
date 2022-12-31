#Bubble Sort
#Module
#ascending order

list = [3,1,0,4,2,66,90,72]


def bubblesort(list):
    count = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(count):
            if list[i] > list[i+1]:
                sorted = False
                temp = list[i]
                temp2 = list[i+1]
                list[i + 1] = temp
                list[i] = temp2
    return list
output = bubblesort(list)
print(output)