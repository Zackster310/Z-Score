from audioop import getsample
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('medium_data.csv')
avg = df['reading_time'].tolist()

pMean = statistics.mean(avg)
pStdDev = statistics.stdev(avg)

print("Population mean is: ", pMean)
print("Population standard deviation is: ", pStdDev)

def getSampleMean(counter):
    dataSet = []

    for i in range(0,counter):
        randIndex = random.randint(0, len(avg)-1)
        val = avg[randIndex]
        dataSet.append(val)

    mean = statistics.mean(dataSet)
    return mean

def showFigure(meanList):
    fig = ff.create_distplot([meanList], ["Sampling Mean Distribution"], show_hist = False)

    sMean = statistics.mean(meanList)
    sStdDev = statistics.stdev(meanList)

    print("Sampling mean is: ", sMean)
    print("Sampling standard deviation is: ", sStdDev)

    fsd_start,fsd_end = sMean - sStdDev, sMean + sStdDev
    ssd_start,ssd_end = sMean - (2*sStdDev), sMean + (2*sStdDev)
    tsd_start,tsd_end = sMean - (3*sStdDev), sMean + (3*sStdDev)

    interventionMean = getSampleMean(1)
    zScore = (interventionMean - sMean)/sStdDev

    print("Z Score is: ", zScore)

    fig.add_trace(go.Scatter(x = [sMean, sMean], y = [0, 0.8], mode = "lines", name = "Mean"))

    fig.add_trace(go.Scatter(x = [fsd_end, fsd_end], y = [0, 0.8], mode = "lines", name = "1st Standard Deviation"))
    fig.add_trace(go.Scatter(x = [ssd_end, ssd_end], y = [0, 0.8], mode = "lines", name = "2nd Standard Deviation"))
    fig.add_trace(go.Scatter(x = [tsd_end, tsd_end], y = [0, 0.8], mode = "lines", name = "3rd Standard Deviation"))

    fig.add_trace(go.Scatter(x = [interventionMean, interventionMean], y = [0, 0.8], mode = "lines", name = "Intervention"))
   
    fig.show()

def setup():
    meanList = []
    
    for i in range(0,100):
        mean = getSampleMean(30)
        meanList.append(mean)

    

    

    showFigure(meanList)

setup()