#Title: Project-6a
def find_median(some_nums):
    """a function named find_median that takes as a parameter a list of numbers.
    The function should return the statistical median of those numbers"""
    some_nums.sort()

    if(len(some_nums) % 2 == 1):
        return some_nums[len(some_nums)//2]
    else:
        return (some_nums[len(some_nums)//2-1] + some_nums[len(some_nums)//2])/2

some_nums = [13, 7, -3, 82, 4]
result = find_median(some_nums)

#print("Median of list = ", find_median(some_nums))