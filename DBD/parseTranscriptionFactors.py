import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_DBB.xlsx')
worksheet = workbook.add_worksheet("DBD Results")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "	Hidden Markov Model identifier", bold)
worksheet.write("B1", "Sequence identifier", bold)
worksheet.write("C1", "Match region", bold)
worksheet.write("D1", "Family name", bold)
# Start from the first cell below the headers.
row = 1
col = 0

f = open('x7.tf.ass', 'r')
lines = f.readlines()
f.close()

g = open('proteinids.txt', 'r')
ids = g.readlines()
id_list = []
for id in ids:
    id = id.strip()
    id_list.append(id)
g.close()


for i in range(1, len(lines)):
    terms = lines[i].split('\t')
    for id in id_list:
        if id == terms[1][16:len(terms[1])-1]:
            print("yo")
            for i in range(len(terms)):
                print(row, col+1, terms[i])
                worksheet.write(row, col+i, terms[i])
            row += 1

workbook.close() # close the workbook