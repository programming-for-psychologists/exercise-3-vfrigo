import random
masked = ["masked", "masked", "nonmasked"]
sides = ["right", "left"]
trials = []
def generateTrials(blocks, numberBeforeBlockSwitch, numberRepetitions):
	for i in range(blocks):
		for m in masked:
			for side in sides:
				trials.append([str(i +1) + "," + str(m) +"," + str(side)])
	return(trials)

trials = generateTrials(5, 6, 4) 
random.shuffle(trials)

print trials