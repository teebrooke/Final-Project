# A.B.C (Always be Concatenating)

# Author: 
Taylor Alderete
Email: teebrooke@g.ucla.edu

# Introduction: 
This program is designed to take tables with large data sets that involve eDNA and concatenate them to form one large conclusive table. The tables included are Metadata and OTU and they will be concatenated independently from each other. Specifically for Metadata I will be using Sample 18 for the foundation of the header and following it with tabs for Sample 17 and 19. When file 17 gets read, a line is read and tehn the header of 17 is compared with 18 and where there is a mismatch due to no entry in 17, it inserts tabs. The same goes when comparing Sample 19 with Sample 18. Tabs are inserted where there is a mismatch. I have verified, by examining each line, that for the headers that do match up with 18, they have the same spelling and punctuation becasue that can give you a false mismatch. For the OTU data, I created a concatenated header that includes the headers from Sample 17, 18 and 19 all on one line. After the headers have been concatenated, I then satrted to feed in teh data from Sample 17 but 14 zeros must follow act as place holders so all the rows and columns. These place holders are important for Sample 18 and 19 as well.

# Purpose
The purpose of my project is to concatenate tables with a single header and single row, thus the tables will be concatenated with repsect to their titles, Metadata and OTU seperately. I do not want to include repeating headers. 

# Psuedocode: 
I will be taking two sets of three tables and all their common and uncommon header rows and using that as the foundation for the final concatenated table. For example, some of the uncommon headers among the three tables in Metadata include Time Collection. The final concatenated header row will include all of theses headers, even if the table does not have any data for it. The same goes for the final concatenated OTU table. 

# Program workflow

1. Import the tables and distinguish how many rows and columns there are in each table (Meatdata will be concatenated with Metadata and OTU with OTU).

2. Open the input file for reading

3. Now to concatentate the headers into one common header

4. Use Python to look through each charcter and line 

5. Use for loop for the ranges that need to include tabs 

6. After the loop is completed, close the file

# Dependencies
1. Python
2. A text editor like text wrangler to view invisible characters


# Steps

data_file_meta1 = pd.read_excel('sample_17_metadata.xlsx')

data_file_meta2 = pd.read_excel('sample_18_metadata.xlsx')

data_file_meta3 = pd.read_excel('sample_19_metadata.xlsx')



#Set the input file name

#(The program must be run from within the directory 
#that contains this data file)

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
        
# Now to concatentate the headers into one common header

OutFileHeader_metadata_merge = "tsa_merged_sample_metadata.txt"

OutFile = open(OutFileHeader_metadata_merge,'w')

OutFile.write(line1)

# After the loop is completed, close the file

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
                        
# After the loop is completed, close the file

InFile1.close()

InFile2.close()

InFile3.close()

OutFile.close()

  
# Next we will work with the OTU data

data_file_OTU1 = pd.read_excel('sample_17_OTUtable.xlsx')

data_file_OTU2 = pd.read_excel('sample_18_OTUtable.xlsx')

data_file_OTU3 = pd.read_excel('sample_19_OTUtable.xlsx')

# Set input file name

InFileName1 = "sample_17_OTUtable.txt"

InFileName2 = "sample_18_OTUtable.txt"

InFileName3 = "sample_19_OTUtable.txt"

# Open the input file for reading

OutFile_OTU_merge = "OTU_3_tables_merged.txt"

OutFile = open(OutFile_OTU_merge,'w')

InFile1 = open(InFileName1, 'r')

InFile2 = open(InFileName2, 'r')

InFile3 = open(InFileName3, 'r')

header1 = InFile1.readline()

header2 = InFile2.readline()

header3 = InFile3.readline()

# Now to concatentate the headers into one common header

headerList1 = header1.split('\t')

headerList2 = header2.split('\t')

headerList3 = header3.split('\t')

# Loop through each line in the file 

for i in range(0,15):

    print(headerList1[i])

for i in range(0,15):

    OutFile.write(headerList1[i]+'\t')

for i in range(1,15):

    OutFile.write(headerList2[i]+'\t')

for i in range(1,15):   

    OutFile.write(headerList3[i]+'\t')

OutFile.write(headerList3[15])

for i in range(0,650):

    line1 = InFile1.readline()

    lineList1 = line1.split('\t')

    lineList1[0] = lineList1[0] + '_17'

    for i in range(15,44):

        lineList1.insert(i,'0')

    for i in range(0,43):

        OutFile.write(lineList1[i]+'\t')            

    OutFile.write(lineList1[44])

for i in range(0,361):

    line2 = InFile2.readline()

    lineList2 = line2.split('\t')

    lineList2[0] = lineList2[0] + '_18'

    for i in range(1,15):

        lineList2.insert(i,'0')

    for i in range(29,44):

        lineList2.insert(i,'0')

    for i in range(0,43):

        OutFile.write(lineList2[i]+'\t')

    OutFile.write(lineList2[44]) 
    
# After the loop is completed, close the file

InFile1.close()

InFile2.close()

InFile3.close()

OutFile.close()




# After the loop is completed, close the file
InFile4.close ()
  
# Next we will work with sample_18_OTUtable.xlsx and sample_19_OTUtable.xlsx and completely ignore the header row.
 
#!/usr/bin/env python

# Set the input file name 
InFileName5 = sample_18_OTUtable.xlsx
# Open the input file for reading
InFile5 = open(InFileName5, 'sample_18_OTUtable.xlsx')
# Initialize the counter used to keep track of lines
LineNumber = 0

# Loop through each line in the file 
for Line in InFile5:
  if LineNumber > 0:
    # Remove the line ending characters
    Line = Line.strip('\n')
    # Print the line
    print LineNumber, ":", Line 
  LineNumber = LineNumber + 1  ????????
  
# After the loop is completed, close the file
InFile5.close ()


#!/usr/bin/env python

# Set the input file name 
InFileName6 = sample_19_OTUtable.xlsx
# Open the input file for reading
InFile6 = open(InFileName6, 'sample_19_OTUtable.xlsx')
# Initialize the counter used to keep track of lines
LineNumber = 0

# Loop through each line in the file 
for Line in InFile6:
  if LineNumber > 0:
    # Remove the line ending characters
    Line = Line.strip('\n')  ????????????????
    # Print the line
    print LineNumber, ":", Line 
  LineNumber = LineNumber + 1  ????????
  
# After the loop is completed, close the file

InFile6.close ()
 
# References:
Python
Text Wrangler
  
