inputfile = open('../Homo_sapiens_assembly19.fasta')

#for i in range(4): inputfile.next() # skip first four lines
#for line in inputfile:
i = 0;
nlines = 40000
outputfile = open('test0.fasta','w')
for line in inputfile:
    i = i+1
    outputfile.writelines(line)
    if i%nlines == nlines-1:
       outputfile.close()
       outputfile = open('test{}.fasta'.format((i+1)/nlines), 'w')
    
inputfile.close()
