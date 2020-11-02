#!/usr/bin/env -python

import base64
import logging
import unicodedata
from collections import defaultdict
from openpyxl import load_workbook


def fix_spl_char(value):
    if value == None:
        value = ''
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'), 'utf-8')

survey_file = "Input file provided by OO"
sdata = []
ulist_wb = load_workbook(filename=survey_file, read_only=True)
ulist_all_ws = ulist_wb['All Other Funding']

fund_stat = {}

for rnum, row in enumerate(ulist_all_ws.rows):
    if rnum == 0:
        continue

    fname = fix_spl_char(row[0].value)
    if not fname:
        print("WARN: On row {}, fname '{}' is not valid".format(rnum, fname))
        continue

    fund_type = row[2].value
    fund_amnt = row[3].value
    fac_fte = row[4].value
    
    if fname not in fund_stat:
        fund_stat[fname] = {'fname':fname, 'fte': fac_fte, 'pub':'NA', 'sfund':0, 'ufund':0, 'ofund':0, 'tfund': 0}
    
    if fund_type == 'SciLifeLab':
        fund_stat[fname]['sfund'] += fund_amnt
    elif fund_type == 'University':
        fund_stat[fname]['ufund'] += fund_amnt
    elif fund_type == 'Other':
        fund_stat[fname]['ofund'] += fund_amnt
    else:
        print("WARN: On row {}, check fund type '{}'".format(rnum, rfund_type))
    fund_stat[fname]['tfund'] += fund_amnt

sorted_funds = sorted(fund_stat.values(), key=lambda v: v['tfund'], reverse=True)

out_list = ['Facility\tFTE\tPublications\tScilifelab_fund\tUniversity_fund\tOther_fund\tTotal_fund']
for fund in sorted_funds:
    fund['sfund'] = str(fund['sfund'])
    fund['ufund'] = str(fund['ufund'])
    fund['ofund'] = str(fund['ofund'])
    fund['tfund'] = str(fund['tfund'])
    fund['fte'] = str(fund['fte'])
    out_list.append("\t".join([fund['fname'], fund['fte'], fund['pub'], fund['sfund'], fund['ufund'], fund['ofund'], fund['tfund']]))

# Output file fed to "fte_scatpie.R"
with open("fte_fund_summary.txt", "w") as ujs:
    dstring = "\n".join(out_list) + "\n"
    ujs.write(dstring)
