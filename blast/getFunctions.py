import os
import re

filelist=os.listdir()

newfile=open("functions.csv","w")

for filename in filelist:
    gene=re.search("lpg[0-9]+",filename)
    if gene:
        filedesc=open(filename,"r")
        text=filedesc.read()
        filedesc.close()
        text=text.strip().split("\n")
        functions={}
        for line in text:
            function=re.search("[^[]+",line).group().strip()
            if function in functions:
                functions[function]+=1
            else:
                functions[function]=1

        flag=False
        counter=0
        for function in functions:
            if functions[function]>counter:
                counter=functions[function]
                maxfunc=function

        if maxfunc=="hypothetical protein":
            flag=True
            counter=0
            for function in functions:
                if functions[function]>counter and function!="hypothetical protein":
                    counter=functions[function]
                    maxfunc=function

        newfile.write(gene.group()+","+maxfunc+",")
        if flag:
            newfile.write("*"+str(functions[maxfunc])+"\n")
        else:
            newfile.write(str(functions[maxfunc])+"\n")

newfile.close()
