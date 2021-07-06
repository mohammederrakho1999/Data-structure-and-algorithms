
#time complexity: O(N)
# space complexity: O(1)
def ValidateSubsequence(array, arraysub):
	for i in range(len(arraysub)):
		if arraysub[i] and arraysub[i + 1] in array:
			if array.index(arraysub[i + 1]) > array.index(arraysub[i]):
				print("TRUE")
				return True

		else:
			return False


#time complexity: O(N)
# space complexity: O(1)
def ValidateSubsequence2(array, arraysub):
	index1 = 0
	index2 = 0
	counter = 0

	while index1 < len(array) and index2 < len(arraysub):
		if array[index1] == arraysub[index2]:
			index2 += 1
			counter += 1
		index1 += 1

		if len(sequence) == counter:
			print("valide subsequence")
			return True
		else:
			print("Not a valide subsequence")
			return False


