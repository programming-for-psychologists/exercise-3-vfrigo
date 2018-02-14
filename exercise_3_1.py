def repetition(letters, numberBeforeSwitch, numRepetitions):
	for i in range(numRepetitions):
		for l in letters:
			for j in range(numberBeforeSwitch):
				print l

repetition(['A','B'],1,1)
repetition(['A','B'],2,1)
repetition(['A','B'],2,2)
repetition(['A','B','C'],3,1)