
infile = open("WorldSeriesWinners.txt",'r')

winners = []

for x in infile:
    x = x.rstrip('\n')
    winners.append(x)
wincount={}
for x in winners:
    counter = winners.count(x)
    wincount[x]= counter

for key in list(wincount.keys()):
    print(key, ":",wincount[key], sep = '')

yearlist = []
win_years= {}
for x in range (1903,2009):
    if x == 1904:
        continue
    elif x == 1994:
        continue
    else:
        yearlist.append(x)

for key in yearlist:
    for value in winners:
        win_years[key] = value
        winners.remove(value)
        break  
for key in list(win_years.keys()):
 print(key, ":",win_years[key], sep = '')

quest = int(input('Enter year from 1903-2008: '))
if quest in win_years:
    print(win_years[quest])
else:
    print('No record of World Series')