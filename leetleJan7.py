def solve(nums):
	current_max = nums[0]
	max_ending_at_current = nums[0]
	for num in nums[1:]:
		max_ending_at_current = max(num, num + max_ending_at_current)
		if max_ending_at_current > current_max:
    		current_max = max_ending_at_current
	return current_max