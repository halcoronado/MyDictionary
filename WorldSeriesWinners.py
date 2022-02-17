###The first line in the file is the name of the team that won in 1903,
# and the last line is the name of the team that won in 2009. 
##(Note the World Series was not played in 1904 or 1994. There are entries in the file indicating this.) 
##Write a program that reads this file and creates a dictionary in which the keys are the names of the teams, 
##and each key’s associated value is the number of times the team has won the World Series. 

infile = open("WorldSeriesWinners.txt",'r')
''''
winners = []
count = 1
for x in infile:
    x = x.rstrip('\n')
    if x not in winners:
        winners+=[x,count]
    else:
        count +=1 
        
        
print (winners)
'''
#Create another dictionary in which the keys are the years, 
# and each key’s associated value is the name of the team that won that year.
##The program should prompt the user for a year in the range of 1903 through 2009. 
##It should then display the name of the team that won the World Series that year, 
# and the number of times that team has won the World Series.

def main():
    win_yrs = {}
    line = infile.readline().rstrip('\n')

    make_dict()
    year = int(input('enter a year bro'))

def make_dict(win_yrs):
    
    for x in range (1903,2008):
        if x != 1904 or x != 1994:
            win_yrs[x]= line
            print(win_yrs)
    return 

    
main()