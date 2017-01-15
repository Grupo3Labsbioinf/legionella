from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord

seq_record = SeqIO.read("LegpneumoPh463_693.gb", "gb") # only works with this file due to range constraints

# generate relevant locus tag strings to store in a list
locus_tags = []
for i in range(463, 693+1):
    locus_tags.append('lpg0' + str(i))

# execute blast for ALL genes
for i in range(693-463+1):
    print('###########-Blast-############')
    feature = seq_record.features[i+1] # +1 to skip the feature type SOURCE
    if feature.type == "CDS":
        seq_PROT = Seq(str(feature.qualifiers["translation"]), IUPAC.extended_protein)
        protein_record = SeqRecord(seq_PROT)
    else:
        feature = seq_record.features[i+2] # since gene and CDS appear alternately, we can skip to CDS by adding +2
                                           # instead of +1 to our index
        seq_PROT = Seq(str(feature.qualifiers["translation"]), IUPAC.extended_protein)
        protein_record = SeqRecord(seq_PROT)
    save_file = open(r'blast_output\blast_%s.xml' % locus_tags[i], 'w')
    result_handle = NCBIWWW.qblast('blastp', 'nr', protein_record.format('gb'))
    blast_results = result_handle.read()
    save_file.write(blast_results)
    save_file.close()
    print('###########-Verificação-############')
    align=open(r'blast_output\blast_%s_align.txt' % locus_tags[i], 'w') # where the output will be written
    result=open(r'blast_output\blast_%s.xml' %locus_tags[i], 'r')
    records= NCBIXML.parse(result)
    item=next(records)
    for alignment in item.alignments:
        for hsp in alignment.hsps:
            if hsp.expect <0.05:
                print('****Alignment****')
                print('sequence:', alignment.title)
                align.write('sequence: ' + alignment.title + '\n')
                print('length:', alignment.length)
                align.write('length: ' + str(alignment.length) + '\n')
                print('score:', hsp.score)
                align.write('score: ' + str(hsp.score) + '\n')
                print('gaps:', hsp.gaps)
                align.write('gaps: ' + str(hsp.gaps) + '\n')
                print('e value: ', hsp.expect)
                align.write('e value: ' + str(hsp.expect) + '\n')
                print(hsp.query[0:75] + '...')
                align.write(hsp.query[0:75] + '...' + '\n')
                print(hsp.match[0:75] + '...')
                align.write(hsp.match[0:75] + '...' +'\n')
                print(hsp.sbjct[0:75] + '...')
                align.write(hsp.sbjct[0:75] + '...' + '\n')
    result.close()
    align.close()
print('\n')
print('###########')
print('Fim')