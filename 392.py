def testSolution(s, t):
    #run through t and check if the next letter is the next letter in s, if so pop that and continue
    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return True if i == len(s) else False
        


s = "axc"
t = "ahbgdc"


print(testSolution(s, t))
    