
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord

seq_record = SeqIO.read("sequence.gb", "gb")

tag = input('insert locus_tag: ')

for feature in seq_record.features:
    if feature.type == "CDS":
        seq_PROT = Seq(str(feature.qualifiers["translation"]), IUPAC.extended_protein)
        protein_record = SeqRecord(seq_PROT)



print('###########-Blast-############')

save_file = open('blast_%s.xml' % tag, 'w')
result_handle = NCBIWWW.qblast('blastp', 'nr', protein_record.format('gb'))
blast_results = result_handle.read()
save_file.write(blast_results)
save_file.close()

print('###########-Verificação-############')



verify=open('blast_%s_verificacao.txt' % tag, 'w')
result=open('blast_%s.xml' %tag, 'r')
records= NCBIXML.parse(result)
item=next(records)
for alignment in item.alignments:
          for hsp in alignment.hsps:
                 if hsp.expect <0.05:
                     print('****Alignment****')
                     print('sequence:', alignment.title)
                     print('length:', alignment.length)
                     print('score:', hsp.score)
                     print('gaps:', hsp.gaps)
                     print('e value:', hsp.expect)
                     print(hsp.query[0:75] + '...')
                     print(hsp.match[0:75] + '...')
                     print(hsp.sbjct[0:75] + '...')
verify.close()
print('\n')
print('###########')
print('Fim')
