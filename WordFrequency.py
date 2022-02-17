###The program should create a dictionary in which the 
#keys are the individual words found in the file and the values are the number of times each word appears. 
##For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
##The program should display the frequency of each word.

infile = open('AI.txt','r')
SC = [ ',' , '.' , '”' , '’' , '"' , "'"  , '?' , '!' , '&', '@', '*' , '#', ')','(', '%' ]
SC=str(SC)
words = infile.readline()
words = words.lower()
for x in SC:
  words = words.replace(x,' ')
words = words.split()

wordlist = []
for i in words:
  wordlist.append(i)
  

word_dict= {}
for n in wordlist:
  counter = wordlist.count(n)
  word_dict[n] = {counter}

for key in list(word_dict.keys()):
  print(key, ":",word_dict[key], sep = '')


infile.close()
