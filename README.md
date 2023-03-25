# COMP4710_Group14_Analyzer

###  Group members
1. [Pengyu Wang](https://github.com/PengyuW007), 7863401
2. [Thomas Czubryt](https://github.com/CZUBRYTT), 7842904
3. [Hantong Li( Lucas )](https://github.com/Lucasbeast), 7845045
4. [Yue Ma( Martin )](https://github.com/mayue1998), 7824580
5. [Zhiyi Chen( Kevin )](https://github.com/Zhiyi233), 7863368

###  Repository 
[COMP4710_Group14_Analyzer](https://github.com/Skadoosh777/COMP4710_Group14_Analyzer/tree/master) 

### [Presentation](https://umanitoba-my.sharepoint.com/:f:/g/personal/czubrytt_myumanitoba_ca/Ev8hN6ZgAF1DkZIrZ6QnBlIB35Zl1jXf5IjSSNEMSH3NDQ?e=KhYFYB)
This link includes:
1. video of presentation
2. Slides of presentation

### Documents
1. [Paper](https://github.com/PengyuW007/COMP4710_Group14_Analyzer/blob/master/Big%20Data%20Analysis%20and%20Data%20Visualization%20on%20COVID-19.pdf) 
2. [Meeting Notes](https://docs.google.com/document/d/1eE0cZnfV1HN_pzAGH-NBKr6rAza0QzS-QoB-pqz-TzU/edit?usp=sharing)
3. [Mind pattern](https://docs.google.com/document/d/174AG0WoritHWgcOhJKUggi1x2X45suu2MmwSJMKS3y0/edit?usp=sharing)

###    Purpose
We are going to use our algorithm and findings in our paper to contribute to the public and make the data to be visualisation to people.

Contributions: 
1. To make the public to know the situation and how's everything of covid going by government, such as the tested cases, positive cases and so on. 

2. To show the tendency of Covid-19 , how it will go in the future. Distribution of people like ages, gender and region groups.

As the two bullet points of contributions I mentioned above,if we build a map of the number of positive cases by data visualisation, for public it is good for people to know which districts of Winnipeg are easily to be affected, or which human race(nation of people) are easier to be affected, and government can announce these group of people are better to stay at home or reduce the likelihood or frequency to go to these areas. 

### Compile and Run
Before compile
1. Whatever you run on any machine, please make sure you have python compiler:


    sudo install python3-pip
and in the newest version of python, if not, type: 

    sudo apt update
2. There are two options for you to run the algorithm: Run on Linux machine or IDE, before run it, please make sure you have installed the packages below:


    a. pandas: pip install pandas

    b. matplotlib: pip install matplotlib

Optional:

    c. numpy: pip install numpy

    d. math: pip install math
3. Compile and run: 
 a. If you are on IDE to run, just click Run button
 b. If you are on Linux machine to run, when you make sure you installed all the packages, then type: 


    python3 main.py
4. The results of data will show in the console or terminal

### Input files
1. COVID19-eng.csv: Big data file to read in
2. checkData.csv, checkData1.csv, checkData2.csv: Transition data of middle steps.
3. final.csv: Final versions of checkData files

**Links:** 

COVID19-eng.csv: All the results' input are read from "Alternative format - Compressed Archive (ZIP)", the original link of the file as shown below:

https://www150.statcan.gc.ca/n1/pub/13-26-0003/2020001/COVID19-eng.zip


### Results
There are 2 csv files of the output, 
1. probability.csv: The official result after U-Viper algorithm.
2. collectionForUViper.csv :To get the possibility of different combinations of Asymptomatic, Death and Hospital Status.

As the two bullet points of contributions I mentioned above,  if we build a map of the number of positive cases by data visualisation, for public it is good for people to know which districts of Winnipeg are easily to be affected, or which human race(nation of people) are easier to be affected, and government can announce these group of people are better to stay at home or reduce the likelihood or frequency to go to these areas.
