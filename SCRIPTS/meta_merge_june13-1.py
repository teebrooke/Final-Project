

# Set the input file name
# (The program must be run from within the directory 
# that contains this data file)


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

List1 = line1.split('\t')

List2 = line2.split('\t')

List3 = line3.split('\t')

for i in range(0,22):          
    # find and store header mismatches for sample_17 file
        if List1[i] != List2[i]:
               List2.insert(i,'zz') # inserts zz
#               print(i)   (diagnostic)

    # find and store header mismatches for sample_18 file

        if List1[i] != List3[i]:
               List3.insert(i,'zz') # inserts zz
#               print(i)



OutFileHeader_metadata_merge = "merged_sample_metadata_12_june.txt"
OutFile = open(OutFileHeader_metadata_merge,'w')

# File sample_18 contains the complete header that files 17 and 19 must conform to
# Write the complete header to the output file

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

# Next, read in 14 rows of 17, and write to OutFile

for j in range(0,14):

        line2 = InFile2.readline()

#        print(line2)

        ListNext2 = line2.split('\t')   # create list from file 17 readlilne (tab-delimited)

        for i in range(0,22):

                if(List2[i]=='zz'):    #use zz as pointer to 'missing' data and insert tab

                        ListNext2.insert(i,'\t')

        for i in range(0,22):

                if((List2[i]!='zz')and(i!=21)):

                        OutFile.write(ListNext2[i]+'\t')  # write 'normal' data plus tab

                if(List2[i]=='zz'):

                        OutFile.write(ListNext2[i])   # write 'missing' data tab

                if(i==21):
                        OutFile.write(ListNext2[i])  # write line feed

#                print(i)    diagnostic
                
               

OutFile.write('\n')   # write line feed for end of file 17

#        print(ListNext2)  diagnostic

line_count = 0

for Line in InFile1:

        OutFile.write(Line)

        line_count = line_count + 1

OutFile.write('\n')  # line feed for end of file 18

for j in range(0,14):  # file 19 code has identical structure and comments as file 17 code

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
