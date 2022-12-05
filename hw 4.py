# theList = [10,20,5]
# product1  = 1
# for number in theList:
#     product1 *= number
# print(product1)
#
# x = 0
# while (x <1001):
#     print(x)
#     x = x+1


def selection_sort(array):
    length = len(array)

    for i in range(length - 1):
        minIndex = i

        for j in range(i + 1, length):
            if array[j] < array[minIndex]:
                minIndex = j

        array[i], array[minIndex] = array[minIndex], array[i]

    return array


array = [10, 15, 9, 30, 109]