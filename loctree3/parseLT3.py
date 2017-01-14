import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('loctree3.xlsx')
worksheet = workbook.add_worksheet("Localization Prediction")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Protein ID", bold)
worksheet.write("B1", "Score", bold)
worksheet.write("C1", "Localization", bold)
worksheet.write("D1", "Gene Ontology Terms", bold)
# collect unitprot ids for parsing
ids = []
with open('uniprotids.txt', 'r') as f:
   for id in f.readlines():
       ids.append(id.strip())
# Start from the first cell below the headers.
row = 1
col = 0
with open('loctree3.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        for id in ids:
            if id in line:
                terms = line.split('\t')
                worksheet.write(row, col, id)
                worksheet.write(row, col+1, terms[1])
                worksheet.write(row, col+2, terms[2])
                worksheet.write(row, col+3, terms[3])
                row +=1
workbook.close() # close the workbook