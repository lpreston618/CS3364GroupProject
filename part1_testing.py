from os import write
from random import shuffle
from timeit import default_timer as timer

import sorting


# Returns a new list containing numbers 1 to n
def getSortedList(n: int):
    return list([x + 1 for x in range(n)])


# Returns a list of numbers 1 to n in a random order
def getShuffledList(n: int):
    mylist = getSortedList(n)
    shuffle(mylist)
    return mylist


# Verify that our hybrid sorting algorithm matches python's built-in sort
def verifySort(array):
    print("=== Verifying correctness of hybrid sort ===")
    print("Sorting test array:\t" + str(array))
    arraycopy = array[:]  # make a copy of the test array
    arraycopy.sort()  # sort the copy with python's built-in sorting algorithm
    array = sorting.quicksortHybrid(
        array, 5
    )  # sort array with our hybrid algorithm with a sample threshold of 5
    print("Python's sort:\t\t" + str(arraycopy))
    print("Our hybrid sort:\t" + str(array))
    print("Our output matches Python's: " + str(array == arraycopy))


def main():
    # Verify that our hybrid algorithm sorts correctly
    testarray = getShuffledList(20)
    verifySort(testarray)

    # Produce test data for different k,n values
    with open("part1data.txt", "w") as output:
        print("=== Producing runtime data for hybrid sort ===")
        print("Writing data to part1data.txt ...")
        output.write("Hybrid Sort data: (n,k,time)\n")
        # Test at different values of n
        n = 100
        kvals = [2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        for _ in range(10):
            # For each n value, test different k values. We'll use some preset values for k,
            # and we won't test when k > n/2. Thus, as we scale up n, we'll test more k values.
            for k in kvals:
                if k > n / 2:
                    break
                # We'll average runtime across three trials
                test1 = getShuffledList(n)
                test2 = getShuffledList(n)
                test3 = getShuffledList(n)

                start = timer()
                sorted1 = sorting.quicksortHybrid(test1, k)
                sorted2 = sorting.quicksortHybrid(test2, k)
                sorted3 = sorting.quicksortHybrid(test3, k)
                end = timer()
                elapsed = end - start
                average = elapsed / 3
                output.write(f"{n},{k},{average}\n")
            n *= 2


if __name__ == "__main__":
    print("Testing Part 1 sorting algorithms...")
    main()
