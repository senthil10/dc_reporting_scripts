#/usr/bin/env python
# -*- coding: utf-8 -*-

# This only contains the plot values for individual facility
# This is a dependancy for the fstat_pdf_gen.py script

from reportlab.lib.units import mm

base_dir = "/Users/senpa282/opt/publication_reporting/facility_stat_plot/pdfs/"
doc_width = 250*mm
doc_height = 150*mm
doc_pads = 0*mm
show_bound = 0

def calc_frame_width(dw, dpd, ncol=3):
    return (dw - ((ncol-1)*dpd))/ncol

def calc_frame_height(dh, dpd, nrow=2):
    return (dh - ((nrow-1)*dpd))/nrow

facility_graph_data = {}

# Facilites with huge user data  #

# For facility 'National Genomics Infrastructure'

facility_graph_data['National Genomics Infrastructure'] = dict(
    doc = dict(
        fname = base_dir + "National Genomics Infrastructure.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("small_inner_heading", "small_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 7*mm,
                topPadding = 6*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    ),
    figsize = dict(
        u17 = dict(imw=78, imh=59),
        u18 = dict(imw=85, imh=61),
        u19 = dict(imw=85, imh=61)
    )
)


# For facility 'Support, Infrastructure and Training'

facility_graph_data['Support, Infrastructure and Training'] = dict(
    doc = dict(
        fname = base_dir + "Support Infrastructure and Training.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("small_inner_heading", "small_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 8*mm,
                topPadding = 5*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 4*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    ),
    figsize = dict(
        u17 = dict(imw=76, imh=58),
        u18 = dict(imw=82, imh=60),
        u19 = dict(imw=86, imh=61)
    )
)

# For facility 'Compute and Storage'

facility_graph_data['Compute and Storage'] = dict(
    doc = dict(
        fname = base_dir + "Compute and Storage.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 11*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
    figsize = dict(
        u17 = dict(imw=86, imh=65),
        u18 = dict(imw=86, imh=65),
        u19 = dict(imw=86, imh=65)
    )
)

# For facility 'Biochemical Imaging Centre Umea'

facility_graph_data['Biochemical Imaging Centre Umea'] = dict(
    doc = dict(
        fname = base_dir + "Biochemical Imaging Centre Umea.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 5*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 8*mm,
                topPadding = 3.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
    figsize = dict(
        u17 = dict(imw=70, imh=58),
        u18 = dict(imw=92, imh=63),
        u19 = dict(imw=92, imh=63)
    )
)

# Facilities with all pub but only two user plots #

# For facility 'AIDA Data Hub'

facility_graph_data['AIDA Data Hub'] = dict(
    doc = dict(
        fname = base_dir + "AIDA Data Hub.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        flist = ['fstat', 'ctbar', 'jfbar', 'usr18', 'usr19'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 7*mm
                ),
            usr18 = dict(
                x1 = (calc_frame_width(doc_width, doc_pads)/2)-5*mm,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (calc_frame_width(doc_width, doc_pads)*1.5)+4*mm,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    ),
    figsize = dict(
        u18 = dict(imw=80, imh=60),
        u19 = dict(imw=85, imh=62)
    )
)

# For facility 'Intravital Microscopy Facility'

facility_graph_data['Intravital Microscopy Facility'] = dict(
    doc = dict(
        fname = base_dir + "Intravital Microscopy Facility.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        flist = ['fstat', 'ctbar', 'jfbar', 'usr18', 'usr19'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 6*mm
                ),
            usr18 = dict(
                x1 = (calc_frame_width(doc_width, doc_pads)/2)-6*mm,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 1*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (calc_frame_width(doc_width, doc_pads)*1.5)+5*mm,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    ),
    figsize = dict(
        u18 = dict(imw=82, imh=60),
        u19 = dict(imw=88, imh=61)
    )
)

# For facilites have no publication plot but 2 user plot #

# For facility 'Ancient DNA'

facility_graph_data['Ancient DNA'] = dict(
    doc = dict(
        fname = base_dir + "Ancient DNA.pdf",
        dwidth = doc_width,
        dheight = doc_height/2,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat', 'usr18', 'usr19'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 4*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    ),
    figsize = dict(
        u18 = dict(imw=75, imh=59)
    )
)


# For facilites have 2 publication plot but no user plot #

# For facility 'Advanced FISH Technologies'

facility_graph_data['Advanced FISH Technologies'] = dict(
    doc = dict(
        fname = base_dir + "Advanced FISH Technologies.pdf",
        dwidth = doc_width,
        dheight = doc_height/2,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat', 'ctbar', 'jfbar'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 11*mm,
                topPadding = 4*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
        )
    )
)

# For facilites with 3 plots (either all user or 2 bar 1 user)

# For facility 'Glycoproteomics'

facility_graph_data['Glycoproteomics'] = dict(
    doc = dict(
        fname = base_dir + "Glycoproteomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        flist = ['fstat', 'ctbar', 'jfbar', 'usr17', "usr18", "usr19"],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
               x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
               y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
                usr17 = dict(
                    x1 = doc_pads,
                    y1 = doc_pads,
                    width = calc_frame_width(doc_width, doc_pads),
                    height = calc_frame_height(doc_height, doc_pads),
                    id = "usr17",
                    showBoundary = show_bound,
                    leftPadding = 0*mm,
                    topPadding = 0*mm,
                    rightPadding = 0*mm,
                    bottomPadding = 0*mm
                    ),
                usr18 = dict(
                    x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                    y1 = doc_pads,
                    width = calc_frame_width(doc_width, doc_pads),
                    height = calc_frame_height(doc_height, doc_pads),
                    id = "usr18",
                    showBoundary = show_bound,
                    leftPadding = 1*mm,
                    topPadding = 0*mm,
                    rightPadding = 0*mm,
                    bottomPadding = 0*mm
                    ),
                usr19 = dict(
                    x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                    y1 = doc_pads,
                    width = calc_frame_width(doc_width, doc_pads),
                    height = calc_frame_height(doc_height, doc_pads),
                    id = "usr19",
                    showBoundary = show_bound,
                    leftPadding = 3*mm,
                    topPadding = 0*mm,
                    rightPadding = 0*mm,
                    bottomPadding = 0*mm
                    )
                )
            ),
        figsize = dict(
            u17 = dict(imw=85, imh=62),
            u18 = dict(imw=87, imh=62),
            u19 = dict(imw=81, imh=61)
        )
    )


facility_graph_data['Clinical Genomics Orebro'] = dict(
    doc = dict(
        fname = base_dir + "Clinical Genomics Orebro.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat', 'ctbar', 'jfbar', 'usr19'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            ctbar = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "ctbar",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
               x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
               y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "jfbar",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
    figsize = dict(
        u19 = dict(imw=93, imh=63)
    )
)

# For facilites with only stat no plots

# For facility 'Exposomics'

facility_graph_data['Exposomics'] = dict(
    doc = dict(
        fname = base_dir + "Exposomics.pdf",
        dwidth = doc_width/3,
        dheight = doc_height/2,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 7*mm
                )
            )
        )
    )

# For facility 'Clinical Genomics Linkoping'

facility_graph_data['Clinical Genomics Linkoping'] = dict(
    doc = dict(
        fname = base_dir + "Clinical Genomics Linkoping.pdf",
        dwidth = doc_width/3,
        dheight = doc_height/2,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 7*mm
                )
            )
        )
    )

# For facility 'Clinical Genomics Linkoping'

facility_graph_data['Clinical Genomics Umea'] = dict(
    doc = dict(
        fname = base_dir + "Clinical Genomics Umea.pdf",
        dwidth = doc_width/3,
        dheight = doc_height/2,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        use_default = False,
        flist = ['fstat'],
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 7*mm
                )
            )
        )
    )

# For facilites with pie size tweaks #

# For facility 'BioImage Informatics'

facility_graph_data['BioImage Informatics'] = dict(
    sdoc = dict(
        fname = base_dir + "BioImage Informatics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 5*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=72, imh=58)
        )
    )

# For facility 'Advanced Light Microscopy'

facility_graph_data['Advanced Light Microscopy'] = dict(
    sdoc = dict(
        fname = base_dir + "Advanced Light Microscopy.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 5*mm,
                topPadding = 1.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=76, imh=60),
            u18 = dict(imw=82, imh=60),
            u19 = dict(imw=82, imh=60)
        )
    )


# For facility 'Cryo-EM'

facility_graph_data['Cryo-EM'] = dict(
    sdoc = dict(
        fname = base_dir + "Cryo-EM.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 5*mm,
                topPadding = 1.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=72, imh=60),
            u18 = dict(imw=84, imh=60),
            u19 = dict(imw=84, imh=60)
        )
    )

# For facility 'Cell Profiling'

facility_graph_data['Cell Profiling'] = dict(
    sdoc = dict(
        fname = base_dir + "Cell Profiling.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 15*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 5*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 1.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=84, imh=60)
        )
    )

# For facility 'In Situ Sequencing'

facility_graph_data['In Situ Sequencing'] = dict(
    sdoc = dict(
        fname = base_dir + "In Situ Sequencing.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 16*mm,
                topPadding = 6*mm
                )
            )
        )
    )

# For facility 'National Resource for Mass Spectrometry Imaging'

facility_graph_data['National Resource for Mass Spectrometry Imaging'] = dict(
    sdoc = dict(
        fname = base_dir + "National Resource for Mass Spectrometry Imaging.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 15*mm,
                topPadding = 8*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 10*mm,
                topPadding = 1.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=66, imh=58)
        )
    )

# For facility 'Gothenburg Imaging Mass Spectrometry'

facility_graph_data['Gothenburg Imaging Mass Spectrometry'] = dict(
    sdoc = dict(
        fname = base_dir + "Gothenburg Imaging Mass Spectrometry.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 15*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 0.5*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=84, imh=61)
        )
    )

# For facility 'Chemical Biology Consortium Sweden'

facility_graph_data['Chemical Biology Consortium Sweden'] = dict(
    sdoc = dict(
        fname = base_dir + "Chemical Biology Consortium Sweden.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 12*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3.5*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=76, imh=59)
        )
    )

# For facility 'Chemical Proteomics'

facility_graph_data['Chemical Proteomics'] = dict(
    sdoc = dict(
        fname = base_dir + "Chemical Proteomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 7*mm,
                topPadding = 1*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=71, imh=59),
            u18 = dict(imw=82, imh=60)
        )
    )

# For facility 'Genome Engineering Zebrafish'

facility_graph_data['Genome Engineering Zebrafish'] = dict(
    sdoc = dict(
        fname = base_dir + "Genome Engineering Zebrafish.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 6*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=78, imh=60)
        )
    )

# For facility 'Clinical Genomics Gothenburg'

facility_graph_data['Clinical Genomics Gothenburg'] = dict(
    sdoc = dict(
        fname = base_dir + "Clinical Genomics Gothenburg.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 13*mm,
                topPadding = 7*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 4*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        )
    )

# For facility 'Clinical Genomics Uppsala'

facility_graph_data['Clinical Genomics Uppsala'] = dict(
    sdoc = dict(
        fname = base_dir + "Clinical Genomics Uppsala.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 6*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=73, imh=58),
            u18 = dict(imw=79, imh=60)
        )
    )

# For facility 'Clinical Genomics Stockholm'

facility_graph_data['Clinical Genomics Stockholm'] = dict(
    sdoc = dict(
        fname = base_dir + "Clinical Genomics Stockholm.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 6*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=74, imh=58),
            u18 = dict(imw=85, imh=60),
            u19 = dict(imw=76, imh=59)
        )
    )

# For facility 'Autoimmunity Profiling'

facility_graph_data['Autoimmunity Profiling'] = dict(
    sdoc = dict(
        fname = base_dir + "Autoimmunity Profiling.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 15*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=75, imh=58),
            u18 = dict(imw=77, imh=59),
            u19 = dict(imw=86, imh=60)
        )
    )

# For facility 'Targeted and Structural Proteomics'

facility_graph_data['Targeted and Structural Proteomics'] = dict(
    sdoc = dict(
        fname = base_dir + "Targeted and Structural Proteomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 15*mm,
                topPadding = 7*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=75, imh=58),
            u18 = dict(imw=79, imh=60),
            u19 = dict(imw=85, imh=60)
        )
    )

# For facility 'Microbial Single Cell Genomics'

facility_graph_data['Microbial Single Cell Genomics'] = dict(
    sdoc = dict(
        fname = base_dir + "Microbial Single Cell Genomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 4*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0.7*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=84, imh=60),
            u19 = dict(imw=74, imh=59)
        )
    )


# For facility 'High Throughput Genome Engineering'

facility_graph_data['High Throughput Genome Engineering'] = dict(
    sdoc = dict(
        fname = base_dir + "High Throughput Genome Engineering.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3.5*mm,
                topPadding = 0.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=76, imh=59)
        )
    )

# For facility 'Swedish Metabolomics Centre'

facility_graph_data['Swedish Metabolomics Centre'] = dict(
    sdoc = dict(
        fname = base_dir + "Swedish Metabolomics Centre.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=79, imh=60),
            u19 = dict(imw=85, imh=60)
        )
    )

# For facility 'Drug Discovery and Development'

facility_graph_data['Drug Discovery and Development'] = dict(
    sdoc = dict(
        fname = base_dir + "Drug Discovery and Development.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3.5*mm,
                topPadding = 0.8*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=79, imh=59),
            u19 = dict(imw=84, imh=61)
        )
    )

# For facility 'Clinical Genomics Lund'

facility_graph_data['Clinical Genomics Lund'] = dict(
    sdoc = dict(
        fname = base_dir + "Clinical Genomics Lund.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 5*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=78, imh=60),
            u19 = dict(imw=84, imh=61)
        )
    )

# For facility 'Mass Cytometry'

facility_graph_data['Mass Cytometry'] = dict(
    sdoc = dict(
        fname = base_dir + "Mass Cytometry.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 2*mm,
                topPadding = 2.5*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3.3*mm,
                topPadding = 1*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=74, imh=59),
            u19 = dict(imw=84, imh=60)
        )
    )

# For facility 'Proximity Proteomics'

facility_graph_data['Proximity Proteomics'] = dict(
    sdoc = dict(
        fname = base_dir + "Proximity Proteomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 7*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 6.5*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads)*2,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr19",
                showBoundary = show_bound,
                leftPadding = 0*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=74, imh=59),
            u19 = dict(imw=84, imh=60)
        )
    )

# For facility 'Plasma Profiling'

facility_graph_data['Plasma Profiling'] = dict(
    sdoc = dict(
        fname = base_dir + "Plasma Profiling.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u17 = dict(imw=77, imh=59)
        )
    )

# For facility 'Proteogenomics'

facility_graph_data['Proteogenomics'] = dict(
    sdoc = dict(
        fname = base_dir + "Proteogenomics.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 8*mm
                ),
            usr17 = dict(
                x1 = doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr17",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = doc_pads + calc_frame_width(doc_width, doc_pads) + doc_pads,
                y1 = doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "usr18",
                showBoundary = show_bound,
                leftPadding = 3*mm,
                topPadding = 2*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        ),
        figsize = dict(
            u18 = dict(imw=77, imh=59)
        )
    )

# For facility 'Swedish NMR Centre'

facility_graph_data['Swedish NMR Centre'] = dict(
    sdoc = dict(
        fname = base_dir + "Swedish NMR Centre.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 14*mm,
                topPadding = 6*mm
                )
            )
        )
    )

#For facility 'Centre for Cellular Imaging'

facility_graph_data['Centre for Cellular Imaging'] = dict(
    sdoc = dict(
        fname = base_dir + "Centre for Cellular Imaging.pdf",
        dwidth = doc_width,
        dheight = doc_height,
        dpads = doc_pads,
        show_bound = show_bound
    ),
    style = ("medium_inner_heading", "medium_page_text"),
    frames = dict(
        fdict = dict(
            fstat = dict(
                x1 = doc_pads,
                y1 = doc_pads + calc_frame_height(doc_height, doc_pads) + doc_pads,
                width = calc_frame_width(doc_width, doc_pads),
                height = calc_frame_height(doc_height, doc_pads),
                id = "fstat",
                showBoundary = show_bound,
                leftPadding = 16*mm,
                topPadding = 7*mm
                )
            )
        )
)