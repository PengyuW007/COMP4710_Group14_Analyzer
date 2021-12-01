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
testFile = pd.read_excel("data.xlsx")


def testRemove(count, target):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_GDR"]:
            target += 1
            if i == 9:
                count += 1

    return target


# print("COMP 4710 Group 14 Analyzer.\n")

if __name__ == '__main__':
    print(testFile)
    k = testRemove(0, 0)
    print("The line will be removed is line ", k)
    print()
    print(testFile.drop(testFile.index[k - 1]))
