from Bio import SearchIO

filenames = []
outputs = []
for i in range(463, 693+1):
    filename = r'blast_output\blast_lpg0' + str(i) + '.xml'
    filenames.append(filename)
    output = r'blast_output\hit_descriptions\hit_description_lpg0' + str(i) + '.txt'
    outputs.append(output)

for i in range(693-463+1):
    qresults = SearchIO.parse(filenames[i], 'blast-xml')
    output = outputs[i]
    f = open(output, 'w')
    for qresult in qresults:
        for hit in qresult:
            print(hit)
            f.write(hit.description+'\n')
    f.close()
