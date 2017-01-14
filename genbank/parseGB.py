from Bio import SeqIO
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_features.xlsx')
worksheet = workbook.add_worksheet("Features")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Locus tag", bold)
worksheet.write("B1", "DB xref", bold)
worksheet.write("C1", "Gene", bold)
worksheet.write("D1", "Product", bold)
worksheet.write("E1", "Function", bold)
worksheet.write("F1", "Translation", bold)
worksheet.write("G1", "Note", bold)
# Start from the first cell below the headers.
row = 1
col = 0
# Iterate over the data and write it out row by row.
record = SeqIO.read('LegpneumoPh463_693.gb', "genbank")
for feat in record.features:
    # All this will be written in the same row
    # If a dict key only appears in certain genes, there's an if clause to add that information only if it exists,
    # else write "N/A" for that column in the current row
    if feat.type == "gene":
        worksheet.write(row, col, ''.join(feat.qualifiers["locus_tag"])) # first column
        worksheet.write(row, col+1, ''.join(feat.qualifiers["db_xref"])) # second column, and so forth
        if "gene" in feat.qualifiers:
            worksheet.write(row, col+2, ''.join(feat.qualifiers["gene"]))
        else:
            worksheet.write(row, col+2, "N/A")
    if feat.type == "CDS":
        worksheet.write(row, col+3, ''.join(feat.qualifiers["product"]))
        if "function" in feat.qualifiers:
            worksheet.write(row, col+4, ''.join(feat.qualifiers["function"]))
        else:
            worksheet.write(row, col+4, "N/A")
        worksheet.write(row, col+5, ''.join(feat.qualifiers["translation"]))
        if "note" in feat.qualifiers:
            worksheet.write(row, col+6, ''.join(feat.qualifiers["note"]))
        else:
            worksheet.write(row, col+6, "N/A")
        row += 1 # the types "gene" and "CDS" appear in the same order for all genes so advance rows only after "CDS"

workbook.close() # close the workbook
