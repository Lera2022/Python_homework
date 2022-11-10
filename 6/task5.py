# For a given list of integers, return the index of the elements where the sums of the integers to the left and right of the current element are equal.
# Example:
# ints = [4, 1, 7, 9, 3, 9]
# Sinse 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3
# ints = [1, 0, -1]
# Returns None/nil/undefined/etc (depending on the language) as there are not indices where the left and right sums are equal. Here are the 2 important rules:
# The element at the index to be returned is not included in either of the sum calculations!
# Both the first and last index cannot be considered as a "midpoint" (So None for [X] and [X, X])

# def find_central_point(nums):
#     for i in range(len(nums)):
#         if sum(nums[i+1:])==sum(nums[:i]):
#             return i

nums = [4, 1, 7, 9, 3, 9]
find_central_point = [i for i in filter(lambda x: sum(nums[x+1:])==sum(nums[:x]), range(len(nums)))]

print(find_central_point)