import sys

wordcounter = 0
linecounter = 0
charactercounter = 0
sylcounter = 0
concounter = 0

for c in sys.stdin.read():
	if c == ' ': 
		wordcounter = wordcounter + 1
	if c == '\n':
		linecounter = linecounter + 1
	charactercounter = charactercounter + 1
	if c in 'aeiouáéíóúâêôãàõAEIOUÀÁÂÃÉÊÍÓÔÕÚÜ':
		sylcounter= sylcounter + 1
	if c in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM':
		concounter = concounter + 1
print(wordcounter)
print(linecounter)
print(charactercounter)
print(sylcounter)
print(concounter)