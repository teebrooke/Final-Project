# A.B.C (Always be Concatenating)

# Author: 
Taylor Alderete

Email: teebrooke@g.ucla.edu

# Introduction: 

Why is eDNA important in Microbial ecology? All organisms travel across their environment and what do they leave behind... eDNA. These traces of eDNA allow us to not only study live organisms, but also  decomposits of dead organisms. The infomration we get from eDNA allows us to dig deeper into microbial ecology, how organisms interact with others in their surrounding areas. Soil, feces and water samples all contain millions of strands of DNA from a variety of organisms. The purpose of this program is to concatenate sets of eDNA and metadata to make it cleaner and easier for individuals to view large data sets. Data from the PUMA Project was incorporated into the program and the output was two clean, concatentated table with a single header that represented all three tables respectively.   

# Purpose
The purpose of my project is to concatenate tables with a single header and single row, thus the final tables will be concatenated with repsect to their titles, Metadata and OTU seperately. I do not want to include repeating headers. 


# Program workflow

METADATA:

1. Carefully examine the sample_merged_METADATA output file to see how the final concatenated header should look like.

2. Carefully examine the files 17,18,19 using text wrangler to see any invisible characters like tabs and line feeds   

3. Since file 18 contains a complete header we will start there

4. File 17 and file 19 header and rows are compared with fiel 18's headers and rows

5. Default tabs fill data values to align file 17 and file 19 with file 18 header

6. To test the correct function of the code  use text wrangler to evaluate the output

7. The final output file name is merged_sample_metadata_12_june.txt for comparison.

OTU: 

1. Carefully examine the sample_merged_OTU output file to see how the final concatenated header should look like.

2. Carefully examine input files 17,18,19

3. See that there are zeros instead of tabs in files 17,18,19

4. Concatenate the headers and insert zeros to permit alignment to the concatenated header

5. To test the correct function of the code use text wrangler to evaluate the output.

6. The final output file name is OTU_3_tables_merged.txt for comparison.

# Dependencies
1. Python 3.6
This is important because the  difference between Python 2 and 3 is that the print statement in Python 2 is just print, but in Python 3 you need to enclose the print statement in parenthese. 

2. A text editor like text wrangler to view invisible characters. This is important because invisible characters are part of the text. The goal is to match the uncommon invisible characters like line feeds and tabs. This is important when concatenating headers and tables. 



# Instructions

METADATA 

1. Python program and corresponding input programs need to be in the same directory

2. Python was called from terminal 

3. Insert python program name final_METADATAscript.py

4. Press return 

5. Open text wrangler to see final output and compare with sample output

OTU

1. User must have Python 3.6

2. Python program and corresponding input programs need to be in the same directory

3. Python was called from terminal 

4. Insert python program name final_OTUscript.py

5. Press return 

6. Open text wrangler to see final output and compare with sample output
 
# References
Python 3.6

Text Wrangler

PUMA Project https://www.biorxiv.org/content/10.1101/482380v1.full. 
