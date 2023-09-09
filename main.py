import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Firstly reading the excels file, glob help to read similiar files.
filepaths = glob.glob("invoices/*.xlsx")

# for getting all data in these xl sheets
# for processing xl files we need openpyxl library of python.
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Extracting names of files to use it, firstline will give pure name by removing suffix
    """It will return filename 10001-2023.01.08.xlsx 
    like this.
    """
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    # now generating pdf files.
    pdf = FPDF(orientation="P", unit="mm", format="a4")
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, ln=1, txt=f"Invoice nr: {invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")



