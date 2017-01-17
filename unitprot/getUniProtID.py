from Bio import SwissProt
handle = open("prots.txt")
f = open('uniprotids.txt', 'w')
for record in SwissProt.parse(handle):
    f.write(''.join(record.accessions))
    f.write('\n')
f.close()
