#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is used in fstat_pdf_gen.py to generate the plots that are to be in the PDF.

import json, time, urllib, os
import unicodedata

#Plotting libs
import plotly
import plotly.graph_objs as go
from adrian_code.colour_science import SCILIFE_COLOURS, FACILITY_USER_AFFILIATION_COLOUR_OFFICIAL
from adrian_code.issn_files import ISSN_IMPACT_2017, ISSN_IMPACT_2016, ISSN_IMPACT_2015, ISSN_TO_ISSNL, ISSNL_TO_ISSN, issn_to_impact
from adrian_code.publications_api import Publications_api

def fix_spl_char(value):
    if value == None:
        value = ''
    elif not isinstance(value, unicode):
        value = unicode(str(value), 'utf-8')
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'))

def publication_plot(label_list, year, pformat="png"):
    url = "https://publications.scilifelab.se/labels.json"
    response = urllib.urlopen(url)
    labels = json.loads(response.read())

    labels_check_dict = dict()
    label_list_no_spl_char = [fix_spl_char(l) for l in label_list]

    for label in labels["labels"]:
#        labels_check_dict[label["value"]] = label["links"]["self"]["href"]
        labels_check_dict[fix_spl_char(label["value"])] = label["links"]["self"]["href"]

    all_publications = list()
    pub_read = list()

    for label in label_list:
        label = fix_spl_char(label)
        if label not in labels_check_dict.keys():
            #import pdb; pdb.set_trace()
            exit("ERROR: Wrong label, does not exist in database {}".format(label))

        url = labels_check_dict[label]
        response = urllib.urlopen(url)
        publications = json.loads(response.read())
        for pub in publications["publications"]:
            if pub not in all_publications:
                all_publications.append(pub)

    years = {
        year:{"Service":0, "Collaborative":0, "Technology development":0, "None":0}, 
        year-1:{"Service":0, "Collaborative":0, "Technology development":0, "None":0}, 
        year-2:{"Service":0, "Collaborative":0, "Technology development":0, "None":0}
    }
    publication_issns = list()
    publication_impacts = {year: [], year-1: [], year-2: []}

#    if 'Bioinformatics Support and Infrastructure' in label_list:
#        import pdb; pdb.set_trace()
    
    for pub in all_publications:
        pub_year = int(pub["published"].split("-")[0])
        if pub_year in years.keys():
            catflag = False
            jifflag = False
            for key in pub["labels"].keys():
#                if key in label_list and not catflag:
                if fix_spl_char(key) in label_list_no_spl_char and not catflag:
                    # Need to use the right label for the category
                    # This WILL break for several labels, categories will be counted several times
                    try:
                        years[pub_year][pub["labels"][key]] += 1
                        catflag = True
                    except KeyError as e:
                        years[pub_year]["None"] += 1
                        catflag = True

            if pub["journal"]["issn"]:
                issn = pub["journal"]["issn"]
                publication_issns.append(issn)
                impact = issn_to_impact(issn)

                # if impact is None:
                #     print "NO IMPACT FACTOR FOUND FOR:", issn, pub["journal"]
                # At the end, add the impact to the list
                publication_impacts[pub_year].append(impact)
                jifflag = True
            else: 
                # NO ISSN
                publication_impacts[pub_year].append(None)
                jifflag = True
                # print "NO ISSN FOUND FOR:", pub["journal"]
            if catflag ^ jifflag:
                print "\n\nERROR THIS SHOULD NEVER HAPPEN. PUBLICATION ADDED TO CATEGORY PLOT BUT NOT JIF PLOT\n\n", pub
                # This should never happen, ie having only one of the flags
                # I added this to make sure all publications are always visible in BOTH graphs

    jif_data = {year-2: [0,0,0,0,0], year-1: [0,0,0,0,0], year: [0,0,0,0,0]}

    for year in publication_impacts.keys():
        for impact in publication_impacts[year]:
            if impact is not None:
                real_impact = float(impact)/1000
                #print real_impact
                if real_impact>25.0:
                    jif_data[year][3] += 1
                    continue
                if real_impact>9.0:
                    jif_data[year][2] += 1
                    continue
                if real_impact>6.0:
                    jif_data[year][1] += 1
                    continue                    
                jif_data[year][0] += 1
            else:
                jif_data[year][4] += 1

    trace_service = go.Bar(
        x=[year-2, year-1, year],
        y=[years[year-2]["Service"], years[year-1]["Service"], years[year]["Service"]],
        width=0.75,
        name="Service ",
        marker=dict(
            color=SCILIFE_COLOURS[2],
            line=dict(color='#000000', width=1)
        )
    )
    trace_collaborative = go.Bar(
        x=[year-2, year-1, year],
        y=[years[year-2]["Collaborative"], years[year-1]["Collaborative"], years[year]["Collaborative"]],
        width=0.75,
        name="Collaborative ",
        marker=dict(
            color=SCILIFE_COLOURS[8],
            line=dict(color='#000000', width=1)
        )
    )
    trace_tech_dev = go.Bar(
        x=[year-2, year-1, year],
        y=[years[year-2]["Technology development"], years[year-1]["Technology development"], years[year]["Technology development"]],
        width=0.75,
        name="Technology<br>development ", 
        marker=dict(
            color=SCILIFE_COLOURS[4],
            line=dict(color='#000000', width=1)
        )
    )
    trace_none = go.Bar(
        x=[year-2, year-1, year],
        y=[years[year-2]["None"], years[year-1]["None"], years[year]["None"]],
        width=0.75,
        name="No category ",
        marker=dict(
            color=SCILIFE_COLOURS[5],
            line=dict(color='#000000', width=1)
        )
    )

    if (years[year-2]["None"] or years[year-1]["None"] or years[year]["None"]):
        data = [trace_none, trace_service, trace_collaborative, trace_tech_dev]
    else:
        data = [trace_service, trace_collaborative, trace_tech_dev]

    highest_y_value = max(
        years[year-2]["None"]+years[year-2]["Technology development"]+years[year-2]["Collaborative"]+years[year-2]["Service"],
        years[year-1]["None"]+years[year-1]["Technology development"]+years[year-1]["Collaborative"]+years[year-1]["Service"],
        years[year]["None"]+years[year]["Technology development"]+years[year]["Collaborative"]+years[year]["Service"]
    )
    yaxis_tick = 1
    if highest_y_value>10:
        yaxis_tick = 2
    if highest_y_value>20:
        yaxis_tick = 5
    if highest_y_value>50:
        yaxis_tick = 10
    if highest_y_value>100:
        yaxis_tick = 20
    if highest_y_value>150:
        yaxis_tick = 40
    if highest_y_value>200:
        yaxis_tick = 50
    if highest_y_value>1000:
        yaxis_tick = 100

    layout = go.Layout(
        barmode='stack',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=go.layout.Margin(
            l=60,
            r=50,
            b=50,
            t=30,
            pad=4
        ),
        # title=dict(
        #     text="<b>Publications by Category</b>",
        #     font=dict(family="Arial", size=32, color="#95C11E"),
        #     x=0.20,
        #     y=0.03
        # ),
        xaxis=dict(
            showticklabels=True, 
            dtick=1,
            zeroline=True,
            tickfont=dict(family='Arial', size=28)
        ),
        yaxis=dict(
#            domain=[0.12, 1],
            showticklabels=True,
            dtick=yaxis_tick,
            tickfont=dict(family='Arial', size=28),
            range=[0, int(highest_y_value*1.15)] # Set the ylim slightly higher than the max value for a prettier graph
        ),
        legend=dict(
            traceorder='reversed',
            font=dict(family='Arial', size=22),
            bordercolor="#5a5c60",
            borderwidth=0.6
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.io.write_image(fig, 'facility_onepagers_figures/pub_plot/{}_category.{}'.format(label_list[0].lower().replace(" ", "_").replace(",", ""), pformat))
#                          height=1150, width=1500, scale=3)

    total_pubs_lastlast_year = years[year-2]["None"]+years[year-2]["Technology development"]+years[year-2]["Collaborative"]+years[year-2]["Service"]
    total_pubs_last_year = years[year-1]["None"]+years[year-1]["Technology development"]+years[year-1]["Collaborative"]+years[year-1]["Service"]
    total_pubs_current_year = years[year]["None"]+years[year]["Technology development"]+years[year]["Collaborative"]+years[year]["Service"]

    jif_unknown = go.Bar(
        x=[year-2, year-1, year],
        y=[jif_data[year-2][4], jif_data[year-1][4], jif_data[year][4]],
        name="JIF unknown ",
        width=0.75,
        marker=dict(
            color=SCILIFE_COLOURS[5],
            line=dict(color='#000000', width=1)
        )
    )
    jif_low = go.Bar(
        x=[year-2, year-1, year],
        y=[jif_data[year-2][0], jif_data[year-1][0], jif_data[year][0]],
        name="JIF < 6 ",
        width=0.75,
        marker=dict(
            color=SCILIFE_COLOURS[0],
            line=dict(color='#000000', width=1)
        )
    )
    jif_mediocre = go.Bar(
        x=[year-2, year-1, year],
        y=[jif_data[year-2][1], jif_data[year-1][1], jif_data[year][1]],
        name="JIF = 6 - 9 ",
        width=0.75,
        marker=dict(
            color=SCILIFE_COLOURS[7],
            line=dict(color='#000000', width=1)
        )
    )
    jif_good = go.Bar(
        x=[year-2, year-1, year],
        y=[jif_data[year-2][2], jif_data[year-1][2], jif_data[year][2]],
        name="JIF = 9 - 25 ",
        width=0.75,
        marker=dict(
            color=SCILIFE_COLOURS[9],
            line=dict(color='#000000', width=1)
        )
    )
    jif_high = go.Bar(
        x=[year-2, year-1, year],
        y=[jif_data[year-2][3], jif_data[year-1][3], jif_data[year][3]],
        name="JIF > 25 ",
        width=0.75,
        marker=dict(
            color=SCILIFE_COLOURS[1],
            line=dict(color='#000000', width=1)
        )
    )

    if (jif_data[year-2][4] or jif_data[year-1][4] or jif_data[year][4]):
        jif_fig_data = [jif_unknown, jif_low, jif_mediocre, jif_good, jif_high]
    else:
        jif_fig_data = [jif_low, jif_mediocre, jif_good, jif_high]

    jif_layout = go.Layout(
        barmode="stack",
        plot_bgcolor='rgba(0,0,0,0)',
        margin=go.layout.Margin(
            l=60,
            r=50,
            b=50,
            t=30,
            pad=4
        ),
        # title=dict(
        #     text="<b>Publications by JIF</b>",
        #     font=dict(family="Arial", size=32, color="#95C11E"),
        #     x=0.25,
        #     y=0.03
        # ),
        xaxis=dict(
            showticklabels=True, 
            dtick=1,
            zeroline=True,
            tickfont=dict(family='Arial', size=28)
        ),
        yaxis=dict(
#            domain=[0.12, 1],
            showticklabels=True,
            dtick=yaxis_tick,
            tickfont=dict(family='Arial', size=28),
            range=[0, int(highest_y_value*1.15)] # Set the ylim slightly higher than the max value for a prettier graph
        ),
        legend=dict(
            traceorder='reversed',
            font=dict(family='Arial', size=22),
            bordercolor="#5a5c60",
            borderwidth=0.6
            )
        )
    
        
    jif_fig = go.Figure(data=jif_fig_data, layout=jif_layout)
    plotly.io.write_image(jif_fig, 'facility_onepagers_figures/pub_plot/{}_jif.{}'.format(label_list[0].lower().replace(" ", "_").replace(",", ""), pformat))
#                          height=1150, width=1500, scale=3)

    return (
        '{}/facility_onepagers_figures/pub_plot/{}_category.{}'.format(os.getcwd(), label_list[0].lower().replace(" ", "_").replace(",", ""), pformat),
        '{}/facility_onepagers_figures/pub_plot/{}_jif.{}'.format(os.getcwd(), label_list[0].lower().replace(" ", "_").replace(",", ""), pformat),
        (total_pubs_current_year, total_pubs_last_year, total_pubs_lastlast_year)
    )
    

def user_plot(user_affiliation_data, fac, year="2019", prefix=None, pformat="png"):
    aff_map_abbr = {
        "Chalmers University of Technology": "Chalmers",
        "KTH Royal Institute of Technology": "KTH",
        "Swedish University of Agricultural Sciences": "SLU",
        "Karolinska Institutet": "KI",
        "Linköping University": "LiU",
        "Lund University": "LU",
        "Naturhistoriska Riksmuséet": "NRM",
        "Naturhistoriska Riksmuseet": "NRM",
        "Stockholm University": "SU",
        "Umeå University": "UmU",
        "University of Gothenburg": "GU",
        "Uppsala University": "UU",
        "Örebro University": "OU",
        "International University": "Int Univ",
        "Other Swedish University" : "Other Swe{}Univ".format("<br>" if fac=='Chemical Proteomics' else " "),
        "Other Swedish organization" : "Other Swe Org",
        "Other international organization" : "Other Int Org",
        "Industry": "Industry",
        "Healthcare": "Healthcare" + ("<br>" if fac=='Clinical Genomics Gothenburg' else ""),
        "National University Ireland Galway": "National University<br>Ireland Galway"
    }

    if not os.path.isdir("facility_onepagers_figures/"):
        os.mkdir("facility_onepagers_figures/")

    fn = fix_spl_char(fac).lower().replace(" ", "_").replace(",", "") + (prefix if prefix else '')
    user_fig_name = '{}/facility_onepagers_figures/user_plot/{}_user.{}'.format(os.getcwd(), fn, pformat)

    values = []
    labels = []

    for institution in user_affiliation_data.keys():
        if user_affiliation_data[institution]:
            values.append(user_affiliation_data[institution])
            labels.append(institution)
    
    if sum(values) < 2:
        pi_plural = "PI"
    else:
        pi_plural = "PIs"
    
    # Set font sizes for exceptional case
    font_size, title_size = (25, 37)
    if (fac=="Compute and Storage"):
        font_size, title_size = (23, 31)
    elif (fac=="National Genomics Infrastructure" and year=="2017"):
        font_size, title_size = (23, 32)
    elif (fac=="National Genomics Infrastructure" and year=="2018"):
        font_size, title_size = (22, 32)
    elif (fac=="National Genomics Infrastructure" and year=="2019"):
        font_size, title_size = (22, 32)
    elif (fac=="AIDA Data Hub" and year=="2019"):
        font_size, title_size = (22, 35)
    elif (fac=="BioImage Informatics" and year=="2017"):
        font_size, title_size = (29, 38)
    elif (fac=="Support, Infrastructure and Training" and year=="2017"):
        font_size, title_size = (24, 36)
    elif (fac=="Support, Infrastructure and Training" and year=="2018"):
        font_size, title_size = (22, 36)
    elif (fac=="Support, Infrastructure and Training" and year=="2019"):
        font_size, title_size = (22, 36)
    elif (fac=="Advanced Light Microscopy" and year=="2017"):
        font_size, title_size = (28, 38)
    elif (fac=="Intravital Microscopy Facility" and year=="2018"):
        font_size, title_size = (28, 42)
    elif (fix_spl_char(fac)=="Biochemical Imaging Centre Umea" and year=="2017"):
        font_size, title_size = (30, 45)
    elif (fix_spl_char(fac)=="Biochemical Imaging Centre Umea" and year=="2018"):
        font_size, title_size = (22, 37)
    elif (fix_spl_char(fac)=="Biochemical Imaging Centre Umea" and year=="2019"):
        font_size, title_size = (22, 37)
    elif (fac=="Cryo-EM" and year=="2017"):
        font_size, title_size = (30, 42)
    elif (fac=="National Resource for Mass Spectrometry Imaging" and year=="2018"):
        font_size, title_size = (32, 44)
    elif (fac=="Gothenburg Imaging Mass Spectrometry" and year=="2017"):
        font_size, title_size = (24, 36)
    elif (fac=="Chemical Biology Consortium Sweden" and year=="2017"):
        font_size, title_size = (26, 39)
    elif (fac=="Chemical Proteomics" and year=="2017"):
        font_size, title_size = (29, 42)
    elif (fac=="Genome Engineering Zebrafish" and year=="2017"):
        font_size, title_size = (26, 38)
    elif (fac=="High Throughput Genome Engineering" and year=="2018"):
        font_size, title_size = (26, 38)
    elif (fac=="Clinical Genomics Gothenburg" and year=="2017"):
        font_size, title_size = (26, 38)
    elif (fac=="Clinical Genomics Lund" and year=="2018"):
        font_size, title_size = (26, 38)
    elif (fac=="Clinical Genomics Uppsala" and year=="2017"):
            font_size, title_size = (26, 38)
    elif (fac=="Ancient DNA" and year=="2018"):
            font_size, title_size = (27, 38)
    elif (fac=="Glycoproteomics" and year=="2017"):
            font_size, title_size = (24, 33)
    elif (fac=="Glycoproteomics" and year=="2018"):
            font_size, title_size = (23, 33)
    elif (fac=="Glycoproteomics" and year=="2019"):
            font_size, title_size = (24, 33)
    elif (fac=="Mass Cytometry" and year=="2019"):
            font_size, title_size = (23, 36)
    elif (fac=="Proximity Proteomics" and year=="2019"):
            font_size, title_size = (23, 36)
    elif (fac=="Targeted and Structural Proteomics" and year=="2019"):
            font_size, title_size = (24, 36)
    elif (fac=="Swedish Metabolomics Centre" and year=="2019"):
            font_size, title_size = (24, 36)
    elif (fac=="Swedish NMR Centre"):
            font_size, title_size = (25, 32)
    
    fig = go.Figure(layout=dict(
                    margin=go.layout.Margin(
                        l=50,
                        r=50,
                        b=30,
                        t=30,
                        pad=4
                        ),
                    annotations=[dict(
                        font=dict(family="Arial", size=title_size),
                        showarrow=False,
#                        text='<b><span style="color:#95C11E">Users {}<br>({})</span></b>'.format(year, sum(values)),
                        text='{} {}'.format(sum(values), pi_plural),
                        x=0.49,
                        y=0.49)
                        ]
                    )
                )

    fig.add_pie(labels=labels,
        values=values,
        text=["{} ({}%)".format(aff_map_abbr.get(labels[i].encode('utf-8'), labels[i].encode('utf-8')), round(float(values[i])/float(sum(values))*float(100), 1)) for i in range(len(labels))],
        marker=dict(colors=[FACILITY_USER_AFFILIATION_COLOUR_OFFICIAL.get(labels[i], "#000000") for i in range(len(labels))]),
        hole=0.6,
        automargin=True,
        sort=True,
        direction="clockwise",
        textinfo="text",
        textposition="outside",
        textfont=dict(family="Arial", size=font_size, color="#000000"),
        showlegend=False)

    plotly.io.write_image(fig, user_fig_name)#, height=1300, width=1200, scale=3)

    return user_fig_name