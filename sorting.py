# CS 3364-002 Group Project
# Logan Preston
# Abenezer Setegn
# Luis Baeza


# Implementations of three sorting algorithms: Insertion Sort, Quicksort, and a
# hybrid of the two. The algorithms will be implemented on normal Python lists
# of numbers.


# Performs an in-place insertion sort on the array.
def insertionSort(array: list[int]):
    for i in range(len(array)):
        # Sort the i_th element into place
        for j in range(i, 0, -1):
            # Swap the i_th element down until it finds its place in the sorted subarray
            if array[j] < array[j - 1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
            # Once it finds its place, stop the inner loop and move on to the next element.
            else:
                break


# Partition a list according to the quicksort algorithm. Uses the middle element
# as a pivot. Returns three partitions: the elements lesser than the pivot, elements
# equalt to the pivot, and elements greater than the pivot.
# Assumes that array has at least two elements - it's up to the algorithms
# calling partition to ensure correct usage.
def partition(array: list[int]):
    lower = []
    upper = []
    same = []
    pivot = array[len(array) // 2]
    for x in array:
        if x < pivot:
            lower.append(x)
        elif x == pivot:
            same.append(x)
        else:
            upper.append(x)
    return lower, same, upper


# Classic quicksort algorithm - recursively sort the array into partitions,
# sort the partition, then stitch back together and return. Does NOT operate in place -
# returns a new list that is a sorted version of the original.
def quicksortClassic(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    left, same, right = partition(array)
    return quicksortClassic(left) + same + quicksortClassic(right)


# Our hybrid sort - quicksorts until the array length is less than or equal to k,
# our threshold, then we hand it over to the insertion sort algorithm.
def quicksortHybrid(array: list[int], threshold: int) -> list[int]:
    if len(array) <= threshold:
        insertionSort(array)
        return array
    left, same, right = partition(array)
    return quicksortHybrid(left, threshold) + same + quicksortHybrid(right, threshold)


if __name__ == "__main__":
    import random

    MAXLEN = 30
    THRESHOLD = 7
    myArray = [x for x in range(1, MAXLEN + 1)]
    myarray = random.shuffle(myArray)
    print(myArray)
    print("\n\n ==== SORTING ====")
    # insertionSort(myArray)
    newArray = quicksortHybrid(myArray, THRESHOLD)
    print(newArray)
