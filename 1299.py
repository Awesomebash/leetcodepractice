def testSolution(arr):
    highestNum = arr[len(arr) - 1]
    for index, i in enumerate(reversed(arr)):
        arr[len(arr) - 1 - index] = highestNum
        if i > highestNum:
            highestNum = i
    arr[len(arr) - 1] = -1
    return arr

s = [17,18,5,4,6,1]
#Use a pointer to check where we are in the array, use another pointer to check what the greatest element is

print(testSolution(s))
    