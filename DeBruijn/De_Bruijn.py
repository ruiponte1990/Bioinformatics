def suffix(kmer):
	k = len(kmer)
	return kmer[1:(k)]
def prefix(kmer):
	k = len(kmer)
	return kmer[0:(k-1)]
def mergeNodes(matrix):
	n = len(matrix)
	i = 0
	while(i < n):
		j = i + 1
		while (j < n):
			if(matrix[i][0] == matrix[j][0]):
				matrix[j].pop(0)
				matrix[i].extend(matrix[j])
				vertex = matrix[i][0]
				matrix[i].pop(0)
				matrix[i].sort()
				matrix[i].insert(0,vertex)
				matrix.pop(j)
				n = len(matrix)
			j = j + 1
		i = i + 1

	return matrix	

with open('rosalind_ba3d.txt') as f:
#with open('test.txt') as f:
	z = 0
	for line in (line for line in f if line.rstrip('\n')):
		if z < 1:
			k = int(line.rstrip('\n'))			
			
			z += 1
		else:
			text = line.rstrip('\n')

	numMers = len(text) - k + 1
	kmers = [""]*numMers
	for i in range(0,numMers):
		mer = text[i:(i+k)]
		kmers[i] = mer

	matrix = []	
	for i in range(0,numMers):
		matrix.append([])
		matrix[i].append(prefix(kmers[i]))
		matrix[i].append(suffix(kmers[i]))
	newMatrix = mergeNodes(matrix)
	#newMatrix = matrix
	f = len(newMatrix)
	matrix.sort()
	for i in range(0,f):
		n = len(newMatrix[i])-1
		print(newMatrix[i][0] + "->"), #add arrow
		for j in range(1,n):
			print(newMatrix[i][j] + ","), # add comma
		print(newMatrix[i][n])
