import pandas as pd
import numpy as np
import xlrd  # you should install xlrd package

'''
Read
'''
# path
file_loc = "data.xlsx"  # copy the root of repository's path
data = xlrd.open_workbook(file_loc)  # all the data inside excel file
# sheet
sheet = data.sheet_by_index(0)  # read sheet one
numRows = sheet.nrows - 1
# print("number of rows: ", numRows, '\n')

print("COMP 4710 Group 14 Analyzer.\n")
