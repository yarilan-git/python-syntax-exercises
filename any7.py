def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for number in nums:
        if number == 7:
            return True
    return False

    

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

