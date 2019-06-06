# Set the input file name
# (The program must be run from within the directory 
# that contains this data file)
#InFileName = 'Marrus_claudanielis.txt'

#InFileName1 = input('Enter primary header file name: ')

#InFileName2 = input('Enter secondary header file name: ')

#InFileName3 = input('Enter tertiary header file name: ')

InFileName1 = "sample_18_metadata.txt"

InFileName2 = "sample_17_metadata.txt"

InFileName3 = "sample_19_metadata.txt"

# Open the input file for reading

InFile1 = open(InFileName1, 'r')

InFile2 = open(InFileName2, 'r')

InFile3 = open(InFileName3, 'r')

line1 = InFile1.readline()

line2 = InFile2.readline()

line3 = InFile3.readline()

ElementList1 = line1.split('\t')

ElementList2 = line2.split('\t')

ElementList3 = line3.split('\t')

for i in range(0,22):          

        if ElementList1[i] != ElementList2[i]:
               ElementList2.insert(i,'\t') # inserts tab
               print(i)

        if ElementList1[i] != ElementList3[i]:
               ElementList3.insert(i,'\t') # inserts tab
               print(i)

for i in range(0,22):
        print(ElementList2[i])

for i in range(0,22):
        print(ElementList3[i])

OutFileHeader_metadata_merge = "tsa_merged_sample_metadata.txt"
OutFile = open(OutFileHeader_metadata_merge,'w')

OutFile.write(line1)

InFile1.close()
InFile2.close()
InFile3.close()

InFile1 = open(InFileName1, 'r')

InFile2 = open(InFileName2, 'r')

InFile3 = open(InFileName3, 'r')

#line1 = InFile1.readline()

line2 = InFile2.readline()

#line3 = InFile3.readline()

for Line in InFile2:

        ListNext = Line.split('\t')

        for i in range(0,22):
                if ElementList2[i] == '\t':
                        ListNext.insert(i,'\t')

        for i in range(0,22):
                if ((ElementList2[i] != '\t') and (ListNext[i] != '\r\n')):
                        OutFile.write(ListNext[i]+ '\t')
                       
                else:
                        OutFile.write(ListNext[i])




for Line in InFile1:
        
        OutFile.write(Line)

for Line in InFile3:

        ListNext = Line.split('\t')

        for i in range(0,22):
                if ElementList3[i] == '\t':
                        ListNext.insert(i,'\t')

        for i in range(0,22):
                if ((ElementList3[i] != '\t') and (ListNext[i] != '\r\n')):
                        OutFile.write(ListNext[i]+ '\t')
                       
                else:
                        OutFile.write(ListNext[i])


InFile1.close()

InFile2.close()

InFile3.close()

OutFile.close()
