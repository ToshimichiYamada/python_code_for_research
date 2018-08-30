#!/usr/bin/env python2

# Code to convert ensembl_geneID to gene symbol


import mygene
mg = mygene.MyGeneInfo()

with open("ensembl_geneID.txt") as f: #ensembl_geneID from text file
    ens = [s.strip() for s in f.readlines()] # read in single line

ginfo = mg.querymany(ens, scopes='ensembl.gene')

txt = open('symbol.txt', 'w')

for g in ginfo:
    for k, v in g.iteritems():
        if k == 'query':
            print >> txt, v,":",
        if k == 'symbol':
            print >> txt, v

txt.close()
