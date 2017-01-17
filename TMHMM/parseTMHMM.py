import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_TMHMM.xlsx')
worksheet = workbook.add_worksheet("Proteins")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Entry Name", bold)
worksheet.write("B1", "Length", bold)
worksheet.write("C1", "Exp number of AAs in TMHs", bold)
worksheet.write("D1", "SExp number, first 60 AAs", bold)
worksheet.write("E1", "Number of predicted transmembrane helices", bold)
worksheet.write("F1", "Predicted Topology", bold)
# Start from the first cell below the headers.
row = 1
col = 0

handle = open("TMHMM_result.txt")
for line in handle.readlines():
    terms = line.split('\t')
    for i in range(len(terms)):
        term = terms[i].strip()
        worksheet.write(row, col+i, str(term))
    row +=1

handle.close()
workbook.close() # close the workbook