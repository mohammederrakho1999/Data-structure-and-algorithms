
# First solution 
# complexity: O(N²) because of the Two for loops
# space complexity:O(1)
def TwoNumberSum(array, target):

	for i in range(len(array)):
		for j in range(i + 1, len(array) - 1):
			if array[i] + array[j] == target:
				return (array[i], array[j])
			else:
				print("didn't find it")

	return False

#second solution: using Hash Table 
# time complexity: O(N) time
# space complexity: O(N) because we are storing a dictionary 
def TwoNumberSum1(array, target):
	HashTable = {}
	for i in range(len(array)):
		y = target - array[i] 
		if y in HashTable:
			return [array[i], y]
			print([array[i], y])
		else:
			HashTable[array[i]] = True
	return False
	
# third solution
# time complexity: O(nlog(n))
# space complexity: O(1)
def TwoNumbersum2(array, target):
	array.sort()

	i = 0
	j = len(array) - 1
	while i < j:
		value = array[i] + array[j]
		if value == target:
			return [array[i], array[j]]
		elif value > target:
			j -= 1
		elif value < target:
			i += 1

    return False