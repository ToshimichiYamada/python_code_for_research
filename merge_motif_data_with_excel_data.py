#!/usr/bin/env python3

import sys
import re

input_motif_file = open('./siPUM1_up/siPUM1_up_motif_infor2.txt', 'r')
input_excel_file = open('siStealth_compatible_genes_RefSeq_result_mRNA.fpkm_table', 'r')
output_file = open('./siPUM1_up/siPUM1_up_motif_infor_merged2.txt', 'w')

motif_infor_dict = {}
count = 0

for line in input_motif_file:
	line = line.rstrip()
	data = line.split("\t")
	if data[0] == 'gene_symbol':
		continue
	gene_name = data[0]
	motif = data[1]
	pos = data[2]

	motif_infor_dict[gene_name] = [motif,pos]
	count += 1
print(count)

count2 = 0
for line in input_excel_file:
	line = line.rstrip()
	data = line.split("\t")
	if data[0] == 'gr_id':
		print("\t".join(data[0:4]),"motifs","position", sep="\t",end="\n",file=output_file)
		continue

	gene_name = data[1]
	if gene_name in motif_infor_dict:
		motif_line = motif_infor_dict[gene_name][0]
		pos_line = motif_infor_dict[gene_name][1]
		count2 += 1
		print("\t".join(data[0:4]),motif_line,pos_line, sep="\t",end="\n",file=output_file)
	else:
		motif_line = 'NA'
		pos_line = "NA"
		print("\t".join(data[0:4]),motif_line,pos_line, sep="\t",end="\n",file=output_file)

print(count2)