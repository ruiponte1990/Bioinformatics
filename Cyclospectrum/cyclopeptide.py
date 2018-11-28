import copy

def expand(peptides,masses):

	m = len(masses)
	n = len(peptides)
	newPeptides = []
	for i in range(0,n):
		for j in range(0,m):
			newPep = copy.deepcopy(peptides[i])
			newPep.append(masses[j])
			newPeptides.append(newPep)
			
	
	return newPeptides
	

def process(peptide):

	val = ""
	n = len(peptide)
	m = n-1
	for i in range(1,m):
		val = val + str(peptide[i])
		val = val + "-"

	val = val + str(peptide[m])
	
	return val

def prefixMass(peptide):
	mass = [0]
	n = len(peptide)
	for i in range(0,n):
		mass.append(mass[i]+peptide[i])
	return mass


def cyclospectrum(peptide):
	
	mass = prefixMass(peptide)
	spectrum = [0]
	n = len(peptide)
	for i in range(0,n):
		for j in range(i+1,n):
			val1 = spectrum.append(mass[j]-mass[i])
			if val1 > 0:
				#print val1
				spectrum.append(val1)
			if (i > 0 and j < n):
				val = mass[n]-(mass[j]-mass[i])
				if val > 0:
					#print val
					spectrum.append(val)

	l = list(set(spectrum))
	l.sort()
	l.remove(0)
	return l


def checkSpectrum(peptide,spectrum):

	val =  sum(peptide) in spectrum
	return val
	
	

	




#with open('pepIn.txt') as f:
with open('rosalind_ba4e.txt') as f:
#with open('peptide_test.txt') as f:
	for line in (line for line in f if line.rstrip('\n')):
		text = line.rstrip('\n')
		spectrum = map(int,text.split(" "))
		n = len(spectrum) 
	parentmass = int(spectrum[n-1])
	spectrum2 = copy.deepcopy(spectrum)
	spectrum2.remove(parentmass)
	peptides = [[0]]
	peptides2 = []
	masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	i = 0
	while i < len(masses):
		if masses[i] not in spectrum:
			masses.pop(i)
			i = i - 1
		i = i + 1
	print(masses)
	while peptides:
		peptides = expand(peptides,masses)
		i = 0
		while i < len(peptides):
			if sum(peptides[i]) == parentmass:
				l = list(set(spectrum2))
				l.remove(0)
				l.sort()
				print("spectrum2"),
				print l
				print("cyclospectrum"),
				print cyclospectrum(peptides[i])
				
				if cyclospectrum(peptides[i]) == l: 
					peptides2.append(peptides[i])
				peptides.pop(i)
				i = i -1
			elif checkSpectrum(peptides[i],spectrum) != True: 
				peptides.pop(i) 
				i = i - 1
			i = i + 1
	result = ""
	peptides2.sort(reverse = True)
	print(peptides2)
	n = len(peptides2) - 1 
	for i in range(0,n):
		result = result + process(peptides2[i])
		result = result + " "	
	result = result + process(peptides2[n])
	print "result: "
	print result
	file = open("output.txt","w")
	file.write(result)
	file.close()