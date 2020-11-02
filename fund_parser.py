#!/usr/bin/env -python

import base64
import logging
import unicodedata
from collections import defaultdict
from openpyxl import load_workbook
from adrian_code.publications_api import Publications_api


js_file_temp = '''
var fundStat = {};

'''

label_map = {'Advanced Light Microscopy (ALM)': 'Advanced Light Microscopy',
             'Ancient DNA': 'Ancient DNA',
             'Autoimmunity Profiling': 'Autoimmunity Profiling', 
             'BioImage Informatics': 'BioImage Informatics', 
             'Cell Profiling': 'Cell Profiling', 
             'Chemical Biology Consortium Sweden (CBCS)': 'Chemical Biology Consortium Sweden', 
             'Chemical Proteomics & Proteogenomics': 'Chemical Proteomics and Proteogenomics', 
             'Clinical Genomics Gothenburg': 'Clinical Genomics Gothenburg', 
             'Clinical Genomics Lund': 'Clinical Genomics Lund', 
             'Clinical Genomics Stockholm': 'Clinical Genomics Stockholm', 
             'Clinical Genomics Uppsala': 'Clinical Genomics Uppsala', 
             'Bioinformatics Compute and Storage': 'Compute and Storage', 
             'Cryo-EM': 'Cryo-EM', 
             'Drug Discovery and Development (DDD)': 'Drug Discovery and Development', 
             'Eukaryotic Single Cell Genomics (ESCG)': 'Eukaryotic Single Cell Genomics', 
             'Genome Engineering Zebrafish': 'Genome Engineering Zebrafish', 
             'High-throughput Genome Engineering (HTGE)': 'High Throughput Genome Engineering', 
             'Bioinformatics Long-term Support WABI': 'Bioinformatics Long-term Support', 
             'Mass Cytometry': 'Mass Cytometry', 
             'Microbial Single Cell Genomics': 'Microbial Single Cell Genomics', 
             'NGI Stockholm (Genomics Production)': 'NGI Stockholm',
             'NGI Stockholm (Genomics Applications)': 'NGI Stockholm', 
             'NGI Uppsala (SNP&SEQ Technology Platform)': 'NGI Uppsala SNP&SEQ', 
             'NGI Uppsala (Uppsala Genome Center)': 'NGI Uppsala UGC', 
             'PLA and Single Cell Proteomics': 'PLA and Single Cell Proteomics', 
             'Plasma Profiling': 'Plasma Profiling', 
             'Protein Science Facility (PSF)': 'Protein Science Facility', 
             'Bioinformatics Support and Infrastructure': 'Bioinformatics Support and Infrastructure', 
             'Swedish Metabolomics Centre (SMC)': 'Swedish Metabolomics Centre', 
             'Swedish NMR Centre (SNC)': 'Swedish NMR Centre', 
             'Systems Biology': 'Bioinformatics Systems Biology'}

platform_map = {"Advanced Light Microscopy" : "Cellular and Molecular Imaging",
                "Ancient DNA" : "Genomics",
                "Autoimmunity Profiling" : "Proteomics and Metabolomics",
                "BioImage Informatics" : "Cellular and Molecular Imaging",
                "Cell Profiling" : "Cellular and Molecular Imaging",
                "Chemical Biology Consortium Sweden" : "Chemical Biology and Genome Engineering",
                "Chemical Proteomics and Proteogenomics" : "Proteomics and Metabolomics",
                "Clinical Genomics Gothenburg" : "Diagnostics Development",
                "Clinical Genomics Lund" : "Diagnostics Development",
                "Clinical Genomics Stockholm" : "Diagnostics Development",
                "Clinical Genomics Uppsala" : "Diagnostics Development",
                "Compute and Storage" : "Bioinformatics",
                "Cryo-EM" : "Cellular and Molecular Imaging",
                "Drug Discovery and Development" : "Drug Discovery and Development",
                "Eukaryotic Single Cell Genomics" : "Genomics",
                "Genome Engineering Zebrafish" : "Chemical Biology and Genome Engineering",
                "High Throughput Genome Engineering" : "Chemical Biology and Genome Engineering",
                "In Situ Sequencing" : "Genomics",
                "Bioinformatics Long-term Support" : "Bioinformatics",
                "Mass Cytometry" : "Proteomics and Metabolomics",
                "Microbial Single Cell Genomics" : "Genomics",
                "NGI Stockholm" : "Genomics",
                "NGI Uppsala SNP&SEQ" : "Genomics",
                "NGI Uppsala UGC" : "Genomics",
                "PLA and Single Cell Proteomics" : "Proteomics and Metabolomics",
                "Plasma Profiling" : "Proteomics and Metabolomics",
                "Protein Science Facility" : "Cellular and Molecular Imaging",
                "Bioinformatics Support and Infrastructure" : "Bioinformatics",
                "Swedish Metabolomics Centre" : "Proteomics and Metabolomics",
                "Swedish NMR Centre" : "Cellular and Molecular Imaging",
                "Bioinformatics Systems Biology" : "Bioinformatics"}

ignore_label = ['Advanced FISH Technologies', 'Advanced Mass Spectrometry Proteomics', 'AIDA Data Hub', 'Array and Analysis Facility', 'Biochemical Imaging Centre Umeå', 'Bioinformatics and Expression Analysis (BEA)', 'Bioinformatics Support, Infrastructure and Training', 'BioMaterial Interactions (BioMat)', 'Centre for Cellular Imaging', 'Chemical Proteomics', 'Clinical Biomarkers', 'Clinical Genomics Linköping', 'Clinical Genomics Örebro', 'Clinical Genomics Umeå', 'Clinical Proteomics Mass spectrometry', 'Exposomics', 'Fluorescence Correlation Spectroscopy', 'Fluorescence Tissue Profiling', 'Glycoproteomics', 'Gothenburg Imaging Mass Spectrometry', 'In Situ Sequencing (ISS)', 'Intravital Microscopy Facility', 'Karolinska High Throughput Center (KHTC)', 'Mass Spectrometry-based Proteomics, Uppsala', 'Mutation Analysis Facility (MAF)', 'National Genomics Infrastructure', 'National Resource for Mass Spectrometry Imaging', 'Proteogenomics', 'Targeted and Structural Proteomics', 'Tissue Profiling']

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
    if fname not in fund_stat:
        fund_stat[fname] = {'fname':fname, 'plat': platform_map[fname], 'sfund':0, 'ufund':0, 'ofund':0, 'tfund': 0, 'pub':0}
    fund_type, fund_amnt = (row[2].value, row[3].value)
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

for fund in sorted_funds:
    fund['sfund'] = fund['sfund']*1000
    fund['ufund'] = fund['ufund']*1000
    fund['ofund'] = fund['ofund']*1000
    fund['tfund'] = fund['tfund']*1000

pub_getter = Publications_api(years=["2019"])
pub_2019 = pub_getter.get_publications()

pub_read = []
for pub in pub_2019:
    if pub["doi"] in pub_read:
        continue
    ngi_sto = False
    for lab in pub['labels']:
        if lab in ignore_label:
            continue
        elif lab.startswith('NGI Stockholm'):
            if not ngi_sto:
                fund_stat['NGI Stockholm']['pub'] += 1
                ngi_sto = True
        else:
            fund_stat[label_map[lab]]['pub'] += 1
    pub_read.append(pub["doi"])

# Out file fed to "distribution_plots.html"
with open("fund_content.js", "w") as ujs:
    ujs.write(js_file_temp.format(sorted_funds))
