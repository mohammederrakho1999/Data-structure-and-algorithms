

def MonotonicArray(array):
	# set our hypothesis
	IsNotDecreasing = True
	IsNotIncreasing = True

	for i in range(len(array) - 1):

		if array[i] < array[i - 1]:
			IsNotDecreasing = False
		if array[i] > array[i - 1]:
			IsNotIncreasing = False

	return IsNotIncreasing or IsNotDecreasing



f = MonotonicArray([-1,22,1,0])
print(f)