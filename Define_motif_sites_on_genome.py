#!/usr/bin/env python3

import re
import sys

motif_file = open("allgene_PUMmotif_combined_refid.txt", 'r') #$Refseq_mRNA_3UTR_PUM_study.result NM_000XXX  300,1000
motif_length = int(8) #8nt
anno_bed_list = open("/home/akimitsu/Documents/database/annotation_file/Refseq_gene_hg19_June_02_2014_3UTR.bed", 'r') #Refseq_mRNA_3UTR.bed
output_file = open("allgene_PUMmotif_combined_refid_genome_sites.txt", 'w')

motif_dict = {}

for line in motif_file:
    line = line.rstrip()
    data = line.split("\t")
    if data[0] == "refid":
        continue
    refid = data[0]
    if data[2] != "NA":
        motif_st_sites = data[2].split('|')
        motif_seq = data[1].split('|')
        motif_dict[refid] = [motif_st_sites,motif_seq]
    else:
        continue

counter = 0

for line in anno_bed_list:
    line = line.rstrip()
    data = line.split("\t")
    refid = data[3]
    if refid in motif_dict:
        motif_st_sites = motif_dict[refid][0] #list(st)
        motif_seq = motif_dict[refid][1] #list(st)
        motif_sites = [[int(x), int(x)+int(motif_length)] for x in motif_st_sites] #[[st1,ed1], [st2,ed2]...]

        chrom = data[0]
        st = int(data[1])
        ed = int(data[2])
        strand = data[5]

        exon_block = data[10].split(',')
        exon_block.pop()
        exon_block = list(map(int,exon_block))
        exon_st_block = data[11].split(',')
        exon_st_block.pop()
        exon_st_block = list(map(int,exon_st_block))

        for x in range(len(motif_sites)):
            #Define the start/end site of one of motifs
            st_motif = motif_sites[x][0]
            ed_motif = motif_sites[x][1]
            curr_motif_seq = motif_seq[x]
            if len(exon_block) == 1:
                if strand == '+':
                    chrom_st_motif = st + st_motif - 1
                    chrom_ed_motif = st + ed_motif - 1
                    length = str(chrom_ed_motif - chrom_st_motif) + ','
                    print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid + '|' + curr_motif_seq,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                elif strand == '-':
                    chrom_st_motif = ed - ed_motif + 1
                    chrom_ed_motif = ed - st_motif + 1
                    length = str(chrom_ed_motif - chrom_st_motif) + ','
                    print(chrom,str(chrom_st_motif),str(chrom_ed_motif),refid + '|' + curr_motif_seq,'0',strand,str(chrom_ed_motif),str(chrom_ed_motif),'0','1',length,'0,', sep="\t", end="\n", file=output_file)
                else:
                    print("ERROR: Strand is not defined...")
                    sys.exit(1)
            else:
                #print(refid)
                #print(exon_st_block)
                #print(exon_block)
                #exon_sites_real: Define the start/end sites for each exon based on 'genome' position
                exon_sites_real = [[exon_st_block[i],exon_st_block[i]+exon_block[i]] for i in range(len(exon_block))] #[[exon_st1,exon_ed1], [exon_st2,exon_ed2]...]

                #exon_sites: Define the start/end sites for each exon based on 'transcript' position
                #exon_block = [200,100,50]
                exon_block_test = [0] + exon_block
                exon_site_now = exon_block_test[0]
                exon_sites = [] #[[exon_st1,exon_ed1], [exon_st2,exon_ed2]...]
                for index in range(len(exon_block_test)-1):
                    exon_sites.extend([[exon_site_now, exon_site_now+exon_block_test[index+1]]])
                    exon_site_now += exon_block_test[index+1]
    else:
        continue

print(str(counter))