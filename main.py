import pandas as pd
import numpy as np
import xlrd  # you should install xlrd package, resolvent: pip install xlrd/ pip install openpyxl

'''
Read
'''
# path
# file_loc = "data.xlsx"  # copy the root of repository's path, if you have error" Excel xlsx file;
# not supported solution, resolvent: pip install xlrd==1.2.0"
# data = xlrd.open_workbook(file_loc)  # all the data inside excel file
# sheet
# sheet = data.sheet_by_index(0)  # read sheet one
# numRows = sheet.nrows
# print("number of rows: ", numRows, '\n')

'''yue ma tests, '''
testFile = pd.read_csv("COVID19-eng.csv")  # COVID19-eng.csv, official path repository

def testRemove(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_GDR"]:
            if i == 9:
                count += 1

    return count


# print("COMP 4710 Group 14 Analyzer.\n")

if __name__ == '__main__':
    print(testFile)
    k = testRemove(0)
    print("The line will be removed is line ", k)
    print()
    testFile = testFile[~testFile["COV_EY"].isin([99])]
    testFile = testFile[~testFile["COV_GDR"].isin([9])]
    testFile = testFile[~testFile["COV_AGR"].isin([99])]
    testFile = testFile[~testFile["COV_OCC"].isin([9])]
    testFile = testFile[~testFile["COV_ASM"].isin([9])]
    testFile = testFile[~testFile["COV_OY"].isin([99])]
    testFile = testFile[~testFile["COV_HSP"].isin([9])]
    testFile = testFile[~testFile["COV_RSV"].isin([9])]
    testFile = testFile[~testFile["COV_RY"].isin([99])]
    testFile = testFile[~testFile["COV_DTH"].isin([9])]
    testFile = testFile[~testFile["COV_TRM"].isin([9])]
    print(testFile)
