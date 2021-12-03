import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt  # install matplotlib.pyplot

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


def uViperofRegion(region, dataProb):
    regionName = "COV_REG == " + region
    qData = dataProb.query(regionName)

    a = []
    count = 0
    for i in qData['PER_ASM']:
        if math.isnan(i):
            a.insert(count, 0)
            count += 1
        else:
            a.insert(count, i)
            count += 1

    count = 0
    b = []
    for i in qData['PER_DTH']:
        if math.isnan(i):
            b.insert(count, 0)
            count += 1
        else:
            b.insert(count, 1 - i)
            count += 1

    count = 0
    c = []
    for i in qData['PER_HSP']:
        if math.isnan(i):
            c.insert(count, 0)
            count += 1
        else:
            c.insert(count, i)
            count += 1

    ab = []
    size = len(a)
    for i in range(size):
        ab.insert(i, a[i] * b[i])

    ac = []
    for i in range(size):
        ac.insert(i, a[i] * c[i])

    bc = []
    for i in range(size):
        bc.insert(i, b[i] * c[i])

    abc = []
    for i in range(size):
        abc.insert(i, a[i] * b[i] * c[i])

    testData = {'COV_REG': region, 'a': a, 'b': b, 'c': c, 'ab': ab, 'ac': ac, 'bc': bc, 'abc': abc}
    write = pd.DataFrame(testData)
    return write


'''
Lucas viper
'''


# UViperOfRegion
# data = pd.read_csv('probability.csv')

# U-VIPER for region 1-5
def UViperofRegion(region, MinSupp):
    regionName = "COV_REG == " + region
    data = pd.read_csv('probability.csv')
    qData = data.query(regionName)

    # probability of people who have symptom
    a = []
    count = 0
    for i in qData['PER_ASM']:
        if math.isnan(i):
            a.insert(count, 0)
            count += 1
        else:
            a.insert(count, i)
            count += 1
    print("the sum of A: ", a)

    # probability of people who have died
    count = 0
    b = []
    for i in qData['PER_DTH']:
        if math.isnan(i):
            b.insert(count, 0)
            count += 1
        else:
            b.insert(count, 1 - i)
            count += 1
    print("the sum of b: ", b)

    # probability of people were in ICU
    count = 0
    c = []
    for i in qData['PER_HSP']:
        if math.isnan(i):
            c.insert(count, 0)
            count += 1
        else:
            c.insert(count, i)
            count += 1
    print("the sum of c: ", c)

    # probability of people who have symptom and died
    ab = []
    size = len(a)
    for i in range(size):
        if a[i] * b[i] >= MinSupp:
            ab.insert(i, a[i] * b[i])
        if a[i] * b[i] < MinSupp:
            ab.insert(i, 0)

    if (sum(ab) < MinSupp):
        ab.clear()

    print("the list for ab: ", ab)

    # probability of people who have symptom and were in INC
    ac = []
    for i in range(size):
        if a[i] * c[i] >= MinSupp:
            ac.insert(i, a[i] * c[i])
        if a[i] * c[i] < MinSupp:
            ac.insert(i, 0)

    if (sum(ac) < MinSupp):
        ac.clear()

    print("the list for ac: ", ac)

    # probability of people who were in ICU and died
    bc = []
    for i in range(size):
        if b[i] * c[i] >= MinSupp:
            bc.insert(i, b[i] * c[i])
        if b[i] * c[i] < MinSupp:
            bc.insert(i, 0)

    if sum(bc) < MinSupp:
        bc.clear()

    print("the sum of bc: ", bc)

    # probability of people who have sympton and were in ICU and died
    abc = []
    if ac and ab and bc:
        for i in range(size):
            if a[i] * b[i] * c[i] > MinSupp:
                abc.insert(i, a[i] * b[i] * c[i])
            if a[i] * b[i] * c[i] < MinSupp:
                abc.insert(i, 0)

    if sum(abc) < MinSupp:
        abc.clear()

    print("the sum of abc: ", abc)


# end of Lucas UViperOfRegion


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

    displayPlot(1, "symptomatic Distribution of Atlantic")
    displayPlot(2, "symptomatic Distribution of Quebec")
    displayPlot(3, "symptomatic Distribution of Ontario and Nunavut")
    displayPlot(4, "symptomatic Distribution of Prairies and the NorthWest Territories")
    displayPlot(5, "symptomatic Distribution of British Columbia and Yukon")

    w1 = uViperofRegion('1', dataset1)
    w2 = uViperofRegion('2', dataset1)
    w3 = uViperofRegion('3', dataset1)
    w4 = uViperofRegion('4', dataset1)
    w5 = uViperofRegion('5', dataset1)

    final = pd.concat([w1, w2, w3, w4, w5], ignore_index=True)
    final.to_csv('collectionForUVIPER.csv', index=False, header=True)

    # Lucas Viper
    UViperofRegion('1', 0.025)
    UViperofRegion('2', 0.025)
    UViperofRegion('3', 0.025)
    UViperofRegion('4', 0.025)
    UViperofRegion('5', 0.025)

