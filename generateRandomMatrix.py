def getBase(base):
  from random import randint
  options = 'ACGT'
  remnants = ''
  for i in range(0,4):
    if options[i] != base:
      remnants += options[i]    
  alt = remnants[randint(0,2)]
  return alt


def generateRandomMatrix(directory):
  import numpy as np
  import math
  import os
  outputfile = open('output/test_{0}.txt'.format(directory),'w')
  nMuthPerFile, nColumn = 4, 130

  for filename in os.listdir('input/{0}'.format(directory)):
#  for filename in os.listdir('{0}'.format(directory)):

    randMatrix = np.random.random((nMuthPerFile, nColumn))
    inputfile = open('input/{0}/{1}'.format(directory,filename))
   # inputfile = open('{0}/{1}'.format(directory,filename))
    count = 0

    base = None
    prime5 = None
    prime3 = None
    linetemp = None

    for i, line in enumerate(inputfile):
      if prime3 == "X":
        alt = getBase(base)
        outputfile.writelines('{0}{1}{2}\t{1}\t{3}'.format(prime5, base, line[0], alt))
      else:
        prime3 = None
      
      if len(line) >= 82:
       print(len(line))
       continue
      
      for j in range(0, nMuthPerFile):
        for k in range (0, nColumn):

          value = int(80*40000*randMatrix[j, k])
          characterNum = value%(80)
          lineNum = int(value/40000) 

          if i == 0 and characterNum == 0:
            continue
          
          if i == lineNum:
            count+=1

            if(characterNum < len(line)):
              base = line[characterNum]
              if characterNum == 0:
                prime5 = linetemp[len(linetemp)-2]
              else:
                prime5 = line[characterNum-1]
              if characterNum < 79:
                prime3 = line[characterNum+1]
                alt = getBase(base)
                outputfile.writelines('{0}{1}{2}\t{1}\t{3}\n'.format(prime5, base, prime3, alt))
              else:
                prime3 = "X"
            
            
            
            if count == 521:
              break
      linetemp = line
      
    inputfile.close()
  outputfile.close()

