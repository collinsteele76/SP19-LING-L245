#based on how many other python commands have 'import sys'
import sys

vocab = [] #vocab is a list of valid word forms

#'r' to read file opened line by line
f = open('freq.txt', 'r')

for line in f.readlines(): 
	line = line.strip('\n ')
	# the form is the line without spacing
	(f, w) = line.split('\t')
	vocab.append(w)

for line in sys.stdin.readlines(): #line is a line from the input
	w = line.split(' ') #w is list of tokens
	for token in w : 
		if token not in vocab :
			sys.stdout.write('*'+token+' ')
		else :
			sys.stdout.write(token+' ')
