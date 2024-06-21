def contains_duplicate(nums):
    duplicate = set()
    for i in nums:
        if i in duplicate:
            return True
        else:
            duplicate.add(i)

    return False

print(contains_duplicate([1,2,3,1]))