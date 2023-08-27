def testSolution(s, t):
    sest = {}
    test = {}

    for char in s:
        sest[char] = sest.get(char, 0) + 1

    for char in t:
        test[char] = test.get(char, 0) + 1

    return test == sest

s = "ab"
t = "a"


print(testSolution(s, t))
    