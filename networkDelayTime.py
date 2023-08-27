def testSolution(times, n, k):
    minHeap = [[0, k]]
    for num in range(n):
        for i in times:
            if not minHeap:
                return -1
            if i[0] == minHeap[0][1]:
                minHeap.append([minHeap[0][0] + i[2], i[1]])
        print(minHeap)
        x = minHeap.pop(0)
        for index, indiv in enumerate(minHeap):
            if indiv[1] == x[1]:
                print(index)
                minHeap.pop(index)  
        minHeap.sort()
    return x[0]
        



times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
n = 4
k = 1


print(testSolution(times, n, k))
    