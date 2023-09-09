import pandas as pd
import glob

# Firstly reading the excels file, glob help to read similiar files.
filepaths = glob.glob("invoices/*.xlsx")

# for getting all data in these xl sheets
# for processing xl files we need openpyxl library of python.
for filepath in filepaths:
    df = pd.read_excel(filepath)
    print(df)
