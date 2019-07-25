import time
def main():
	# testCases = raw_input()
	# checkPoints = raw_input()
	# costStr = raw_input()
	# petrolReqStr = raw_input()

	testCases = "1"
	checkPoints = "2"
	costStr =      "7 2 2 3 1 3"
	petrolReqStr = "1 2 1 2 2 2"
	testCases = int(testCases)
	checkPoints = int(checkPoints)

	costList = []
	for i in costStr.split(' '):
		try:
			costList.append(int(i))
		except:
			None

	petrolReqList = []
	for i in petrolReqStr.split(' '):
		try:
			petrolReqList.append(int(i))
		except:
			None

	# costList = [int(i) ]
	# petrolReqList = [int(i) for i in petrolReqStr.split(' ')]
	# print testCases
	# print petrolReqList, costList
	
	
	totCost = 0
	for eachTest in range(testCases):
		while len(costList) > 0:
			minCost = min(costList)
			minIndex = costList.index(minCost)
			print minCost, minIndex
			for eachLen in petrolReqList[minIndex:]:
				totCost += minCost * eachLen
			print "totCost:", totCost
			costList = costList[:minIndex]
			petrolReqList = petrolReqList[:minIndex]
			print costList, petrolReqList 
		print totCost
	
if __name__ == "__main__":
	a = time.time()
	main()
	print time.time() - a