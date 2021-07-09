

def SpiralTraverse(array2D):
	startrow, endrow = 0, len(array2D) - 1
	startcol, endcol = 0, len(array2D[0]) - 1

	results = []

	while startrow <= endrow and startcol <= endcol:


		for col in range(startcol, endcol + 1):
			results.append(array2D[startrow][col])

		for row in range(startrow + 1, endrow + 1):
			results.append(array2D[row][endcol])

		for col in reversed(range(startcol,endcol)):
			results.append(array2D[endrow][col])

		for row in reversed(range(startrow + 1, endrow)):
			results.append(array2D[row][startcol])


		startrow += 1 
		endrow -= 1

		startcol += 1
		endcol -= 1


	return results

