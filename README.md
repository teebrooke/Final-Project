# Merging Microbiome Data Tables
# Author: Taylor Alderete
# Email: teebrooke@g.ucla.edu
# Introduction: Living organisms are continuously moving throughout their environment, shedding DNA as they travel. This DNA is collected by scientists and has been used to discover rare or invasive species as well as new pathogens in a variety of environments. The PUMA Project focuses on microbiome data and anaysis, for example the production of the 16S rRNA gene. The goal for their Project is to allow researchers to analyse their microbiome data without the use of command-line interface or R/Python scripting.

# Backbone:
# The purpose of my project is to merge tables with a single header and single row, thus the tables will be concatenated with repsect to their titles, Metadata and OTU seperately. I do not want to include repeating headers. For users, make sure that you have the same number of dimension of tables before using this program.

# Psuedocode: I will be taking three files and all their common and uncommon header rows and using that as the foundation for the final concatenated table. For example, some of the uncommon headers among the three tables in Metadata include Time Collection. The final concatenated header row will include all of theses headers, even if the table does not have any data for it. The same goes for the final concatenated OTU table. 

# First step will be to import the tables and distinguish how many rows and columns there are in each table (Meatdata will be concatenated with Metadata and OTU with OTU).

data_file_meta1 = pd.read_excel('sample_17_metadata.xlsx')
data_file_meta2 = pd.read_excel('sample_18_metadata.xlsx')
data_file_meta3 = pd.read_excel('sample_19_metadata.xlsx')

# Next we will take a look at the Metadata tables to determine a concatenated header row with common and uncommon headers (common headers are included in all and uncommon headers are only present on some tables)

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
  
# Next we will work with the OTU data

data_file_OTU1 = pd.read_excel('sample_17_OTUtable.xlsx')
data_file_OTU2 = pd.read_excel('sample_18_OTUtable.xlsx')
data_file_OTU3 = pd.read_excel('sample_19_OTUtable.xlsx')

#!/usr/bin/env python

# Set the input file name 
InFileName4 = sample_17_OTUtable.xlsx
# Open the input file for reading
InFile4 = open(InFileName4, 'sample_17_OTUtable.xlsx')
# Initialize the counter used to keep track of lines
LineNumber = 0

# Loop through each line in the file 
for Line in InFile4:
  if LineNumber >= 0:
    # Remove the line ending characters
    Line = Line.strip('\n')  ????????????????
    # Print the line
    print LineNumber, ":", Line 
  LineNumber = LineNumber + 1  ????????
  
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
 
 
 
  
