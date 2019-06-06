# A.B.C (Always be Concatenating)

# Author: 
Taylor Alderete

Email: teebrooke@g.ucla.edu

# Introduction: 
This program is designed to take tables with large data sets that involve eDNA and taxonomy and concatenate them to form one large conclusive table. The tables included are Metadata and OTU and they will be concatenated independently from each other. Specifically for Metadata I will be using Sample 18 for the foundation of the header and following it with tabs for Sample 17 and 19. When file 17 gets read, a line is read and tehn the header of 17 is compared with 18 and where there is a mismatch due to no entry in 17, it inserts tabs. The same goes when comparing Sample 19 with Sample 18. Tabs are inserted where there is a mismatch. I have verified, by examining each line, that for the headers that do match up with 18, they have the same spelling and punctuation becasue that can give you a false mismatch. For the OTU data, I created a concatenated header that includes the headers from Sample 17, 18 and 19 all on one line. After the headers have been concatenated, I then satrted to feed in teh data from Sample 17 but 14 zeros must follow act as place holders so all the rows and columns. These place holders are important for Sample 18 and 19 as well.

# Purpose
The purpose of my project is to concatenate tables with a single header and single row, thus the final tables will be concatenated with repsect to their titles, Metadata and OTU seperately. I do not want to include repeating headers. 


# Program workflow

1. Import the tables and distinguish how many rows and columns there are in each table (Meatdata will be concatenated with Metadata and OTU with OTU).

2. Set input file name

3. Open the input file for reading

4. Now to concatentate the headers into one common header

5. Use Python to look through each charcter and line 

6. Use for loop for the ranges that need to include tabs 

7. After the loop is completed, close the file

# Dependencies
1. Python
2. A text editor like text wrangler to view invisible characters


# Instructions



# References
Python
Text Wrangler
