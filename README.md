# Merging Microbiome Data Tables
# Author: Taylor Alderete
# Overview: Living organisms are continuously moving throughout their environment, shedding DNA as they travel. This DNA is collected by scientists and has been used to discover rare or invasive species as well as new pathogens in a variety of environments. The PUMA Project focuses on microbiome data and anaysis, for example the production of the 16S rRNA gene. The goal for their Project is to allow researchers to analyse their microbiome data without the use of command-line interface or R/Python scripting.

# Backbone:
# The purpose of my project is to merge tables with a single header and single row, thus the tables will be stacked on top of one another. I do not want to include repeating headers. For users, make sure that you have the same number of dimension of tables before using this program.

# Psuedocode: I will be taking three files and all their common and uncommon header rows and using that as the foundation for the final concatenated table. For example, some of the uncommon headers among the three tables in Metadata include, pH meter CALeDNA, Amount of Leaf Litter, Time Collection, pH Litmus Strip. The final concatenated header row will include all of theses headers, even if the table does not have any data for it. The same goes for the final concatenated OTU table. 

# First step will be to input file values such as, number of rows and columns and file type (Metadata with Mestadata, OTU with OTU).

data_file_meta1 = pd.read_excel('sample_17_metadata.xlsx')
data_file_meta2 = pd.read_excel('sample_18_metadata.xlsx')
data_file_meta3 = pd.read_excel('sample_19_metadata.xlsx')
data_file_OTU1 = pd.read_excel('sample_17_OTUtable.xlsx')
data_file_OTU2 = pd.read_excel('sample_18_OTUtable.xlsx')
data_file_OTU3 = pd.read_excel('sample_19_OTUtable.xlsx')

# Secondly, create a common header row that includes all common and uncommon headers from the three tables respectively. For the common header row we need to store variables to indicate which columns are common and which entries are going to be blank because they need to follow under uncoomon headers.

# THE FOLLWOING IS FOR METADATA ONLY

#!/usr/bin/env python

# Set the input file name
InFileName = sample_17_metadata.xlsx

# Open the input file for reading
InFile = open(InFileName 'sample_17_metadata.xlsx')

# Initialize the counter used to keep track of line numbers 
Linenumber = 0

# Loop through each line in the file    ????????????????????????
for Line in Infile:
  if Linenumber > 0:
    #Remove the line ending characters
    Line = Line.strip('\n')   >?????????????????
    #Print the line
    print Linenumber, ":", Line  ??????????????
   Linenumber = Linenumber + 1  ?????????????
   
# After the loop is completed, close the file
InFile.close()

# Next, we will be taking each element in each column and will feed it over to the combined header row. Again, we will do that with table two and table three, concatenating them below one another.

#!/usr/bin/env python

# Set the input file name
InFileName2 = sample_18_metadata.xlsx

# Open the input file for reading
InFile2 = open(InFileName2 'sample_18_metadata.xlsx')

# Intialize the counter used to keep track of line number 
Linenumber = ? (i think 1 but not sure)

# Loop through each line in hte file   ?????????????????????????
for Line in Infile2:
  if Linenumber > 1:?????
    #Remove the line ending characters
    Line = Line.strip('\n')   >?????????????????
    #Print the line
    print Linenumber, ":", Line  ??????????????
   Linenumber = Linenumber + 1  ?????????????
   
# After the loop is completed, close the file
InFile2.close()


#!/usr/bin/env python

# Set the input file name
InFileName3 = sample_19_metadata.xlsx

# Open the input file for reading
InFile3 = open(InFileName3 'sample_19_metadata.xlsx')

# Intialize the counter used to keep track of line number 
Linenumber = ? (i think 1 but not sure)

# Loop through each line in hte file   ?????????????????????????
for Line in Infile3:
  if Linenumber > 1:?????
    #Remove the line ending characters
    Line = Line.strip('\n')   >?????????????????
    #Print the line
    print Linenumber, ":", Line  ??????????????
   Linenumber = Linenumber + 1  ?????????????
   
# After the loop is completed, close the file
InFile3.close()
   
 
# THE FOLLOWING IS FOR OTU ONLY

#!/usr/bin/env python

# Set the input file name
InFileName4 = sample_17_OTUtable.xlsx

# Open the input file for reading
InFile4 = open(InFileName4 'sample_17_OTUtable.xlsx')

# Initialize the counter used to keep track of line numbers 
Linenumber = 0

# Loop through each line in the file ???????????????????????????????
for Line in Infile4:
  if Linenumber >= 0:
    #Remove the line ending characters
    Line = Line.strip('\n')   >?????????????????
    #Print the line
    print Linenumber, ":", Line  ??????????????
   Linenumber = Linenumber + 1  ?????????????
   
# After the loop is completed, close the file
InFile4.close()


#!/usr/bin/env python

# Set the input file name
InFileName4 = sample_18_OTUtable.xlsx

# Open the input file for reading
InFile5 = open(InFileName4 'sample_18_OTUtable.xlsx')

# Initialize the counter used to keep track of line numbers 
Linenumber = 0

# Loop through each line in the file ???????????????????????????????
for Line in Infile5:
  if Linenumber > 0:
    #Remove the line ending characters
    Line = Line.strip('\n')  /?????????????
    #Print the line
    print Linenumber, ":", Line  ???????????
   Linenumber = Linenumber + 1  ?????????????
   
# After the loop is completed, close the file
InFile5.close()


#!/usr/bin/env python

# Set the input file name
InFileName6 = sample_19_OTUtable.xlsx

# Open the input file for reading
InFile6 = open(InFileName6 'sample_19_OTUtable.xlsx')

# Initialize the counter used to keep track of line numbers 
Linenumber = 0

# Loop through each line in the file ???????????????????????????????
for Line in Infile6:
  if Linenumber > 0:
    #Remove the line ending characters
    Line = Line.strip('\n')
    #Print the line
    print Linenumber, ":", Line ??????????????
   Linenumber = Linenumber + 1 ????????????
   
# After the loop is completed, close the file
InFile6.close()
   

# Lastly, This common file will have this first header row and the concatenated process will have to to ignore the repeating header rows. 








