from Bio.KEGG import REST
# Opens a text file containing KEGG search terms and retrieves their relevant information in the KEGG DB
# Writes the output for each term in a separated file
f = open('kegg_entries.txt', 'r')
search_terms = []
for line in f.readlines():
    terms = line.split('\t')
    if terms[0] != '\n': # can be removed if there's no lone newlines between lines
        search_terms.append(terms[0])
f.close()
for term in search_terms:
    filename = r'KEGG_output\kegg_entry' + term + '.txt'
    filename = filename.replace(':', '')
    output = open(filename, 'w') # if the filename is changed to be the same in each loop, the output can be stored
                                 # in a single file
    entry = REST.kegg_get(term)
    output.write('#####' + term + '#####' + '\n')
    for line in entry.readlines():
        output.write(line)
    output.close()
