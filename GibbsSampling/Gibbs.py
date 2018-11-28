import random
import numpy
def generate_kmer(Profile, DNA, k):
	numMers = len(DNA) - k +1
	mers = [""]*numMers
	probabilities = [0]*numMers
	for i in range(0,numMers-1):
		end = i + k 
		kmer = DNA[i:end]
		mers[i] = kmer
		pbegin = 1
		for j in range(0,k):
			if(kmer[j] == "A"):
				pbegin = pbegin * Profile[0][j]
			elif(kmer[j] == "C"):
				pbegin = pbegin * Profile[1][j]
			elif(kmer[j] == "G"):
				pbegin = pbegin * Profile[2][j]
			elif(kmer[j] == "T"):
				pbegin = pbegin * Profile[3][j]
		probabilities[i] = pbegin
	s = sum(probabilities)
	for i in range(0,numMers):
		probabilities[i] = probabilities[i]/s
	
	prob2 = numpy.array(probabilities, dtype=float)
	
	return_mer = numpy.random.choice(mers,size =None, replace = True, p = prob2)
	
	return return_mer

def score(Motifs):
	score = 0
	k = len(Motifs[1])
	
	t = len(Motifs)

	for i in range(0,k):
		counts = [0]*4
		for j in range(0,t):
			if(Motifs[j][i] == "A"):
				counts[0] = counts[0] + 1
			elif(Motifs[j][i] == "C"):
				counts[1] = counts[1] + 1
			elif(Motifs[j][i] == "G"):
				counts[2] = counts[2] + 1
			elif(Motifs[j][i] == "T"):
				counts[3] = counts[3] + 1
		score = score + (t - max(counts))	
	return score

def make_profile(Motifs):
	k = len(Motifs[1])
	
	t = len(Motifs)
	
	h = 1.0 / (t+4)

	profile = [[h]*(k) for i in range(0,4)]	
	for i in range(0,k):
		for j in range(0,t):
			if(Motifs[j][i] == "A"):
			 	profile[0][i] = profile[0][i]+h
			elif(Motifs[j][i] == "C"):
			 	profile[1][i] = profile[1][i]+h
			elif(Motifs[j][i] == "G"):
			 	profile[2][i] = profile[2][i]+h
			elif(Motifs[j][i] == "T"):
			 	profile[3][i] = profile[3][i]+h

	return profile
with open('rosalind_ba2g.txt') as f:
	z = 0
	k = 0
	t = 0
	N = 0
	lines = f.readlines()
	for i in range(0,len(lines)):
		lines[i] = lines[i].rstrip('\n')
	x = lines[0].split(" ")
	k = int(x[0])
	t = int(x[1])
	N = int(x[2])
	Motifs = [""]*t
	finalMotifs = [""]*t
	BestMotifs = [""]*t

	numMers = len(lines[1]) - k + 1
	scoreOut = 9999999999
	
	for y in range(0,20):
		for i in range(1,t+1):
			z = random.randint(0,numMers-1)
			Motifs[i-1] = lines[i][z:(z+k)]
		for i in range(0,len(Motifs)):
			BestMotifs[i] = Motifs[i]
		
		for j in range(0,N):

			i = random.randint(0,t-1)
			profile_motifs = [""]*(t-1)
			index = 0
			for h in range(0,t):
				if(h != i):
					profile_motifs[index] = Motifs[h]
					index = index + 1
			profile = make_profile(profile_motifs)
			
			Motifs[i] = generate_kmer(profile, lines[i+1],k)
			
			if(score(Motifs) < score(BestMotifs)):
				for i in range(0,len(Motifs)):
					BestMotifs[i] = Motifs[i]
				if(score(BestMotifs) < scoreOut):
					scoreOut = score(BestMotifs)
					for i in range(0,len(BestMotifs)):
						finalMotifs[i] = BestMotifs[i]
					
	for i in range(0,len(finalMotifs)):
		print(finalMotifs[i])


