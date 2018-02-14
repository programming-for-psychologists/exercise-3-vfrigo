masked = ["masked", "masked", "nonmasked"]
sides = ["right", "left"]
def generateTrials(blocks, numberBeforeBlockSwitch, numberRepetitions):
	for i in range(blocks):
		for m in masked:
			for side in sides:
				print str(i +1) + "," + str(m) +"," + str(side)

generateTrials(5, 6, 4)