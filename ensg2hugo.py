#!/usr/bin/python

import sys
import fileinput
import re
import csv

ensg2hugo = {}
for each_line_of_text in fileinput.input("./Homo_sapiens.GRCh37.75.gtf"):
    gene = re.findall(r'^.*?\t.*?\t(gene)\t', each_line_of_text, re.I)
    geneID = re.findall(r'gene_id "(ENSG\d*?)"', each_line_of_text, re.I)
    hugoName = re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    if gene:
        if geneID:
            if hugoName:
                ensg2hugo[geneID[0]]= hugoName[0]
               # print(ensg2hugo)
for line in fileinput.input("./expres.anal.csv"):
    splitcolumn = re.split('\,', line)
    ensembl = re.findall(r'ENSG+[0-9]{11}', line, re.I)
    if ensembl:
        match = ensembl[0]
       # print(match)
        if match in ensg2hugo:
            print(splitcolumn[0] + ',"' + ensg2hugo[match] + '",'+ splitcolumn[2] + ','+ splitcolumn[3] + ',' + splitcolumn[4])
        else:
            print((splitcolumn[0] + ',' + "NA"+ ','+ splitcolumn[2] + ','+ splitcolumn[3] + ',' + splitcolumn[4]))
