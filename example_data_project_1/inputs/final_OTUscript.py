InFileName1 = "sample_17_OTUtable.txt"

InFileName2 = "sample_18_OTUtable.txt"

InFileName3 = "sample_19_OTUtable.txt"

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

InFile1.close()

InFile2.close()

InFile3.close()

OutFile.close()
