import numpy
import sys
sys.setrecursionlimit(9999)
def outLCS(backtrack,seq,i,j,str):
	if i == -1:
		return str
	if j == -1:
		return str
	if backtrack[i][j] == 1:
		
		return outLCS(backtrack,seq,i-1,j,str)
	elif backtrack[i][j] == 2:
		
		return outLCS(backtrack,seq,i,j-1,str)
	else:
		str =  seq[i]  + str
		return outLCS(backtrack,seq,i-1,j-1,str)


with open('rosalind_ba5c.txt') as f:
	z = 0
	for line in (line for line in f if line.rstrip('\n')):
		if z < 1:
			seq1 = line.rstrip('\n')
			z += 1
		else:
			seq2 = line.rstrip('\n')
	v = len(seq1)
	w = len(seq2)
	s = numpy.zeros((v,w))
	backtrack = numpy.zeros((v,w))
	for i in range(1,v):
		for j in range(1,w):
			a = s[i-1][j]
			b = s[i][j-1]
			if seq1[i] == seq2[j]:
				c = s[i-1][j-1] + 1
			else:
				c = -1
			arr = [a,b,c]
			s[i][j] = numpy.max(arr)
			if s[i][j] == s[i-1][j]:
				backtrack[i][j] = 1
				
			elif s[i][j] == s[i][j-1]:
				backtrack[i][j] = 2
				
			elif (s[i][j] == (s[i-1][j-1]+1) and seq1[i] == seq2[j]):
				backtrack[i][j] = 3
				
	final = outLCS(backtrack,seq1,v-1,w-1,"")
	
	
	print final		
	file = open("LCS_output.txt","w")
	file.write(final)
	file.close()
			

