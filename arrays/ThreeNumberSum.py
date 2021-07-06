
# find triplet that sum up to the target num
# time complexity: O(N²)
# space complexity:O(1)
def ThreeNumberSum(Array, TargetNumber):
	all_triplet = []
	for i in range(len(Array)):
		for j in range(i + 1, len(Array) - 1):
			for k in range(j + 1, len(Array) - 1):
				Sum = Array[i] + Array[j] + Array[k]
				if Sum == TargetNumber:
					all_triplet.append([Array[i], Array[j], Array[k]])
				else:
					print("NOT FOUND YET")
	return all_triplet

#all_triplet = ThreeNumberSum([1,2,3,1,2,-6,5,-8,6],0)
#print(all_triplet)


def ThreeNumberSum1(Array, TargetNumber):

	Array.sort()
	all_triplet = []

	for i in range(len(Array) - 2):
		left = i + 1
		right = len(Array) - 1

		while left < right:
			Sum = Array[right] + Array[left] + Array[i]
			if Sum == TargetNumber:
				all_triplet.append([Array[right], Array[left], Array[i]])
				right -= 1
				left += 1
			elif Sum < TargetNumber:
				left += 1
			elif Sum > TargetNumber:
				right -= 1
	
	return all_triplet

all_triplet = ThreeNumberSum1([1,2,3,1,2,-6,5,-8,6],0)
print(all_triplet)
