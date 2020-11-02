#!/usr/bin/env python

# Script to generate files from web form (reports submitted by facilities) info

import collections
import datetime
import glob
import json
import os
import pandas
import requests
import string
import urllib
import xlsxwriter

platform_map = {"Advanced Light Microscopy (ALM)" : "Cellular and Molecular Imaging",
                "Ancient DNA" : "Genomics",
                "Autoimmunity Profiling" : "Proteomics and Metabolomics",
                "BioImage Informatics" : "Cellular and Molecular Imaging",
                "Cell Profiling" : "Cellular and Molecular Imaging",
                "Chemical Biology Consortium Sweden" : "Chemical Biology and Genome Engineering",
                "Chemical Proteomics and Proteogenomics (MBB)" : "Proteomics and Metabolomics",
                "Chemical Proteomics and Proteogenomics (OnkPat)" : "Proteomics and Metabolomics",
                "Clinical Genomics Göteborg" : "Diagnostics Development",
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
                "Systems Biology" : "Bioinformatics"}   

file_names = {
              "infra" : "merged_files/A_Infrastructure Single Data Reported 2019.xlsx",
              "heads" : "merged_files/B_Infrastructure FD and HF 2019.xlsx",
              "funds" : "merged_files/C_Infrastructure Other Funding 2019.xlsx",
              "props" : "merged_files/D_Infrastructure Immaterial Property Rights 2019.xlsx",
              "users" : "merged_files/E_Infrastructure Users 2019.xlsx",
              "cours" : "merged_files/F_Infrastructure Courses 2019.xlsx",
              "confs" : "merged_files/G_Infrastructure Conferences Symposia Seminars 2019.xlsx",
              "colab" : "merged_files/H_Infrastructure External Collaborations 2019.xlsx"
    }

keys_needed = {
               "infra" : ["personnel_count", "personnel_count_male", "personnel_count_phd", "personnel_count_phd_male",
                          "fte", "fte_scilifelab", "eln_usage", "resource_academic_national", "resource_academic_international",
                          "resource_internal", "resource_industry", "resource_healthcare", "resource_other", "total_user_fees",
                          "user_fee_models", "user_fees", "user_fees_academic_sweden", "user_fees_academic_international",
                          "user_fees_industry", "user_fees_healthcare", "user_fees_other", "cost_reagents", "cost_instrument",
                          "cost_salaries", "cost_rents", "cost_other", "number_projects", "user_feedback", "innovation_utilization",
                          "technology_development", "scientific_achievements"],
               "heads" : ["facility", "facility_director", "facility_head"],
               "funds" : ["facility", "additional_funding"],
               "props" : ["facility", "immaterial_property_rights"]
    }

files_info = {
              "infra" : [["Facility", "Platform", "Personnel count", "Personnel count male", "Personnel count Phd", "Personnel count Phd male",
                         "FTE", "FTE Scilifelab", "ELN usage", "Resource academic national", "Resource academic international",
                         "Resource internal", "Resource industry", "Resource healthcare", "Resource other", "Total user fees",
                         "User fee models", "User fees", "User fees academic Sweden", "User fees academic international",
                         "User fees industry", "User fees healthcare", "User fees other", "Cost reagents", "Cost instrument",
                         "Cost salaries", "Cost rents", "Cost other", "#Projects", "User feedback", "Innovation utilization",
                         "Technology development", "Scientific achievements"]],
                         
              "heads" : [],
              
              "funds" : [["Facility", "Platform", "Category of financier", "Name/type of financier", "Amount (kSEK)"]],
              
              "props" : [["Facility", "Platform", "Patent title", "Patent application number", "Filed or granted during 2018?",
                          "Registered designs", "Registered trademarks"]],
              
              "users" : [["1. Name of reporting unit* (choose from drop-down menu)", "2. Platform", "3. Your e-mail address*",
                          "4a. First name of the responsible PI*", "4b. Surname of the responsible PI*", "5. E-mail address of responsible PI*",
                          "6a. Affiliation of PI: Specific university or category (choose from drop-down menu)*",
                          "6b. For non-specific universities and categories in 5a, name the organization (free text)"]],
                          
              "cours" : [["1. Name of reporting unit* (choose from drop-down menu)", "2. Platform", "3. Your e-mail address*",
                          "4. Full name of the course*", "5a. Did the reporting unit organize or co-organize the course?*",
                          "5b. If co-organized, with whom?", "6. Start date* (yyyy-mm-dd)", "7. End date* (yyyy-mm-dd)",
                          "8. Location (city) of the course*", "9. Comment"]],
                          
              "confs" : [["1. Name of reporting unit* (choose from drop-down menu)", "2. Platform ", "3. Your e-mail address*",
                          "4. Name of activity*", "5a. Did the reporting unit organize or co-organize this activity?*", "5b. If co-organized, with whom?",
                          "6. Start date* (yyyy-mm-dd)", "7. End date* (yyyy-mm-dd)", "8. Location (city) of activity *", "9. Comment"]],
              
              "colab" : [["1. Name of reporting unit* (choose from drop-down menu)", "2. Platform", "3. Your e-mail address*",
                          "4. Name of external organization*", "5. Type of organization* (choose from drop-down menu)", "6. Reference person",
                          "7. Purpose of collabaration/alliance*"]]
}

files_list = collections.defaultdict(list)

def get_submitted_reports():
    reports_list = []
    reports_url = "facility report API url" #real URL should be given
    api_headers = {'X-OrderPortal-API-key': "API_KEY"} #real key should be given
    resp = requests.get(reports_url, headers=api_headers)
    repall = resp.json()
    for rep in repall["items"]:
        rurl = rep["links"]["api"]["href"]
        rres = requests.get(rurl, headers=api_headers)
        reports_list.append(rres.json())
    return reports_list

def download_file(url, path, fname=None):
    if fname:
        local_filename = fname
    else:
        local_filename = u''.join(filter(lambda x: x in string.printable, urllib.request.url2pathname(url.split('/')[-1])))
    api_headers = {'X-OrderPortal-API-key': API_KEY}
    with requests.get(url, stream=True, headers=api_headers) as r:
        r.raise_for_status()
        with open("{}/{}".format(path, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk:
                    f.write(chunk)
    return local_filename

def get_sheet_rows(excel, sname):
    rlist = []
    sheet = excel.parse(sname)
    read_row = False
    for i, row in sheet.iterrows():
        if isinstance(row[0], str) and row[0].startswith('1.'):
            read_row = True
            continue
        if not read_row:
            continue
        r = row.fillna('').to_list()
        if read_row and r[0] == '':
            read_row = False
            continue
        fac = r[0][0].upper() + r[0][1:]
        r.insert(1, platform_map[fac.strip()])
        r[0] = fac
        rlist.append([datetime.datetime.strftime(i, "%Y-%m-%d") if isinstance(i, datetime.datetime) else i for i in r])
    return rlist

all_reports = get_submitted_reports()
for report in all_reports:

    facility = report["fields"]["facility"] if report['identifier'] != "SFR00173" else "In Situ Sequencing"
    platform = platform_map[facility]
    # info for infra file
    iinfo = [facility, platform]
    iinfo.extend([report["fields"][k] for k in keys_needed["infra"]])
    files_info["infra"].append(iinfo)

    # info for head file
    hinfo = [facility, platform]
    hinfo.extend(list(map(lambda x: "\n".join(x), zip(*report["fields"]["facility_director"]))))
    hinfo.extend(list(map(lambda x: "\n".join(x), zip(*report["fields"]["facility_head"]))))
    files_info["heads"].append(hinfo)

    # info for funding
    finfo = [facility, platform]
    fnd = report['fields']['additional_funding']
    if len(fnd) > 1:
        finfo.extend(fnd)
        files_info['funds'].append(finfo)
    elif len(fnd) == 1:
        finfo.extend(fnd[0])
        files_info['funds'].append(finfo)

    # info for patent
    pinfo = [facility, platform]
    pat = report['fields']['immaterial_property_rights']
    if len(pat) > 1:
        pinfo.extend(pat)
        files_info['props'].append(pinfo)
    elif len(pat) == 1:
        pinfo.extend(pat[0])
        files_info['props'].append(pinfo)

    # collect file list
    for fname in report["files"]:
        files_list[facility].append(report["files"][fname]["href"])
        # if 'kpi' in fname.lower() or 'key' in fname.lower():
        #     dfl = download_file(report["files"][fname]["href"], "report_attachments/kpi_data", "{} KPI Data 2019{}".format(facility, os.path.splitext(fname)[-1]))
        # elif not fname.strip().endswith('xlsm') and not fname.strip().endswith('xlsx'):
        #     dfl = download_file(report["files"][fname]["href"], "report_attachments/reporting_data", "{} Reporting 2019{}".format(facility, os.path.splitext(fname)[-1]))
        # if 'budget' in fname.lower():
        #     dfl = download_file(report["files"][fname]["href"], "report_attachments/budget_data", "{} Budget Data{}".format(facility, os.path.splitext(fname)[-1]))
        # if 'volume' in fname.lower() or fname in ['Clinical_Genomics_Gothenburg_1.xlsm', 'Genome Engineering Zebrafish 2019_1.xlsm']:
        #     dfl = download_file(report["files"][fname]["href"], "report_attachments/volume_data", "{} Volume Data 2019{}".format(facility, os.path.splitext(fname)[-1]))

#Download all the files for all reports
# for fc_name, fl_list in files_list.items():
#     for fl in fl_list:
#         lfl = download_file(fl, "report_files")

# Parse volume data files
for vfl in glob.glob("report_attachments/volume_data/*Volume Data 2019*"):
    xl = pandas.ExcelFile(vfl)
    files_info['users'].extend(get_sheet_rows(xl, 'A. Users'))
    files_info['cours'].extend(get_sheet_rows(xl, 'B. Courses'))
    files_info['confs'].extend(get_sheet_rows(xl, 'C. Conf, symp, semin'))
    files_info['colab'].extend(get_sheet_rows(xl, 'D. External Collab '))

# Creating infra excel file
infra_wbook = xlsxwriter.Workbook(file_names['infra'])

head_text_format = infra_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = infra_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = infra_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

infra_wsheet = infra_wbook.add_worksheet()
infra_wsheet.freeze_panes(1, 2)
infra_wsheet.set_row(0, None, head_text_format)
infra_wsheet.set_column(0, 1, 40, normal_text_format)
infra_wsheet.set_column(2, 29, 20, normal_text_format)
infra_wsheet.set_column(30, 32, 100, long_text_format)

for row, rdata in enumerate(files_info["infra"]):
    infra_wsheet.write_row(row, 0, rdata)

infra_wbook.close()


# Creating facility head excel file
heads_wbook = xlsxwriter.Workbook(file_names['heads'])
head_text_format = heads_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = heads_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = heads_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

heads_wsheet = heads_wbook.add_worksheet()
heads_wsheet.freeze_panes(2, 2)
heads_wsheet.set_row(0, None, head_text_format)
heads_wsheet.set_row(1, None, head_text_format)
heads_wsheet.merge_range(0, 0, 1, 0, "Facility")
heads_wsheet.merge_range(0, 1, 1, 1, "Platform")
heads_wsheet.merge_range(0, 2, 0, 5, "Facility director")
heads_wsheet.merge_range(0, 6, 0, 9, "Facility heads")
heads_wsheet.write_row(1, 2, ["First Name", "Last Name", "Email", "Affliation"])
heads_wsheet.write_row(1, 6, ["First Name", "Last Name", "Email", "Affliation"])

heads_wsheet.set_column(0, 1, 40, long_text_format)
heads_wsheet.set_column(2, 3, 20, long_text_format)
heads_wsheet.set_column(4, 4, 40, long_text_format)
heads_wsheet.set_column(5, 7, 20, long_text_format)
heads_wsheet.set_column(8, 8, 40, long_text_format)
heads_wsheet.set_column(9, 9, 20, long_text_format)

for row, rdata in enumerate(files_info["heads"], 2):
    heads_wsheet.write_row(row, 0, rdata)

heads_wbook.close()


# Creating funding excel file
funds_wbook = xlsxwriter.Workbook(file_names['funds'])
head_text_format = funds_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = funds_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = funds_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

funds_wsheet = funds_wbook.add_worksheet()
funds_wsheet.freeze_panes(1, 2)
funds_wsheet.set_row(0, None, head_text_format)
funds_wsheet.set_column(0, 3, 40, long_text_format)
funds_wsheet.set_column(4, 4, 20, long_text_format)

row = 0
for rdata in files_info["funds"]:
    if isinstance(rdata[2], list):
        nrow = len(rdata) - 3
        funds_wsheet.merge_range(row, 0, row + nrow, 0, rdata[0])
        funds_wsheet.merge_range(row, 1, row + nrow, 1, rdata[1])
        for cdata in rdata[2:]:
            funds_wsheet.write_row(row, 2, cdata)
            row += 1
    else:
        funds_wsheet.write_row(row, 0, rdata)
        row += 1

funds_wbook.close()


# Creating props excel file
props_wbook = xlsxwriter.Workbook(file_names['props'])
head_text_format = props_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = props_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = props_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

props_wsheet = props_wbook.add_worksheet()
props_wsheet.freeze_panes(1, 2)
props_wsheet.set_row(0, None, head_text_format)
props_wsheet.set_column(0, 2, 40, long_text_format)
props_wsheet.set_column(3, 6, 20, long_text_format)

row = 0
for rdata in files_info["props"]:
    if isinstance(rdata[2], list):
        nrow = len(rdata) - 3
        props_wsheet.merge_range(row, 0, row + nrow, 0, rdata[0])
        props_wsheet.merge_range(row, 1, row + nrow, 1, rdata[1])
        for cdata in rdata[2:]:
            props_wsheet.write_row(row, 2, cdata)
            row += 1
    else:
        props_wsheet.write_row(row, 0, rdata)
        row += 1

props_wbook.close()


# Creating Users excel file
users_wbook = xlsxwriter.Workbook(file_names['users'])

head_text_format = users_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = users_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = users_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

users_wsheet = users_wbook.add_worksheet()
users_wsheet.freeze_panes(1, 2)
users_wsheet.set_row(0, None, head_text_format)
users_wsheet.set_column(0, 2, 40, normal_text_format)
users_wsheet.set_column(3, 4, 20, normal_text_format)
users_wsheet.set_column(5, 7, 40, normal_text_format)

for row, rdata in enumerate(files_info["users"]):
    users_wsheet.write_row(row, 0, rdata)

users_wbook.close()


# Creating Course excel file
cours_wbook = xlsxwriter.Workbook(file_names['cours'])

head_text_format = cours_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = cours_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = cours_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

cours_wsheet = cours_wbook.add_worksheet()
cours_wsheet.freeze_panes(1, 2)
cours_wsheet.set_row(0, None, head_text_format)
cours_wsheet.set_column(0, 2, 40, normal_text_format)
cours_wsheet.set_column(3, 4, 40, long_text_format)
cours_wsheet.set_column(5, 5, 30, long_text_format)
cours_wsheet.set_column(6, 8, 20, long_text_format)
cours_wsheet.set_column(9, 9, 40, long_text_format)

for row, rdata in enumerate(files_info["cours"]):
    cours_wsheet.write_row(row, 0, rdata)

cours_wbook.close()


# Creating conf excel file
confs_wbook = xlsxwriter.Workbook(file_names['confs'])

head_text_format = confs_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = confs_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = confs_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

confs_wsheet = confs_wbook.add_worksheet()
confs_wsheet.freeze_panes(1, 2)
confs_wsheet.set_row(0, None, head_text_format)
confs_wsheet.set_column(0, 4, 40, long_text_format)
confs_wsheet.set_column(5, 8, 20, long_text_format)
confs_wsheet.set_column(9, 9, 40, long_text_format)

for row, rdata in enumerate(files_info["confs"]):
    confs_wsheet.write_row(row, 0, rdata)

confs_wbook.close()


#Creating colab excel file
colab_wbook = xlsxwriter.Workbook(file_names['colab'])

head_text_format = colab_wbook.add_format({'bold':True, 'text_wrap':True, 'bg_color':'#9ECA7F', 'font_size':15, 'align':'center', 'border':1})
normal_text_format = colab_wbook.add_format({'font_size':14, 'align':'left', 'valign':'vcenter'})
long_text_format = colab_wbook.add_format({'text_wrap':True, 'font_size':14, 'align':'left', 'valign':'vcenter'})

colab_wsheet = colab_wbook.add_worksheet()
colab_wsheet.freeze_panes(1, 2)
colab_wsheet.set_row(0, None, head_text_format)
colab_wsheet.set_column(0, 5, 40, long_text_format)
colab_wsheet.set_column(6, 6, 50, long_text_format)

for row, rdata in enumerate(files_info["colab"]):
    colab_wsheet.write_row(row, 0, rdata)

colab_wbook.close()

#import pdb; pdb.set_trace()
