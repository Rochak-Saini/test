from __future__ import print_function
import sys

mostFreq = []
currentMax = -1

for line in sys.stdin:
	count, word = line.strip().split('\t',1)
	count = int(count)
	if count > currentMax:
		currentMax = count
		mostFreq = [word]
	elif count == currentMax:
		mostFreq.append(word)

for word in mostFreq:
	print('%s\t%s' % (word,currentMax))





echo "foo foo foo labs labs labs quux labs foo bar quux" | python3 
freqmap1.py |sort|python3 freqred1.py 
echo "foo foo foo labs labs labs quux labs foo bar quux" | 
python3 freqmap1.py |sort|python3 freqred1.py|python3 freqmap2.py
echo "foo foo foo labs labs labs quux labs foo bar quux" | 
python3 freqmap1.py |sort|python3 freqred1.py|python3 freqmap2.py|sort 
echo "foo foo foo labs labs labs quux labs foo bar quux" | 
python3 freqmap1.py |sort|python3 freqred1.py|python3 freqmap2.py|sort|python3 
freqred2.py
