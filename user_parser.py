#!/usr/bin/env -python

import base64
import logging
import unicodedata
from collections import defaultdict
from openpyxl import load_workbook

# University names in English
js_file_temp = '''
var userAffListEng = {org_list};

var userAffLabelEng = {aff_label};

var userFacListEng = {fac_list};

var userFacLabelEng = {fac_list};

var platformList = {pla_list};

var platformMap = {{"Advanced Light Microscopy (ALM)" : "Cellular and Molecular Imaging",
                "Ancient DNA" : "Genomics",
                "Autoimmunity Profiling" : "Proteomics and Metabolomics",
                "BioImage Informatics" : "Cellular and Molecular Imaging",
                "Cell Profiling" : "Cellular and Molecular Imaging",
                "Chemical Biology Consortium Sweden" : "Chemical Biology and Genome Engineering",
                "Chemical Proteomics and Proteogenomics (MBB)" : "Proteomics and Metabolomics",
                "Chemical Proteomics and Proteogenomics (OnkPat)" : "Proteomics and Metabolomics",
                "Clinical Genomics Goteborg" : "Diagnostics Development",
                "Clinical Genomics Lund" : "Diagnostics Development",
                "Clinical Genomics Stockholm" : "Diagnostics Development",
                "Clinical Genomics Uppsala" : "Diagnostics Development",
                "Compute and Storage" : "Bioinformatics",
                "Cryo-EM (SU)" : "Cellular and Molecular Imaging",
                "Cryo-EM (UmU)" : "Cellular and Molecular Imaging",
                "Drug Discovery and Development" : "Drug Discovery and Development",
                "Eukaryotic Single Cell Genomics" : "Genomics",
                "Genome Engineering Zebrafish" : "Chemical Biology and Genome Engineering",
                "High Throughput Genome Engineering" : "Chemical Biology and Genome Engineering",
                "In Situ Sequencing" : "Genomics",
                "Long-term Support (WABI)" : "Bioinformatics",
                "Mass Cytometry (KI)" : "Proteomics and Metabolomics",
                "Mass Cytometry (LiU)" : "Proteomics and Metabolomics",
                "Microbial Single Cell Genomics" : "Genomics",
                "NGI Stockholm" : "Genomics",
                "NGI Uppsala SNP&SEQ" : "Genomics",
                "NGI Uppsala UGC" : "Genomics",
                "PLA and Single Cell Proteomics" : "Proteomics and Metabolomics",
                "Plasma Profiling" : "Proteomics and Metabolomics",
                "Protein Science Facility" : "Cellular and Molecular Imaging",
                "Support and Infrastructure" : "Bioinformatics",
                "Swedish Metabolomics Centre" : "Proteomics and Metabolomics",
                "Swedish NMR Centre" : "Cellular and Molecular Imaging",
                "Systems Biology" : "Bioinformatics"}};


var userInfoString = window.atob("{dstr}");
'''

# Created/order adjusted manually depending after getting the list of affliation and facility
# Basically if the input file changes, after first time running the script, the following
# variable should be checked if need to be adjusted manually

aff_label = ['Chalmers University', 'KTH Royal Institute', 'Karolinska Institute', 'Linkopings university',
             'Lunds university', 'Naturhistoriska Riksmuseet', 'Stockholms university',
             'Swedish University of Agricultural Sciences', 'Umea university', 'Goteborgs university',
             'Uppsala university', 'Other Swedish University', 'Other Swedish organization',
             'International University', 'Other international organization', 'Healthcare', 'Industry'];


sheets_interested = ['All except NGISthlm', 'NGI-STHLM']

def get_org_from_email(email):
    domain = uemail.split('@')[-1]
    ext = domain.split('.')[-1]
    key = domain.split('.')[-2]
    return organization_map.get(key, "Others")

def validate_email(email):
    is_valid = True
    if email == None:
        is_valid = False
    elif isinstance(email, int):
        is_valid = False
    elif '@' not in email:
        is_valid = False
    elif '.' not in email.split('@')[-1]:
        is_valid = False
    return is_valid

def fix_spl_char(value):
    if value == None:
        value = ''
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'), 'utf-8')

user_file = "Input file provided by OO"
sdata = []
ulist_wb = load_workbook(filename=user_file, read_only=True)
ulist_all_ws = ulist_wb['Sheet1']
fac_list = set()
org_list = set()
pla_list = set()
ulist_compiled = ["Num\tUser_email\tOrganisation\tFacility\tPlatform"]

for rnum, row in enumerate(ulist_all_ws.rows):
    if rnum == 0:
        continue
    
    fname = fix_spl_char(row[0].value)
    if not fname:
        print("WARN: On row {}, fname '{}' is not valid".format(rnum, fname))
        continue
    elif fname == "Compute and Storage":
        continue
    fac_list.add(fname)
    
    uemail = row[2].value
    if not validate_email(uemail):
        print("WARN: On row {}, email '{}' is not valid".format(rnum, uemail))
        continue
    
    oname = fix_spl_char(row[3].value)
    if not oname:
        print("WARN: On row {}, oname '{}' is not valid".format(rnum, oname))
        continue
    org_list.add(oname)
    
    pname = fix_spl_char(row[1].value)
    if not pname:
        print("WARN: On row {}, pname '{}' is not valid".format(rnum, pname))
        continue
    pla_list.add(pname)
    
    ulist_compiled.append("\t".join([str(rnum), uemail, oname, fname, pname]))

fac_list = list(fac_list)
org_list = list(org_list)
pla_list = list(pla_list)

# Creates a JS output file, which is fed to 'distribution_plots.html'
# Creates a txt output, for possible manual reference if needed
with open("All_user_list_eng.txt", "w") as ufl, open("user_content.js", "w") as ujs:
    dstring = "\n".join([fix_spl_char(u) for u in ulist_compiled])
    ufl.write(dstring + "\n")
    ujs.write(js_file_temp.format(fac_list=fac_list, org_list=org_list, aff_label=aff_label, pla_list=pla_list, dstr=str(base64.b64encode(dstring.encode('utf-8')), 'utf-8')))
