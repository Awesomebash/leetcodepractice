
def recur(nums):
    print (nums)
    if nums[0] < nums[len(nums) - 1]:
        return nums[0]
    if nums[0] > nums[int(len(nums) / 2)]:
        return recur(nums[0:round(len(nums) / 2)])
    elif round(len(nums) / 2) != len(nums):
        return recur(nums[round(len(nums) / 2):len(nums)])
    
    


def testSolution(nums):
    return recur(nums)
    

    

s = [2, 4, 5, 6, 7, 0, 1]


print(testSolution(s))
    