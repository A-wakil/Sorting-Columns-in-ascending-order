letters = 'abcdefghijklmnopqrstuvwxyz'
alphadict= {letters[i] : i for i in range(26)}


mygrid = ['geh',
        'kbs',
        'yeo']
for i in range(len(mygrid)):
  mygrid[i] = list(mygrid[i])
  mygrid[i].sort()
  mygrid[i]= "".join(mygrid[i])
for i in mygrid:
  print(i)
def isColumnSorted(grid,column):
  for i in range(1,len(grid)):
    if alphadict[grid[i][column]] < alphadict[grid[i-1][column]]:
      return False
  return True
for i in range(len(mygrid)):
  if not isColumnSorted(mygrid,i):
    print("Column {} is not sorted".format(i+1))

    
    
