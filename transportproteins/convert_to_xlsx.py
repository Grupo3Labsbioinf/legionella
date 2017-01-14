import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('membranetransport.xlsx')
worksheet = workbook.add_worksheet("Localization Prediction")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "ORF", bold)
worksheet.write("B1", "Family ID", bold)
worksheet.write("C1", "Family TC", bold)
worksheet.write("D1", "Family Name", bold)
worksheet.write("E1", "Transporter Type", bold)
worksheet.write("F1", "Substrate", bold)
worksheet.write("G1", "TC", bold)
# collect lines from file to make rows
lines = []
with open('membranetransport.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip())
# Start from the first cell below the headers.
row = 1
col = 0
for line in lines:
    terms = line.split('\t')
    terms = list(filter(None, terms)) # remove empty strings from list
    for i in range(len(terms)):
        worksheet.write(row, col+i, terms[i])
    row += 1

workbook.close() # close the workbook
