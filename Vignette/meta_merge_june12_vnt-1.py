

# Set the input file name
# (The program must be run from within the directory 
# that contains this data file)
#InFileName = 'Marrus_claudanielis.txt'

#InFileName1 = input('Enter primary header file name: ')

#InFileName2 = input('Enter secondary header file name: ')

#InFileName3 = input('Enter tertiary header file name: ')

InFileName1 = "sample_18_metadata_vnt.txt"

InFileName2 = "sample_17_metadata_vnt.txt"

InFileName3 = "sample_19_metadata_vnt.txt"

# Open the input file for reading

InFile1 = open(InFileName1, 'r')

InFile2 = open(InFileName2, 'r')

InFile3 = open(InFileName3, 'r')

line1 = InFile1.readline()

line2 = InFile2.readline()

line3 = InFile3.readline()

List1 = line1.split('\t')

List2 = line2.split('\t')

List3 = line3.split('\t')

for i in range(0,22):          

        if List1[i] != List2[i]:
               List2.insert(i,'zz') # inserts zz
#               print(i)

        if List1[i] != List3[i]:
               List3.insert(i,'zz') # inserts zz
#               print(i)

#for i in range(0,22):
#        print(List2[i])

#for i in range(0,22):
#        print(List3[i])

OutFileHeader_metadata_merge = "merged_sample_metadata_12_june_vnt.txt"
OutFile = open(OutFileHeader_metadata_merge,'w')

OutFile.write(line1)

# Combined header row is now complete
# Close and reopen 17, 18, and 19, and write to merged file


InFile1.close()
InFile2.close()
InFile3.close()

InFile1 = open(InFileName1, 'r')

InFile2 = open(InFileName2, 'r')

InFile3 = open(InFileName3, 'r')

line1 = InFile1.readline()

line2 = InFile2.readline()

line3 = InFile3.readline()

# Next, read in 5 rows of 17, and write to OutFile

for j in range(0,5):

        line2 = InFile2.readline()

#        print(line2)

        ListNext2 = line2.split('\t')

        for i in range(0,22):

                if(List2[i]=='zz'):

                        ListNext2.insert(i,'\t')

        for i in range(0,22):

                if((List2[i]!='zz')and(i!=21)):

                        OutFile.write(ListNext2[i]+'\t')

                if(List2[i]=='zz'):

                        OutFile.write(ListNext2[i])

                if(i==21):
                        OutFile.write(ListNext2[i])

#                print(i)
                
               

#        OutFile.write('\n')

#        print(ListNext2)

line_count = 0

for Line in InFile1:

        OutFile.write(Line)

        line_count = line_count + 1

#OutFile.write('\n')

for j in range(0,5):

        line3 = InFile3.readline()

        ListNext3 = line3.split('\t')

        for i in range(0,22):

                if(List3[i]=='zz'):

                        ListNext3.insert(i,'\t')

        for i in range(0,22):

                if((List3[i]!='zz')and(i!=21)):

                        OutFile.write(ListNext3[i]+'\t')

                if(List3[i]=='zz'):

                        OutFile.write(ListNext3[i])

                if(i==21):
                        OutFile.write(ListNext3[i])




InFile1.close()
InFile2.close()
InFile3.close()
OutFile.close()
