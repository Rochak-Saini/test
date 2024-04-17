from operator import itemgetter 
import sys 
 
current_word = None 
current_count = 0 
word = None 
  
for line in sys.stdin: 
  
	line = line.strip() 
  
	word, count = line.split('\t', 1) 
  
	try: 
 
		count = int(count) 
 
	except ValueError: 
 
		continue 
 
	if current_word == word: 
		current_count += count 
	else: 
 
		if current_word: 
  
			print ('%s\t%s' % (current_word, current_count))	 
		current_count = count 
		current_word = word 
 
 
if current_word == word: 
 
	print ('%s\t%s' % (current_word, current_count))



echo "a a a a v v f f hh hh fg tg fg gt nnn ccc ddd nnn ddd"|python3 mapper.py
echo "a a a a v v f f hh hh fg tg fg gt nnn ccc ddd nnn ddd"|python3 
mapper.py|python3 reducer.py 
echo "a a a a v v f f hh hh fg tg fg gt nnn ccc ddd nnn ddd"|python3 
mapper.py|sort|python3 reducer.py 