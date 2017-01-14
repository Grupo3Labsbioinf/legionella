from Bio import Entrez
from Bio import Medline


lista_de_termos=['Legionella  pneumophila paris','Legionella  pneumophila lens' ]  # inserir termos que quer pesquisar a aqui
for i in lista_de_termos:

    Entrez.email = 'email_aqui'  # NOTA: Fazer mail
    handle = Entrez.egquery(term= i)
    record = Entrez.read(handle)

    for row in record['eGQueryResult']:
        if row['DbName'] == 'pubmed':
            x = row['Count']

    handle = Entrez.esearch(db='pubmed', term=i, retmax=x)
    record = Entrez.read(handle)
    idlist = record['IdList']

    handle = Entrez.efetch(db='pubmed', id=idlist, rettype='medline', retmode='text')
    records = list(Medline.parse(handle))
    record_results = open('lista_de_fontes %s.txt' %i,  'w')
    for record in records:
        tit = ('Title: ', record.get('TI', '?'))
        aut = ('Authors: ', record.get('AU', '?'))
        sour = ('Source: ', record.get('SO', '?'))

        record_results.write(str(tit))
        record_results.write('\n')
        record_results.write(str(aut))
        record_results.write('\n')
        record_results.write(str(sour))
        record_results.write('\n')
        record_results.write('\n')

    record_results.close()
