import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

from generateRandomMatrix import generateRandomMatrix

for i in range(num1,num2):
  subdir = 'batch{0}'.format(i)
  generateRandomMatrix(subdir)
