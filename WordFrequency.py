###The program should create a dictionary in which the 
#keys are the individual words found in the file and the values are the number of times each word appears. 
##For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
##The program should display the frequency of each word.

infile = open('AI.txt','r')
SC = [ ',' , '.' , '”' , '’' , '"' , "'"  , '?' , '!' , '&', '@', '*' , '#' ]
SC=str(SC)

words = ''
for x in infile:
  words += ' ' 
  words += infile.read()
words = words.lower()
for x in SC:
  words = words.replace(x,'')
print (words)
  

infile.close()
