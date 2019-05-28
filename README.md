# Merging Microbiome Data Tables
# Author: Taylor Alderete
# Overview: Living organisms are continuously moving throughout their environment, shedding DNA as they travel. This DNA is collected by scientists and has been used to discover rare or invasive species as well as new pathogens in a variety of environments. The PUMA Project focuses on microbiome data and anaysis, for example the production of the 16S rRNA gene. The goal for their Project is to allow researchers to analyse their microbiome data without the use of command-line interface or R/Python scripting.

# Backbone:
# The purpose of my project is to merge tables with a single header and single row, thus the tables will be stacked on top of one another. I do not want to include repeating headers. For users, make sure that you have the same number of dimension of tables before using this program.

# Psuedocode: I will be taking three files and all their common and uncommon header rows and using that as the foundation for the final concatenated table. For example, some of the uncommon headers among the three tables in Metadata include, pH meter CALeDNA, Amount of Leaf Litter, Time Collection, pH Litmus Strip. The final concatenated header row will include all of theses headers, even if the table does not have any data for it. The same goes for the final concatenated OTU table. 
