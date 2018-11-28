with open('rosalind_ba9j.txt') as f:
#with open('BW_IN.txt') as f:
#with open('input.txt') as f:
	for line in (line for line in f if line.rstrip('\n')):
		text = line.rstrip('\n')
	n = len(text)
	lex = ''.join(sorted(text))
	num1 = set(lex)
	uniq = list(num1)
	z = len(uniq)
	m = n - 1
	mat = [""]*n
	for i in range(0,n):
		mat[i] += lex[i]
		mat[i] += ','
		for j in range(1,m):
			mat[i] += '?,'
		mat[i] += text[i]
		mat[i] = str.split(mat[i],',')
	for j in range(0,z):
		char = uniq[j]
		cnt1 = 1
		cnt2 = 1
		for i in range(0,n):
			if (mat[i][0] ==char):
				mat[i][0] = mat[i][0]+str(cnt1)
				cnt1 = cnt1 +1
			if(mat[i][m]==char):
				mat[i][m] = mat[i][m]+str(cnt2)
				cnt2 = cnt2 +1
	for i in range(0,n):
		print(mat[i][0]),
		print(mat[i][m])
	final = ""
	start = "$1"
	end = ""
	while (start != end):
		end = "$1"
		for i in range(0,n):
			if(mat[i][m] == start):
				start = mat[i][0]
				final += start
				break
						
	final = ''.join(i for i in final if not i.isdigit())
	print final		
	file = open("output.txt","w")
	file.write(final)
	file.close()
	#print final
	
		
	

