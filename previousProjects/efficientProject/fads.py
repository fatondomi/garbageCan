
class efficient:

	def addition(self, minInt, maxInt, dim):

		newList = []

		for i in range(0, minInt):

			newRow = []

			for j in range(0, minInt):
				newRow.append(0)
			newList.append(newRow)

		for i in range(minInt, maxInt + 1):

			newRow = []

			for j in range(minInt, maxInt + 1):
				newRow.append(i + j)
			
			newList.append(newRow)
		return newList
eObj = efficient()

add2 = [[0,1],
 		[1,2]]

add2New = eObj.addition(0,1)

def addTwo(x,y):
	return x+y

numri1 = 1
numri2 = 0

print(addTwo(numri1,numri2))
print(add2[numri1][numri2])
print(add2New[numri1][numri2][numri3])

