import random
maskedCond = ["masked", "masked", "nonmasked"]
sides = ["right", "left"]

def repetition(mask,side):
	trials = []
	for masks in mask:
		for sides in side:
			trials.append([masks,sides])
	return trials 


numTrials=range(5)
for i in numTrials:
	trials = repetition(maskedCond, sides)
	random.shuffle(trials)
	for trial in trials:
		print ','.join((str(i+1), str(trial[0]), trial[1]))
                             
