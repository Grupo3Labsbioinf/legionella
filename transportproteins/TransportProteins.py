from lxml import html
import requests


def main():
    page = requests.get('http://www.membranetransport.org/all_type_btab.php?oOID=lpne1')
    tree = html.fromstring(page.content)

    fdisc=open("membranetransport.txt","w")

    tds=tree.xpath('//td/text()')

    rows={}
    index="columns"
    rows[index]=[]
    for td in tds:
        if isLocus(td):
            index=td
            rows[index]=[]
        else:
            rows[index].append(td)

    del(rows["columns"])

    for gene in rows:
        if int(gene[3:7])>462 and int(gene[3:7])<694:
            fdisc.write(str(gene)+"\t\t")
            fdisc.write("\t\t".join(rows[gene]))
            fdisc.write("\n")

def isLocus(string):
    return bool(string.find("lpg")>=0)


main()
