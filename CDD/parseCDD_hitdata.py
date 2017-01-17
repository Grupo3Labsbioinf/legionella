import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_CDD_hitdata.xlsx')
worksheet = workbook.add_worksheet("CDD Results")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Query", bold)
worksheet.write("B1", "UniProt ID", bold)
worksheet.write("C1", "Hit Type", bold)
worksheet.write("D1", "PSSM-ID", bold)
worksheet.write("E1", "From", bold)
worksheet.write("F1", "To", bold)
worksheet.write("G1", "E-Value", bold)
worksheet.write("H1", "Bitscore", bold)
worksheet.write("I1", "Accession", bold)
worksheet.write("J1", "Shortname", bold)
worksheet.write("K1", "Incomplete", bold)
worksheet.write("L1", "Superfamily", bold)
# Start from the first cell below the headers.
row = 1
col = 0

f = open('hitdata.txt')
lines = f.readlines()
f.close()

for i in range(8,len(lines)):
    query_name = lines[i][:7]
    if '>' in query_name:
        line = lines[i][7:]
        worksheet.write(row, col, query_name[:4])
    elif '- ' in query_name:
        line = lines[i][8:]
        worksheet.write(row, col, query_name[:5])
    else:
        line = lines[i][9:]
        worksheet.write(row, col, query_name[:6])
    terms = line.strip().split('\t')
    for i in range(len(terms)):
        worksheet.write(row, col+i+1, terms[i])
    row += 1

workbook.close() # close the workbook