from Bio import SeqIO
from Bio import Entrez
Entrez.email = "mccm20@gmail.com"
record = SeqIO.read('LegpneumoPh463_693.gb', "genbank")
proteinIDs = []
for feat in record.features:
    if feat.type == "CDS":
        proteinIDs.append(''.join(feat.qualifiers["protein_id"]))
# write new file with the ids
f = open('proteinids.txt', 'w')
for id in proteinIDs:
    f.write(id)
    f.write('\n')
f.close()
