#!/usr/bin/env -python

import json
import xlsxwriter

# Publication input file downloaded manually in
# JSON format from publications portal
with open('files/pub_2019.json', 'r') as jfl:
    pinfo = json.load(jfl)

pub_list = pinfo['publications']

skip_label = ['Bioinformatics Compute and Storage']
bioinfo_labels = ['Bioinformatics Long-term Support WABI', 'Bioinformatics Support and Infrastructure']
ngi_labels = ['NGI Stockholm (Genomics Applications)', 'NGI Uppsala (SNP&SEQ Technology Platform)', 'NGI Stockholm (Genomics Production)']

multi_pub, pub_cnt = (0, 0)

multi_labels, single_labels = ([], [])

for pub in pub_list:
    cnt, binf_cnt, ngi_cnt = (0, 0, 0)
    pub_cnt += 1
    for l in pub['labels']:
        if l in skip_label:
            continue
        elif l in bioinfo_labels:
            if binf_cnt == 0:
                cnt += 1
                binf_cnt += 1
            else:
                continue
        elif l in ngi_labels:
            if ngi_cnt == 0:
                cnt += 1
                ngi_cnt += 1
            else:
                continue
        else:
            cnt +=1
        if cnt > 1:
            multi_pub += 1
            break
    
    if cnt > 1:
        multi_labels.append([pub['title'], ", ".join(pub['labels'].keys())])
    else:
        single_labels.append([pub['title'], ", ".join(pub['labels'].keys())])

all_labels =  multi_labels + single_labels

# Creates excel file with publication title and facilities involved
users_wbook = xlsxwriter.Workbook("publications_label.xlsx")

head_text_format = users_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = users_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = users_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

users_wsheet = users_wbook.add_worksheet()
#users_wsheet.freeze_panes(1, 0)
#users_wsheet.set_row(0, None, ['Pubilcation Title', 'Publication Labels'], head_text_format)
users_wsheet.set_column(0, 1, 100, long_text_format)

cf1 = users_wbook.add_format()
cf1.set_bg_color('#ecf7a6')

cf2 = users_wbook.add_format()
cf2.set_bg_color('#f5cabc')

for row, rdata in enumerate(all_labels):
    users_wsheet.write_row(row, 0, rdata, cf1 if row < 77 else cf2)

users_wbook.close()

# prints the percentage of multiple facility publications
print(round((multi_pub/pub_cnt)*100, 2))