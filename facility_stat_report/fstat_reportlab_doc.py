#/usr/bin/env python
# -*- coding: utf-8 -*-

# This have class to create facility reportlab object to generate 
# facility maetrics pdf. This also have default values and the
# individual value for each facility is mention in facility_reportlab_data.py 
# This is a dependancy for the fstat_pdf_gen.py script

from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame

class report_lab_obj(object):
    
    def __init__(self, fname="report.pdf", dwidth=250*mm, dheight=150*mm, dpads=0*mm, show_bound=0):
        self.fname = fname
        self.dwidth = dwidth
        self.dheight = dheight
        self.dpads = dpads
        self.show_bound = show_bound
        self.doc = BaseDocTemplate(fname, pagesize=(dwidth, dheight), rightMargin=dpads , leftMargin=dpads, topMargin=dpads, bottomMargin=dpads)
        
        # default frame size
        self.default_fwidth = (self.doc.width - ((3-1)*self.dpads))/3
        self.default_fheight = (self.doc.height - ((2-1)*self.dpads))/2
        
    
    def make_page_templates(self, fdict=None, flist=None, use_default=True):
        """Makes template with frames if fdict not given goes with default 6 frames"""
        
        frames = []
        default_fdict = dict(
            fstat = dict(
                x1 = self.doc.leftMargin,
                y1 = self.doc.bottomMargin + self.default_fheight + self.dpads,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "fstat",
                showBoundary = self.show_bound,
                leftPadding = 11*mm,
                topPadding = 7*mm
                ),
            ctbar = dict(
                x1 = self.doc.leftMargin + self.default_fwidth + self.dpads,
                y1 = self.doc.bottomMargin + self.default_fheight + self.dpads,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "ctbar",
                showBoundary = self.show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            jfbar = dict(
                x1 = (self.doc.leftMargin + self.default_fwidth + self.dpads)*2,
                y1 = self.doc.bottomMargin + self.default_fheight + self.dpads,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "jfbar",
                showBoundary = self.show_bound,
                leftPadding = 0*mm,
                topPadding = 3*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr17 = dict(
                x1 = self.doc.leftMargin,
                y1 = self.doc.bottomMargin,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "usr17",
                showBoundary = self.show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr18 = dict(
                x1 = self.doc.leftMargin + self.default_fwidth + self.dpads,
                y1 = self.doc.bottomMargin,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "usr18",
                showBoundary = self.show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                ),
            usr19 = dict(
                x1 = (self.doc.leftMargin + self.default_fwidth + self.dpads)*2,
                y1 = self.doc.bottomMargin,
                width = self.default_fwidth,
                height = self.default_fheight,
                id = "usr19",
                showBoundary = self.show_bound,
                leftPadding = 0*mm,
                topPadding = 0*mm,
                rightPadding = 0*mm,
                bottomPadding = 0*mm
                )
            )
        if fdict == None:
            fdict = {}
               
        if flist == None:
            flist = ['fstat', 'ctbar', 'jfbar', 'usr17', 'usr18', 'usr19']
        
        for frm in flist:
            kwargs = fdict.get(frm, default_fdict[frm])if use_default else fdict[frm]
            frames.append(Frame(**kwargs))
        
        self.doc.addPageTemplates([PageTemplate(id='facility_metrics', frames=frames)])
    
    def set_fig_sizes(self, fig_sizes=None):
        """Set width and height for image scaling"""
        if fig_sizes == None:
            fig_sizes = {}
            
        self.cat_bar_width = fig_sizes.get('cat_bar_width', 80)
        self.cat_bar_height = fig_sizes.get('cat_bar_height', 60)
        self.jif_bar_width = fig_sizes.get('jif_bar_width', 80)
        self.jif_bar_height = fig_sizes.get('jif_bar_height', 60)
        self.u17_pie_width = fig_sizes.get('u17_bar_width', 80)
        self.u17_pie_height = fig_sizes.get('u17_bar_height', 60)
        self.u18_pie_width = fig_sizes.get('u18_bar_width', 80)
        self.u18_pie_height = fig_sizes.get('u18_bar_height', 60)
        self.u19_pie_width = fig_sizes.get('u19_bar_width', 80)
        self.u19_pie_height = fig_sizes.get('u19_bar_height', 60)
        
        
            
        