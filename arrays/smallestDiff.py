

# this questions gives you Two arrays and ask you to find the smmlest differece between these arrays
# complexity time: O(N2) assuming that sorting used a fancy sorting algorithmes
# space complecity: O(K) k is the lenght of dictionary
def SmallestDifference(array1, array2): 
	HashTable = {}

	for i in range(len(array1) - 1):
		for j in range(len(array2) - 1):
			currentdiff = array1[i] - array2[j]
			currentdiffabs = abs(currentdiff)
			if currentdiffabs in HashTable:
				HashTable[currentdiffabs].append([array1[i], array2[j]])

			else:
				HashTable[currentdiffabs] = [array1[i], array2[j]]

	index = sorted(HashTable.keys())[0]

	#return HashTable[next(iter(HashTable))]
	return HashTable[index] 


def SmallestDifference1(array1, array2): 
	array1.sort()
	array2.sort()

	index1 = 0
	index2 = 0

	currentdiff = float("inf")
	smmallest = float("inf")

	while index1 < len(array1) and index2 < len(array2): 
		 item1 = array1[index1] 
		 item2 = array2[index2]

		if item1 < item2:
			currentdiff = item2 - item1
			index1 += 1
		elif item1 > item2:
			currentdiff = item1 - item2
			index2 += 1
		else:
			return [item1, item2]

		if smmallest > currentdiff:
			smmallest = currentdiff
			smmallestpair = [item1, item2]

	return smmallestpair





#x = SmallestDifference1([-1,5,10,20,28,3],[26,134,135,15,17])
#print(x)




