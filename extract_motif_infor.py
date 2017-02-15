#!/usr/bin/env python3

import sys
import re

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

global name
name = ''
gene_infor_dict = {}
flg = 0

for line in input_file:
	line = line.rstrip()
	data = line.split()
	if re.search("^>",line):
		#print(line,end="\n", file=output_file)
		name = line
		name = name.replace('>','')
		if not name in gene_infor_dict:
			gene_infor_dict[name] = [ [], [] ]
		else:
			pass
		flg = 1
		continue
	if re.match('^\+',line):
		if flg == 1:
			flg = 0
			#print(name, end="\n",file=output_file)
		seq = data[1]
		seq = seq.replace('[','')
		seq = seq.replace(']','')
		pos = data[3]
		pos = pos.replace(',','')

		if re.match("TGTA", seq):

			gene_infor_dict[name][0].append(seq)
			gene_infor_dict[name][1].append(pos)
			continue

		#f re.search('^TATATA',seq):
		#	continue
		
		#print(seq,end="\n",file=output_file)
		continue


print('gene_symbol','PUM_motifs','position',sep="\t",end="\n",file=output_file)

for x in gene_infor_dict.keys():
	gene_name = x
	seq_line = '|'.join(gene_infor_dict[x][0])
	pos_line = '|'.join(gene_infor_dict[x][1])
	if not seq_line == '':
		print(gene_name,seq_line,pos_line, sep="\t",end="\n",file=output_file)
