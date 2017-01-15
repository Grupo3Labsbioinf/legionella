from Bio import Entrez
from Bio import SeqIO

Entrez.email = "labsbiog3@gmail.com"

handle = Entrez.efetch(db="nucleotide", id="NC_002942.5", rettype="gb", retmode="text", seq_start="505536", seq_stop="753100")

seq_record = SeqIO.read(handle, "genbank")
SeqIO.write(seq_record, 'sequence.gb', "genbank") #Guarda em formato genbank
handle.close()
