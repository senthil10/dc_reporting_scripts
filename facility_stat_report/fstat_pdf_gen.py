#/usr/bin/env python
# -*- coding: utf-8 -*-

# Script that generates facility stat plots for the facilities in 'fac_map'
# The script fstat_data_gen.py should be run before running this script
# All the direct dependecy scripts are needed which are
# fstat_plots_gen.py - that generates individual plots to be in pdf
# fstat_reportlab_doc.py - that has a class which will be used to create custom frame etc
# fstat_reportlab_facility_data.py - which contains the individual tweak values for all facilities
# fstat_import_data.py - which has the data to generate the plot from
# the above file is actually an output of 'fstat_data_gen.py' script


import base64
import unicodedata
import json

# Specific imports from reportlab 
from reportlab.platypus import Paragraph, Spacer, FrameBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER

from svglib.svglib import svg2rlg

from openpyxl import load_workbook

from fstat_plots_gen import user_plot, publication_plot
from fstat_reportlab_doc import report_lab_obj
from fstat_reportlab_facility_data import facility_graph_data
from fstat_import_data import affiliation_data, facility_data, fac_map

def fix_spl_char(value):
    if value == None:
        value = ''
    elif not isinstance(value, unicode):
        value = unicode(str(value), 'utf-8')
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'))

def get_image_story(impath, imw=80, imh=60, title=None, style=None):
    out_story = [FrameBreak()]
    img = svg2rlg(impath)
    scaling_factor = imw*mm/img.width
    img.width = imw*mm
    img.height = imh*mm
    img.scale(scaling_factor, scaling_factor)
    out_story.append(img)
    if title and style:
        out_story.append(Paragraph("<font color='#95C11E' name=Arial-bold>{}</font>".format(title), style))
    return out_story


years_to_work = [2017, 2018, 2019]

fac_map = {'Centre for Cellular Imaging' : ['Centre for Cellular Imaging']}

# register font to use
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-bold', 'Arial Bold.ttf'))

# define styles which are mandatory for paragraph elements
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="big_inner_heading", parent=styles["Heading1"], fontName="Arial",
                          fontSize=12.5, color="#FF00AA", leading=15))

styles.add(ParagraphStyle(name="big_page_text", parent=styles["Normal"], fontName="Arial",
                          fontSize=11, bold=0, color="#000000", leading=14))

styles.add(ParagraphStyle(name="medium_inner_heading", parent=styles["Heading1"], fontName="Arial",
                          fontSize=12, color="#FF00AA", leading=12, afterspace=0))

styles.add(ParagraphStyle(name="medium_page_text", parent=styles["Normal"], fontName="Arial",
                          fontSize=10.5, bold=0, color="#000000", leading=12))

styles.add(ParagraphStyle(name="small_inner_heading", parent=styles["Heading1"], fontName="Arial",
                          fontSize=11, color="#FF00AA", leading=11, afterspace=0))

styles.add(ParagraphStyle(name="small_page_text", parent=styles["Normal"], fontName="Arial",
                          fontSize=9.5, bold=0, color="#000000", leading=11))


styles.add(ParagraphStyle(name="bar_plot_title", parent=styles["Heading1"], fontName="Arial",
                          fontSize=12, color="#FF00AA", spaceBefore=7, alignment=TA_CENTER))

styles.add(ParagraphStyle(name="pie_plot_title", parent=styles["Heading1"], fontName="Arial",
                          fontSize=12, color="#FF00AA", alignment=TA_CENTER))

styles.add(ParagraphStyle(name="no_data_info", parent=styles["Heading1"], fontName="Arial",
                          fontSize=17, color="#FF00AA", spaceBefore=0, alignment=TA_CENTER))


# Generate facility stat plot for all facilities
for fac in fac_map.keys():
    
    # pdf frame size and constant values
    pads, ncols, nrows, show_bound = (1*mm, 3, 2, 0)
    
    fac_eng = fix_spl_char(fac)
    fac_fname = fac_eng.replace(",", "")
    fac_stat = facility_data[fac_eng]
    fac_grph = facility_graph_data.get(fac_eng, {})
    
    head_style, text_style = fac_grph.get("style", ("big_inner_heading", "big_page_text"))
    caller_dict = {}
    all_frame_names = ['fstat', 'ctbar', 'jfbar', 'usr17', 'usr18', 'usr19']
    frames_to_work = fac_grph.get('frames', {}).get('flist', all_frame_names)[1:]
    
    # set base template
    fac_replab = report_lab_obj(**fac_grph.get("doc", {"fname":"/Users/senpa282/opt/publication_reporting/facility_stat_plot/pdfs/{}.pdf".format(fac_eng)}))
    
    story = []
    
    # Put in the facility stat
    story.append(Paragraph("<font color='#95C11E' name=Arial-bold>Basic Information</font>", styles[head_style]))
    if fac == "Drug Discovery and Development":
        story.append(Paragraph("<font name=Arial-bold>Platform director:</font> {}".format(fac_stat['fd']), styles[text_style]))
        story.append(Paragraph("<font name=Arial-bold>Head of platform:</font> {}".format(fac_stat['fh']), styles[text_style]))
        story.append(Paragraph("<font name=Arial-bold>SciLifeLab platform since:</font> {}".format(fac_stat['sf']), styles[text_style]))
    else:
        story.append(Paragraph("<font name=Arial-bold>Facility director:</font> {}".format(fac_stat['fd']), styles[text_style]))
        story.append(Paragraph("<font name=Arial-bold>Head of facility:</font> {}".format(fac_stat['fh']), styles[text_style]))
        story.append(Paragraph("<font name=Arial-bold>SciLifeLab facility since:</font> {}".format(fac_stat['sf']), styles[text_style]))
    story.append(Paragraph("<font name=Arial-bold>Host University:</font> {}".format(fac_stat['hu']), styles[text_style]))
    story.append(Paragraph("<font name=Arial-bold>FTEs:</font> {}".format(fac_stat['fte']), styles[text_style]))
    story.append(Paragraph("<font name=Arial-bold>FTEs financed by SciLifeLab:</font> {}".format(fac_stat['sfte']), styles[text_style]))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("<font color='#95C11E' name=Arial-bold>Funding 2020 (in kSEK)</font>", styles[head_style]))
    story.append(Paragraph("<font name=Arial-bold>SciLifeLab:</font> {}".format(fac_stat['sfund']), styles[text_style]))
    story.append(Paragraph("<font name=Arial-bold>Total:</font> {}".format(fac_stat['tfund']), styles[text_style]))
    
    
    cat_plot, jif_plot, pub_stat = publication_plot(fac_map[fac], 2019, "svg")
    
    if any(pub_stat):
        caller_dict['ctbar'] = dict(impath=cat_plot, title="Publications by category", style=styles["bar_plot_title"], **fac_grph.get("figsize", {}).get("cat", {}))
        caller_dict['jfbar'] = dict(impath=jif_plot, title="Publications by JIF", style=styles["bar_plot_title"], **fac_grph.get("figsize", {}).get("jif", {}))
        if 'ctbar' not in frames_to_work or 'jfbar' not in frames_to_work:
            exit("ERROR: For facility '{}' bar plot available but frame not mentioned in '{}'".format(fac, frames_to_work))
        
    if fac_eng in affiliation_data.keys():
        if 2017 in affiliation_data[fac_eng]:
            u17_plot = user_plot(affiliation_data[fac_eng][2017], fac, str(2017), "_{}".format(str(2017)), "svg")
            caller_dict['usr17'] = dict(impath=u17_plot, title="Users 2017", style=styles["pie_plot_title"], **fac_grph.get("figsize", {}).get("u17", {}))
            if 'usr17' not in frames_to_work:
                exit("ERROR: For facility '{}' user plot 2017 available but frame not mentioned in '{}'".format(fac, frames_to_work))
        else:
            print "WARN: No user plots for facility '{}', year 2017".format(fac)           
            
        if 2018 in affiliation_data[fac_eng]:
            u18_plot = user_plot(affiliation_data[fac_eng][2018], fac, str(2018), "_{}".format(str(2018)), "svg")
            caller_dict['usr18'] = dict(impath=u18_plot, title="Users 2018", style=styles["pie_plot_title"], **fac_grph.get("figsize", {}).get("u18", {}))
            if 'usr18' not in frames_to_work:
                exit("ERROR: For facility '{}' user plot 2018 available but frame not mentioned in '{}'".format(fac, frames_to_work))
        else:
            print "WARN: No user plots for facility '{}', year 2018".format(fac)
        
        if 2019 in affiliation_data[fac_eng]:
            u19_plot = user_plot(affiliation_data[fac_eng][2019], fac, str(2019), "_{}".format(str(2019)), "svg")
            caller_dict['usr19'] = dict(impath=u19_plot, title="Users 2019", style=styles["pie_plot_title"], **fac_grph.get("figsize", {}).get("u19", {}))
            if 'usr19' not in frames_to_work:
                exit("ERROR: For facility '{}' user plot 2019 available but frame not mentioned in '{}'".format(fac, frames_to_work))
        else:
            print "WARN: No user plots for facility '{}', year 2019".format(fac)
    else:
        print "WARN: No user plots for facility '{}' all years".format(fac)
    
    # call for frames
    for frm in frames_to_work:
        if frm in caller_dict:
            story.extend(get_image_story(**caller_dict[frm]))
        else:
            story.append(FrameBreak())
    
    fac_replab.make_page_templates(**fac_grph.get("frames", {}))
    fac_replab.doc.build(story)








