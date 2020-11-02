#/usr/bin/env python

import os
import re
import unicodedata

js_file_temp = '''
var scoreFacList = {flist};

var scoreObject = {sstat};
'''

fstat = {}

keys = ['S1', 'S2', 'S3', 'S4', 'S5', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'I1', 'I2', 'I3', 'I4', 'I5']

flist = ['Bioinformatics Long term Support', 'Bioinformatics Support and Infrastructure', 'Compute and Storage', 'Systems Biology',
         'Advanced Light Microscopy', 'BioImage Informatics', 'Cell Profiling',
         'Cryo EM (SU)', 'Cryo EM (UmU)', 'Protein Science Facility', 'Swedish NMR Centre',
         'Chemical Biology Consortium Sweden (KI)', 'Chemical Biology Consortium Sweden (UmU)',
         'Genome Engineering Zebrafish', 'High Throughput Genome Engineering',
         'Clinical Genomics Goteborg', 'Clinical Genomics Stockholm', 'Clinical Genomics Uppsala',
         'Drug Discovery and Development', 'NGI Stockholm', 'NGI Uppsala SNP&SEQ', 'NGI Uppsala UGC',
         'Autoimmunity Profiling', 'Chemical Proteomics and Proteogenomics (MBB)',
         'Chemical Proteomics and Proteogenomics (OnkPat)', 'Single Cell Proteomics', 'PLA Proteomics',
         'Plasma Profiling', 'Swedish Metabolomics Centre', 'Eukaryotic Single Cell Genomics',
         'Mass Cytometry (KI)', 'Mass Cytometry (LiU)', 'Microbial Single Cell Genomics']

sstat = {'fnames':flist, 'qscore':[], 'sscore':[], 'iscore':[]}

def fix_spl_char(value):
    if value == None:
        value = ''
    value = value.replace(' (NBIS)', '')
    value = value.replace(' (ALM)', '')
    value = value.replace(' (High Throughput Microscopy)', '')
    value = value.replace(' (OncPat)', ' (OnkPat)')
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'), 'utf-8')

def get_mean(tp, dt):
    cnt, sco = (0,0)
    for i in range(1,6):
        sco += (dt[tp + str(i)] * i)
        cnt += dt[tp + str(i)]
    return round(sco/cnt, 2)

# Get survey file of 2018 from DC
with open('user_survey_2018_parsed.tsv', 'r') as sfl:
    head = sfl.readline()
    for uf in sfl:
        scols = uf.strip().split('\t')
        fscores = scols[3].split(',')
        for fs in fscores:
            fnam, fsco = fs.split('-')
            fnam = fix_spl_char(fnam)
            fsco = fsco.split(':')
            
            if fnam in ['Long term Support (WABI)', 'Support and Infrastructure']:
                fnam = 'Bioinformatics ' + fnam.replace(' (WABI)', '')
            
            if fnam not in fstat:
                fstat[fnam] = {k:0 for k in keys}
            fstat[fnam]['S' + str(fsco[0])] += 1
            fstat[fnam]['Q' + str(fsco[1])] += 1
            fstat[fnam]['I' + str(fsco[2])] += 1

for fac in flist:
    fac_sco = fstat[fac]
    sstat['qscore'].append(get_mean('Q', fac_sco))
    sstat['sscore'].append(get_mean('S', fac_sco))
    sstat['iscore'].append(get_mean('I', fac_sco))

# Output then fed to 'distribution_plots.html'
with open("score_content.js", "w") as ujs:
    ujs.write(js_file_temp.format(flist=flist, sstat=sstat))
