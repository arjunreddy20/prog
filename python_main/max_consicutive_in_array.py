


def count_max_consecutive_repeats(nums):
    if not nums:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1

    # Check the last sequence
    if current_count > max_count:
        max_count = current_count

    return max_count

# Example inputs
array1 = [1, 1, 0, 1, 1, 1]
array2 = [2, 2, 0, 6, 2, 2, 21]

# Example outputs
output1 = count_max_consecutive_repeats(array1)
output2 = count_max_consecutive_repeats(array2)

print(output1)  # Expected output: 3
print(output2)  # Expected output: 2
