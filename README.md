# Merging Microbiome Data Tables
# Author: Taylor Alderete
# Overview: Living organisms are continuously moving throughout their environment, shedding DNA as they travel. This DNA is collected by scientists and has been used to discover rare or invasive species as well as new pathogens in a variety of environments. The PUMA Project focuses on microbiome data and anaysis, for example the production of the 16S rRNA gene. The goal for the Project is to allow researchers to analyse their microbiome data without the use of command-line interface or R/Python scripting.

# Backbone:
# The purpose of my project is to merge tables with a single header and single row, thus the tables will be stacked on top of one another. I do not want to include repeating headers. For users, make sure that you have the same number of dimension of tables before using this program.

# Psuedocode: I will be taking a file and all its columns and headers and using that as the foundation for the tables. For the second tables, I will not include the headers, only the columns that were not included in the first table.This will be continued for the rest of the tables that are being stacked. The files that are being merged are very specific. OTU files will be merged with OTU files. Metadata will only be merged with Metadata.
