import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


def countRemoveByASM(count):
    if count != 0:
        print("The input value is not zero, please return and check!")
    else:
        for i in testFile["COV_ASM"]:
            if i == 9:
                count += 1

    return count


def countRemovedTotal():
    print("---------------------------------------------------------------")
    print("Summary of filtering incomplete data as following: ")
    c1 = countRemoveByGDR(0)
    c2 = countRemoveByAGR(0)
    c3 = countRemoveByHSP(0)
    c4 = countRemoveByDTH(0)
    c5 = countRemoveByTRM(0)
    c6 = countRemoveByASM(0)
    print("The # of lines  removed by COV_GDR ", c1)
    print("The # of lines  removed by COV_AGR ", c2)
    print("The # of lines  removed by COV_HSP ", c3)
    print("The # of lines  removed by COV_DTH ", c4)
    print("The # of lines  removed by COV_TRM ", c5)
    print("The # of lines  removed by COV_ASM ", c6)
    print("---------------------------------------------------------------")
    print()



def displayPlot(regionNum, title):
    testFile = pd.read_csv("probability.csv")
    plt.style.use("ggplot")
    AgeGroup = ["0~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80+"]
    male = []
    female = []
    count = 0
    data = np.where((testFile['COV_GDR'] == 1) & (testFile['COV_REG'] == regionNum))
    for i in testFile.loc[data]['PER_DTH']:
        male.insert(count, i)
        count += 1



    count = 0
    data = np.where((testFile['COV_GDR'] == 2) & (testFile['COV_REG'] == regionNum))
    print(testFile.loc[data])
    for i in testFile.loc[data]['PER_DTH']:
        female.insert(count, i)
        count += 1


    xticks = np.arange(len(AgeGroup))

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(xticks, male, width=0.25, label="Male", color="red")
    ax.bar(xticks + 0.25, female, width=0.25, label="Female", color="blue")
    ax.set_title(title, fontsize=15)
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Percentage of Asymptomatic")
    ax.legend()

    ax.set_xticks(xticks + 0.25)
    ax.set_xticklabels(AgeGroup)
    ax.grid(False)
    plt.show()

# print("COMP 4710 Group 14 Analyzer.\n")

if __name__ == '__main__':
    print(testFile)
    countRemovedTotal()
    print()

    # testFile = testFile[~testFile["COV_EY"].isin([99])]
    testFile = testFile[~testFile["COV_GDR"].isin([9])]
    testFile = testFile[~testFile["COV_AGR"].isin([99])]
    testFile = testFile[~testFile["COV_ASM"].isin([9])]
    testFile = testFile[~testFile["COV_DTH"].isin([9])]

    print(testFile)

    # total number of case
    data = testFile.sort_values(['COV_GDR', 'COV_AGR', 'COV_REG'], ascending=False).groupby(
        ['COV_GDR', 'COV_AGR', 'COV_REG']).size().reset_index(name='NUM_CASE')

    data0 = testFile.query('COV_HSP == 1')
    data00 = data0.sort_values(['COV_GDR', 'COV_AGR', 'COV_REG'], ascending=False).groupby(
        ['COV_GDR', 'COV_AGR', 'COV_REG', 'COV_HSP']).size().reset_index(name='NUM_HSP')

    # tootal number of case that have symptoms
    data1 = testFile.query('COV_ASM == 2')
    data11 = data1.sort_values(['COV_GDR', 'COV_AGR', 'COV_REG'], ascending=False).groupby(
        ['COV_GDR', 'COV_AGR', 'COV_REG', 'COV_ASM']).size().reset_index(name='NUM_ASM')

    # total number of case that died
    data2 = testFile.query('COV_DTH == 2')
    data22 = data2.sort_values(['COV_GDR', 'COV_AGR', 'COV_REG'], ascending=False).groupby(
        ['COV_GDR', 'COV_AGR', 'COV_REG', 'COV_DTH']).size().reset_index(name='NUM_DTH')

    result = pd.merge(data, data11, on=['COV_GDR', 'COV_AGR', 'COV_REG'], how='outer')
    final_result = pd.merge(result, data22, on=['COV_GDR', 'COV_AGR', 'COV_REG'], how='outer')
    theFinal = pd.merge(final_result, data00, on=['COV_GDR', 'COV_AGR', 'COV_REG'], how='outer')
    theFinal.to_csv('final.csv')

    data.to_csv('checkData.csv')
    data11.to_csv('checkData1.csv')
    data22.to_csv('checkData2.csv')

    dataset = pd.read_csv("final.csv")
    numCase = dataset['NUM_CASE']
    numASM = dataset['NUM_ASM']
    numDTH = dataset['NUM_DTH']
    numHSP = dataset['NUM_HSP']
    perHSP = numHSP / numCase
    perASM = numASM / numCase
    perDTH = numDTH / numCase
    dataset['PER_ASM'] = perASM
    dataset['PER_DTH'] = perDTH
    dataset['PER_HSP'] = perHSP
    dataset1 = dataset.drop(columns=['Unnamed: 0'])
    dataset1.to_csv('probability.csv')

    displayPlot(1, "Asymptomatic Distribution of Atlantic")
    displayPlot(2, "Asymptomatic Distribution of Quebec")
    displayPlot(3, "Asymptomatic Distribution of Ontario and Nunavut")
    displayPlot(4, "Asymptomatic Distribution of Prairies and the NorthWest Territories")
    displayPlot(5, "Asymptomatic Distribution of British Columbia and Yukon")
