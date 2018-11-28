
import random
def findPath(start,graph,tour):
	stack = [start]
	while(stack):
		curr = stack[-1]
		if graph[curr]:
			next = graph[curr][0]
			stack.append(next)
			del graph[curr][0]
		else:
			tour.append(stack.pop())
	return tour
with open('rosalind_ba3f.txt') as f:
	graph = {}
	for line in (line for line in f if line.rstrip('\n')):
			text = line.rstrip('\n')
			text = text.replace(" -> ",",")
			array = text.split(",")
			n = len(array) 
			graph[array[0]] = array[1:n]
	start = str(random.randrange(0,len(graph),1))
	tour = findPath(start,graph,[])
	result = ""
	n = len(tour)-1
	for i in range(n,0,-1):
		result = result + tour[i]
		result = result + "->"	
	result = result + tour[0]
	file = open("output.txt","w")
	file.write(result)
	file.close()
			