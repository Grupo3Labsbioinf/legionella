import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_CDD_featdata.xlsx')
worksheet = workbook.add_worksheet("CDD Results")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Query", bold)
worksheet.write("B1", "UniProt ID", bold)
worksheet.write("C1", "Type", bold)
worksheet.write("D1", "Title", bold)
worksheet.write("E1", "Coordinates", bold)
worksheet.write("F1", "Complete Size", bold)
worksheet.write("G1", "Mapped Size", bold)
worksheet.write("H1", "Source Domain", bold)
# Start from the first cell below the headers.
row = 1
col = 0

f = open('featdata.txt')
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