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


def countRemoveByGDR(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_GDR"]:
            if i == 9:
                count += 1

    return count


def countRemoveByAGR(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_AGR"]:
            if i == 99:
                count += 1

    return count


def countRemoveByHSP(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_HSP"]:
            if i == 9:
                count += 1

    return count


def countRemoveByDTH(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_DTH"]:
            if i == 9:
                count += 1

    return count


def countRemoveByTRM(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_TRM"]:
            if i == 9:
                count += 1

    return count


def countRemovedTotal():
    print("---------------------------------------------------------------")
    print("Summary of filtering imcomplete data as following: ")
    c1 = countRemoveByGDR(0)
    c2 = countRemoveByAGR(0)
    c3 = countRemoveByHSP(0)
    c4 = countRemoveByDTH(0)
    c5 = countRemoveByTRM(0)
    print("The # of lines  removed by COV_GDR ", c1)
    print("The # of lines  removed by COV_AGR ", c2)
    print("The # of lines  removed by COV_HSP ", c3)
    print("The # of lines  removed by COV_DTH ", c4)
    print("The # of lines  removed by COV_TRM ", c5)
    print("---------------------------------------------------------------")
    print()


# print("COMP 4710 Group 14 Analyzer.\n")

if __name__ == '__main__':
    print(testFile)
    countRemovedTotal()
    print()
    #testFile = testFile[~testFile["COV_EY"].isin([99])]
    testFile = testFile[~testFile["COV_GDR"].isin([9])]
    testFile = testFile[~testFile["COV_AGR"].isin([99])]
    #testFile = testFile[~testFile["COV_OCC"].isin([9])]
    #testFile = testFile[~testFile["COV_ASM"].isin([9])]
    #testFile = testFile[~testFile["COV_OY"].isin([99])]
    testFile = testFile[~testFile["COV_HSP"].isin([9])]
    #testFile = testFile[~testFile["COV_RSV"].isin([9])]
    #testFile = testFile[~testFile["COV_RY"].isin([99])]
    testFile = testFile[~testFile["COV_DTH"].isin([9])]
    testFile = testFile[~testFile["COV_TRM"].isin([9])]
    print(testFile)
