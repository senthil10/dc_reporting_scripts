#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Adrian Lärkeryd <adrian.larkeryd@scilifelab.uu.se>

# Plotting libs
import plotly
import plotly.graph_objs as go

# My own files
from colour_science import SCILIFE_COLOURS
from issn_files import ISSN_IMPACT_2019, ISSN_IMPACT_2017, ISSN_IMPACT_2016, ISSN_IMPACT_2015, ISSN_TO_ISSNL, ISSNL_TO_ISSN, issn_to_impact
from publications_api import Publications_api

# Igonre publications if they have only these labels
def check_valid_label(plabels):
    ignore_list = ['Centre for Cellular Imaging', 'Intravital Microscopy Facility', 'Biochemical Imaging Centre Umeå',
                   'Advanced FISH Technologies', 'National Resource for Mass Spectrometry Imaging',
                   'Gothenburg Imaging Mass Spectrometry', 'Glycoproteomics', 'Targeted and Structural Proteomics',
                   'AIDA Data Hub', 'Clinical Genomics Linköping', 'Clinical Genomics Umeå', 'Clinical Genomics Örebro']
    return any([(l not in ignore_list) for l in plabels])

print "PUBLICATION PLOTS..."
#allyrs = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]
#years_1015 = ["2010", "2011", "2012", "2013", "2014", "2015", "2016"]
allyrs = ["2013", "2014", "2015", "2016", "2017", "2018", "2019"]
years_1015 = ["2013", "2014", "2015", "2016"]
years_161718 = ["2017", "2018", "2019"]

pub_getter_1015 = Publications_api(years=years_1015)
pub_allyrs = pub_getter_1015.get_publications()
aff_allyrs = pub_getter_1015.get_publications_affiliated()
print "Sources:", pub_getter_1015.source_links


pub_getter_161718 = Publications_api(years=years_161718)
pub_161718 = pub_getter_161718.get_publications()
aff_161718 = pub_getter_161718.get_publications_affiliated()

#[pub['labels'].keys() for pub in pub_161718 if pub['published'].split('-')[0] == '2019' and check_valid_label(pub['labels'].keys()) and check_date < datetime.datetime.strptime(pub['created'].split('T')[0], '%Y-%M-%d')]

pub_allyrs += pub_161718
aff_allyrs += aff_161718

print "Sources:", pub_getter_1015.source_links, pub_getter_161718.source_links

pub_aff_161718 = pub_161718 + aff_161718
pub_aff_allyrs = pub_allyrs + aff_allyrs

# pub_getter_2019 = Publications_api(years=["2019"])
# pub_2019 = pub_getter_2019.get_publications()
# new_label_pub = []
# p19_read = []
# p19_uniq = []
# for p19 in pub_2019:
#     if p19["doi"] in p19_read:
#         continue
#     if not check_valid_label(p19["labels"]):
#         new_label_pub.append(p19["doi"])
#     p19_read.append(p19["doi"])
#     p19_uniq.append(p19["doi"])
# import pdb; pdb.set_trace()

if False:

    publication_dois = list()
    publication_issns = list()
    publication_impacts = {"2013": [], "2014": [], "2015": [], "2016": [], "2017": [], "2018": [], "2019": []}
    for pub in pub_aff_allyrs:
        if pub["doi"] in publication_dois or not check_valid_label(pub["labels"]):
            continue
    
        year = pub["published"].split("-")[0]
        if pub["journal"]["issn"]:
            issn = pub["journal"]["issn"]
            publication_issns.append(issn)
            impact = issn_to_impact(issn)

            if impact is None:
                print "NO IMPACT FACTOR FOUND FOR:", issn, pub["journal"]
            # At the end, add the impact to the list
            publication_impacts[year].append(impact)
            jifflag = True
        else: 
            # NO ISSN
            publication_impacts[year].append(None)
            jifflag = True
            print "NO ISSN FOUND FOR:", issn, pub["journal"]


    jif_data = {"2013": [0,0,0,0,0], "2014": [0,0,0,0,0], "2015": [0,0,0,0,0], "2016": [0,0,0,0,0], "2017": [0,0,0,0,0], "2018": [0,0,0,0,0], "2019": [0,0,0,0,0]}

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


    jif_unknown = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][4], jif_data["2014"][4], jif_data["2015"][4], jif_data["2016"][4], jif_data["2017"][4], jif_data["2018"][4], jif_data["2019"][4]],
        name="JIF unknown", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[5],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_low = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][0], jif_data["2014"][0], jif_data["2015"][0], jif_data["2016"][0], jif_data["2017"][0], jif_data["2018"][0], jif_data["2019"][0]],
        name="JIF < 6", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[0],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_mediocre = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][1], jif_data["2014"][1], jif_data["2015"][1], jif_data["2016"][1], jif_data["2017"][1], jif_data["2018"][1], jif_data["2019"][1]],
        name="JIF = 6 - 9", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[7],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_good = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][2], jif_data["2014"][2], jif_data["2015"][2], jif_data["2016"][2], jif_data["2017"][2], jif_data["2018"][2], jif_data["2019"][2]],
        name="JIF = 9 - 25", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[9],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_high = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][3], jif_data["2014"][3], jif_data["2015"][3], jif_data["2016"][3], jif_data["2017"][3], jif_data["2018"][3], jif_data["2019"][3]],
        name="JIF > 25", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[1],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )

    layout = go.Layout(
        barmode="stack",
        plot_bgcolor='rgba(0,0,0,0)',
        width=1200, 
        height=600,
        margin=go.layout.Margin(
            l=100,
            r=100,
            b=100,
            t=30,
            pad=4
        ),
        xaxis=dict(
            showticklabels=True, 
            dtick=1,
            zeroline=True,
            tickfont=dict(
                family='Arial',
                   size=28,
                color='#000000'
            )
        ),
        yaxis=dict(
            showticklabels=True,
            gridcolor="#E2E5E0",
            tickfont=dict(
                family='Arial',
                   size=28,
                color='#000000'
            )
        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='Arial',
                size=20,
                color='#000'
            )
        )
    )
    data = [jif_unknown, jif_low, jif_mediocre, jif_good, jif_high]

    
    fig = go.Figure(data=data, layout=layout)        
    # plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.png'.format(label["value"].lower().replace(" ", "_")))
    # plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.pdf'.format(label["value"].lower().replace(" ", "_")))
    plotly.io.write_image(fig, 'jif_fac_and_aff_allyrs.png', scale=5)



publication_dois = list()
publication_issns = list()
publication_impacts = {"2013": [], "2014": [], "2015": [], "2016": [], "2017": [], "2018": [], "2019": []}
for pub in pub_allyrs:
    if pub["doi"] in publication_dois or not check_valid_label(pub["labels"]):
        continue
    publication_dois.append(pub["doi"])
    year = pub["published"].split("-")[0]
    if pub["journal"]["issn"]:
        issn = pub["journal"]["issn"]
        publication_issns.append(issn)
        impact = issn_to_impact(issn)

        if impact is None:
            print "NO IMPACT FACTOR FOUND FOR:", issn, pub["journal"]
        # At the end, add the impact to the list
        publication_impacts[year].append(impact)
        jifflag = True
    else: 
        # NO ISSN
        publication_impacts[year].append(None)
        jifflag = True
        print "NO ISSN FOUND FOR:", issn, pub["journal"]

jif_data = {"2013": [0,0,0,0,0], "2014": [0,0,0,0,0], "2015": [0,0,0,0,0], "2016": [0,0,0,0,0], "2017": [0,0,0,0,0], "2018": [0,0,0,0,0], "2019": [0,0,0,0,0]}

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


jif_unknown = go.Bar(
    x=allyrs,
    y=[jif_data["2013"][4], jif_data["2014"][4], jif_data["2015"][4], jif_data["2016"][4], jif_data["2017"][4], jif_data["2018"][4], jif_data["2019"][4]],
    name="JIF unknown", 
    textfont=dict(
        family='Arial',
        size=28,
        color='#000000'
    ),
    marker=dict(
        color=SCILIFE_COLOURS[5],
        line=dict(
        color='#000000',
        width=1.5)
    )
)
jif_low = go.Bar(
    x=allyrs,
    y=[jif_data["2013"][0], jif_data["2014"][0], jif_data["2015"][0], jif_data["2016"][0], jif_data["2017"][0], jif_data["2018"][0], jif_data["2019"][0]],
    name="JIF < 6", 
    textfont=dict(
        family='Arial',
        size=28,
        color='#000000'
    ),
    marker=dict(
        color=SCILIFE_COLOURS[0],
        line=dict(
        color='#000000',
        width=1.5)
    )
)
jif_mediocre = go.Bar(
    x=allyrs,
    y=[jif_data["2013"][1], jif_data["2014"][1], jif_data["2015"][1], jif_data["2016"][1], jif_data["2017"][1], jif_data["2018"][1], jif_data["2019"][1]],
    name="JIF = 6 - 9", 
    textfont=dict(
        family='Arial',
        size=28,
        color='#000000'
    ),
    marker=dict(
        color=SCILIFE_COLOURS[7],
        line=dict(
        color='#000000',
        width=1.5)
    )
)
jif_good = go.Bar(
    x=allyrs,
    y=[jif_data["2013"][2], jif_data["2014"][2], jif_data["2015"][2], jif_data["2016"][2], jif_data["2017"][2], jif_data["2018"][2], jif_data["2019"][2]],
    name="JIF = 9 - 25", 
    textfont=dict(
        family='Arial',
        size=28,
        color='#000000'
    ),
    marker=dict(
        color=SCILIFE_COLOURS[9],
        line=dict(
        color='#000000',
        width=1.5)
    )
)
jif_high = go.Bar(
    x=allyrs,
    y=[jif_data["2013"][3], jif_data["2014"][3], jif_data["2015"][3], jif_data["2016"][3], jif_data["2017"][3], jif_data["2018"][3], jif_data["2019"][3]],
    name="JIF > 25", 
    textfont=dict(
        family='Arial',
        size=28,
        color='#000000'
    ),
    marker=dict(
        color=SCILIFE_COLOURS[1],
        line=dict(
        color='#000000',
        width=1.5)
    )
)

layout = go.Layout(
    barmode="stack",
    plot_bgcolor='rgba(0,0,0,0)',
    width=1200, 
    height=600,
    margin=go.layout.Margin(
        l=100,
        r=100,
        b=100,
        t=30,
        pad=4
    ),
    xaxis=dict(
        showticklabels=True, 
        dtick=1,
        zeroline=True,
        tickfont=dict(
            family='Arial',
               size=28,
            color='#000000'
        )
    ),
    yaxis=dict(
        showticklabels=True,
        gridcolor="#E2E5E0",
        tickfont=dict(
            family='Arial',
               size=28,
            color='#000000'
        )
    ),
    legend=dict(
        traceorder='normal',
        font=dict(
            family='Arial',
            size=20,
            color='#000'
        )
    )
)
data = [jif_unknown, jif_low, jif_mediocre, jif_good, jif_high]

fig = go.Figure(data=data, layout=layout)
# plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.png'.format(label["value"].lower().replace(" ", "_")))
# plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.pdf'.format(label["value"].lower().replace(" ", "_")))
plotly.io.write_image(fig, 'Figure 12. Infrastructure publications with JIF distribution.png', scale=5)


if False:

    publication_dois = list()
    publication_issns = list()
    publication_impacts = {"2013": [], "2014": [], "2015": [], "2016": [], "2017": [], "2018": [], "2019": []}
    for pub in aff_allyrs:
        if pub["doi"] in publication_dois or not check_valid_label(pub["labels"]):
            continue
        publication_dois.append(pub["doi"])
        year = pub["published"].split("-")[0]
        if pub["journal"]["issn"]:
            issn = pub["journal"]["issn"]
            publication_issns.append(issn)
            impact = issn_to_impact(issn)

            if impact is None:
                print "NO IMPACT FACTOR FOUND FOR:", issn, pub["journal"]
            # At the end, add the impact to the list
            publication_impacts[year].append(impact)
            jifflag = True
        else: 
            # NO ISSN
            publication_impacts[year].append(None)
            jifflag = True
            print "NO ISSN FOUND FOR:", issn, pub["journal"]

    jif_data = {"2013": [0,0,0,0,0], "2014": [0,0,0,0,0], "2015": [0,0,0,0,0], "2016": [0,0,0,0,0], "2017": [0,0,0,0,0], "2018": [0,0,0,0,0], "2019": [0,0,0,0,0]}

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


    jif_unknown = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][4], jif_data["2014"][4], jif_data["2015"][4], jif_data["2016"][4], jif_data["2017"][4], jif_data["2018"][4], jif_data["2019"][4]],
        name="JIF unknown", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[5],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_low = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][0], jif_data["2014"][0], jif_data["2015"][0], jif_data["2016"][0], jif_data["2017"][0], jif_data["2018"][0], jif_data["2019"][0]],
        name="JIF < 6", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[0],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_mediocre = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][1], jif_data["2014"][1], jif_data["2015"][1], jif_data["2016"][1], jif_data["2017"][1], jif_data["2018"][1], jif_data["2019"][1]],
        name="JIF = 6 - 9", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[7],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_good = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][2], jif_data["2014"][2], jif_data["2015"][2], jif_data["2016"][2], jif_data["2017"][2], jif_data["2018"][2], jif_data["2019"][2]],
        name="JIF = 9 - 25", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[9],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )
    jif_high = go.Bar(
        x=allyrs,
        y=[jif_data["2013"][3], jif_data["2014"][3], jif_data["2015"][3], jif_data["2016"][3], jif_data["2017"][3], jif_data["2018"][3], jif_data["2019"][3]],
        name="JIF > 25", 
        textfont=dict(
            family='Arial',
            size=28,
            color='#000000'
        ),
        marker=dict(
            color=SCILIFE_COLOURS[1],
            line=dict(
            color='#000000',
            width=1.5)
        )
    )

    layout = go.Layout(
        barmode="stack",
        plot_bgcolor='rgba(0,0,0,0)',
        width=1200, 
        height=600,
        margin=go.layout.Margin(
            l=100,
            r=100,
            b=100,
            t=30,
            pad=4
        ),
        xaxis=dict(
            showticklabels=True, 
            dtick=1,
            zeroline=True,
            tickfont=dict(
                family='Arial',
                   size=28,
                color='#000000'
            )
        ),
        yaxis=dict(
            showticklabels=True,
            gridcolor="#E2E5E0",
            tickfont=dict(
                family='Arial',
                   size=28,
                color='#000000'
            )
        ),
        legend=dict(
            traceorder='normal',
            font=dict(
                family='Arial',
                size=20,
                color='#000'
            )
        )
    )
    data = [jif_unknown, jif_low, jif_mediocre, jif_good, jif_high]

    
    fig = go.Figure(data=data, layout=layout)        
    # plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.png'.format(label["value"].lower().replace(" ", "_")))
    # plotly.io.write_image(fig, 'facility_onepagers_figures/{}_jif.pdf'.format(label["value"].lower().replace(" ", "_")))
    plotly.io.write_image(fig, 'jif_aff_allyrs.png', scale=5)
