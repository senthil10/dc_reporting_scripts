This folder consists the files needed to generate individual facility metrics PDF report

**fstat_data_gen.py** - Take files provided by OO and generate python file `fstat_import_data.py` with aggregated data

**fstaf_pdf_gen.py** - Script that generates facility stat plots for the facilities. The script `fstat_data_gen.py` should be run before running this script

**fstat_plots_gen.py** - This is used in `fstat_pdf_gen.py` to generate the plots that are to be in the PDF

**fstat_reportlab_doc.py** - This have class to create facility reportlab object to generate pdf. This also have default values and the individual value for each facility is mention in `facility_reportlab_data.py`. This is a dependancy for the `fstat_pdf_gen.py` script

**fstat_reportlab_facility_data.py** - This only contains the plot values for individual facility. This is a dependancy for the `fstat_pdf_gen.py` script
