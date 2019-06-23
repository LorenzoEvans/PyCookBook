
def binary_search(s_set, ele):
	low = 0
	high = len(s_set) - 1
	# low and high set the boundaries for what section of the list you'll search.
	while low <= high:
		# While the lowest index of the list is less than or equal to the highest index.
		# If a choice was found, it would be a single element of a list, meaning a list whose length is 1,
		# and if the length of the list is one, then the highest and lowest possible index are the same number,
		# meaning low and high have to be equal when a choice is found.
		mid = (low + high) / 2
		# While no choice has been found, the above line of code checks the middle element of the list.
		# The question is, how does adding the low(est index of the list) to the high(est index of the list) result,
		# in a value we can assume is equivalent to the middle index of the list?

		guess = s_set[mid]
		if guess == ele:
			return mid
		if guess > ele:
			high = mid - 1
		else:
			low = mid + 1
	return None

a_list = [1, 2 , 3, 5,  7, 9]


print(binary_search(a_list, 9))