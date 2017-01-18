from Bio.KEGG import REST
from Bio.KEGG import Enzyme
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('LegpneumoPh463_693_Enzymes.xlsx')
worksheet = workbook.add_worksheet("KEGG Enzymes")
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
# Initiate the workbook by filling the first row with headers
worksheet.write("A1", "Gene ID (NCBI, KEGG)", bold)
worksheet.write("B1", "Locus Tag", bold)
worksheet.write("C1", "EC Number", bold)
worksheet.write("D1", "KEGG Orthologs", bold)
worksheet.write("E1", "KEGG Reactions IDs", bold)
worksheet.write("F1", "KEGG Pathways", bold)
# Start from the first cell below the headers.
row = 1
col = 0

ec = open("ecnums.txt", "r")
ec_nums = []
for line in ec.readlines():
    line = line.strip()
    ec_nums.append(line)

for ec_num in ec_nums:
    if "-" in ec_num:
        continue
    print(ec_num)
    res = []
    request = REST.kegg_get("ec:"+ec_num)
    open(r"enzymes\ec_"+ec_num+".txt", 'w').write(request.read())
    records = Enzyme.parse(open(r"enzymes\ec_"+ec_num+".txt"))
    record = list(records)[0]

    # locus_tag
    gene = ""
    for g in record.genes:
        if "LPN" in g:
            gene = g
    if gene != "":
        gene = ''.join(gene[1])
    res.append(gene)
    # EC Number
    ec_number = record.entry
    res.append(ec_number)
    # KEGG Ortholog
    f = open("ec_4.2.1.10.txt", 'r')
    orthologs = []
    for line in f.readlines():
        if line[:12] != "            ":
            keyword = line[:12]
        data = line[12:].strip()
        if "ORTHOLOGY" in keyword:
            orthologs.append(data)
    f.close()
    orth_str = ""
    for ortholog in orthologs:
        orth_str += ortholog + ", "
    res.append(orth_str)
    # KEGG Reaction
    reactions = record.reaction
    if len(reactions) > 1:
        reac_list = ""
        for reaction in reactions:
            reac_list += reaction + ', '
        res.append(reac_list)
    else:
        res.append(''.join(reactions))
    # Kegg Pathways
    pathways = record.pathway
    path_str = ""
    for pathway in pathways:
        id = pathway[1]
        path = pathway[2]
        path_str += id + ": " + path + ", "
    res.append(path_str)

    for i in range(len(res)):
        worksheet.write(row, col+i+1, res[i])
    row += 1

workbook.close() # close the workbook