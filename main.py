import pandas as pd

'''yue ma tests, '''
testFile = pd.read_csv("COVID19-eng.csv")  # COVID19-eng.csv, official path repository




# print("COMP 4710 Group 14 Analyzer.\n")

if __name__ == '__main__':

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
