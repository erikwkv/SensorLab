from turtle import color, width
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import csv
from matplotlib.patches import Ellipse, Rectangle
import numpy as np
from itertools import islice
def readCSV(path):
  data = []
  header = []  # removes first line of file
  filename = path
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip the first 20 lines
    csvreader = islice(csvreader, 20, None)
    # set header to first remaining line
    header = next(csvreader)
    for datapoint in csvreader:
      values = [float(value) for value in datapoint]
      data.append(values)
  return data

def magnitudeBode(dataList, dataLabel,col, col2=-1, line=True,legend_cols=3):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  # plt.minorticks_on()
  #max num ticks in axis
  max_yticks = 15
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)
  ax.tick_params(which='major', length=8)
  ax.tick_params(which='minor', length=6)
  ax.tick_params(which='both', width=1)
  #ax.yaxis.set_minor_locator(AutoMinorLocator())
  #Use log scale  
  ax.set_xscale('log')
  #ax.set_yscale('log')

  #plt.title('Bode diagram demping')
  plt.grid(True)
  
  #ax.xaxis.minorTicks()
  #ax.xaxis.grid(b=True, which='minor', linestyle=(0, (1,3)))

  print(col2)
  #plot data
  for i in range (0,len(dataList)):
    time = [p[0] for p in dataList[i]]
    colors = list(mcolors.TABLEAU_COLORS) + list(mcolors.BASE_COLORS) + list(mcolors.CSS4_COLORS)
    
    if col2==1:
      trace1 = [p[col2] for p in dataList[i]]
      plt.plot(time, trace1, "--", alpha=0.8, label = dataLabel[i]+" (input)", color=colors[i])
      trace2 = [p[col] for p in dataList[i]]
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[i] +" (output)", color=colors[i])
    elif col2==2: #relative plot of channel 2-1
      trace = [p[2]-p[1] for p in dataList[i]]
      plt.plot(time, trace, "-", alpha=0.8,label = dataLabel[i], color=colors[i])
    
    elif col2==3: #relative plot of channel 2-1 and ch1 and ch2
      trace1 = [p[1] for p in dataList[i]]
      plt.plot(time, trace1, "-", alpha=0.8, label = dataLabel[i]+" (input)", color=colors[i*3])
      trace2 = [p[2] for p in dataList[i]]
      plt.plot(time, trace2, "-", alpha=0.8, label = dataLabel[i] +" (output)", color=colors[i*3+2])

      trace3 = [p[2]-p[1] for p in dataList[i]]
      plt.plot(time, trace3, "-", alpha=0.8, label = dataLabel[i] +" (shifted)", color=colors[i*3+1])
    elif col2==4: #both plot with input and output, but all data offset 10 dB
      # trace1 = [p[1]+i*10 for p in dataList[i]]
      # plt.plot(time, trace1, "--", alpha=0.8, label = dataLabel[i]+" (input)", color=colors[i])
      trace2 = [p[2]+i*10 for p in dataList[i]]
      # plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[i] +" (output)", color=colors[i])
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[i], color=colors[i])
    
    else:  
      trace2 = [p[col] for p in dataList[i]]
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[i], color=colors[i])
    

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Magnitude [dB]")
  
  
  
  #Final touch
  if (line):
    plt.axhline(y=-3, color='r', linestyle='dotted', label='-3dB')
  # ellipse = Ellipse(xy=(580, -24), width=900, height=10, 
  #                       edgecolor='r', fc='None', lw=2)
  # ax.add_patch(ellipse)
  
  #ypoints = [(0,580),(-44,580)]

  #plt.plot(ypoints, linestyle = 'dotted')
#   plt.axvline(x=5900, ymin=-0.95, ymax=0.95, linestyle = (0,(2,5)), color = 'cyan',label='$f_s = 5650$ Hz')
#   plt.axvline(x=2950, ymin=-0.95, ymax=0.95, linestyle = (0,(2,5)), color = 'magenta',label=r'$\frac{ f_s}{2} = 2950$ Hz')
#plt.axvline(x=2212.5, ymin=-0.95, ymax=0.95, linestyle = (0,(2,5)), color = 'tab:red',label='$f_c  = 2212,5$ Hz')
#   #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=legend_cols, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])

  plt.show()

def magnitudeSpektrum(dataList, dataLabel,col, col2=-1):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  #ax.set_xscale('log')
  #ax.set_yscale('log')

  #plot data
  time = [p[0]/1000 for p in dataList[0]]

  trace1 = [p[col] for p in dataList[0]]
  trace2 = [p[col2] for p in dataList[0]]
  plt.plot(time, trace1, "-", alpha=1)
  plt.plot(time, trace2, "-", alpha=1)
  # trace2 = [p[3] for p in dataList[0]]
  # plt.plot(time, trace2, "-", alpha=1)
  #plt.plot(time, trace1, "-", alpha=0.8)
  print(np.average(trace1))
  print (len(dataList))  
  for i in range (1,len(dataList)):
    if col2!=-1 :
      print (col2)  
      trace1 = [p[col] for p in dataList[i]]
      trace2 = [p[col2] for p in dataList[i]]
      plt.plot(time, trace1, ":", alpha=0.8)
      plt.plot(time, trace2, ":", alpha=0.8)
      #plt.plot(time, trace1, "-")
    
    

  #labels  
  plt.xlabel("Frekvens [kHz]")
  plt.ylabel(r"Lineær RMS gjennomsnitt [dB]")
  # plt.ylabel(r"Magnitude (Peak Hold Cont.) [dB$\tilde{V}$]")
  
  #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(
    dataLabel,
    bbox_to_anchor=(0.5, -0.15),
    loc="upper center",
    fancybox=True,
    borderaxespad=0
  )
  plt.tight_layout(rect=[0,0,1,0.98])

  #ellipse = Ellipse(xy=(580, -24), width=900, height=10, edgecolor='r', fc='None', lw=2)
  #ax.add_patch(ellipse)
  #add rectangle
  # plt.gca().add_patch(Rectangle((250,-100),1000,80,edgecolor='red',facecolor='none',lw=2))
  
  #Final touch
  #plt.title('Spektrum diagram')
  plt.grid(True)
  plt.show()

def phase(dataList, dataLabel,col):
  #Figure size (x,y) in inches. Move Legend if changed drasticly
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 20 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  ax.set_xscale('log')
  # ax.set_yscale('log')

  #plot data
  for i in range (0,len(dataList)):
    time = [p[0] for p in dataList[i]]
    measurement = [p[col] for p in dataList[i]]
    plt.plot(time, measurement, "-")

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Fase [grader]")
  
  #Legend
  plt.legend(
    dataLabel,
    bbox_to_anchor=(0.5, -0.1),
    loc="upper center",
    fancybox=True,
    ncol=3,
    borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])
  
  #Final touch
  plt.grid(True)
  plt.title('Bode diagram fase')
  plt.show()

def bodeDiagram(fileList,dataLabel,mode, line=True, legend_cols=3):
  if len(fileList)>len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  magnitudeBode(dataList, dataLabel,2,mode, line, legend_cols)
  #phase(dataList, dataLabel,3)

def spektrumDiagram(fileList,dataLabel):
  if len(fileList)!=len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  magnitudeSpektrum(dataList, dataLabel,1,3)
  # xyPlot(dataList, dataLabel,1,3)
  
  
def xyPlot(dataList, dataLabel,col, col2=-1):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(7, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  #ax.set_xscale('log')
  #ax.set_yscale('log')

  #plot data
  # time = [p[0] for p in dataList[0]]
  # trace1 = [p[1] for p in dataList[0]]
  # trace2 = [p[2] for p in dataList[0]]
  # plt.plot(trace2, trace1, ".", alpha=1)
  #plt.plot(time, trace1, "-", alpha=0.8)
    
  for i in range (0,len(dataList)):
    
    
    
    if col2!=-1:
      trace1 = [p[0]*1000 for p in dataList[i]]
      trace2 = [p[1] for p in dataList[i]]
      # trace3 = [p[2] for p in dataList[i]]
      plt.plot(trace1, trace2, "-", alpha=0.7)
      # plt.plot(trace1, trace3, "-", alpha=0.7)
      #plt.plot(time, trace1, "-")
    
    

  #labels  
  plt.xlabel("tid [ms]")
  plt.ylabel("Spenning [V]")
  
  #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(dataLabel, bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=2, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])

  #ellipse = Ellipse(xy=(580, -24), width=900, height=10, edgecolor='r', fc='None', lw=2)
  #ax.add_patch(ellipse)
  #add rectangle
  # plt.gca().add_patch(Rectangle((250,-100),1000,80,edgecolor='red',facecolor='none',lw=2))
  
  #Final touch
  #plt.title('Spektrum diagram')
  plt.grid(True)
  plt.show()  
  
def faseDiagram(fileList,dataLabel):
  if len(fileList)!=len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  xyPlot(dataList, dataLabel,1,2)


def scope(fileList,dataLabel):
  if len(fileList)!=len(dataLabel):
    print("\n\nMissing labels for grafs\n\n")
  dataList= []
  for i in range (0,len(fileList)):
    dataList.append(readCSV(fileList[i]))
  scopeGraph(dataList, dataLabel,1,2)

def scopeGraph(dataList, datalabel,col, col2=-1):
  #Figure size (x,y) in inches. Move Legend if changed drasticly to avoid clipping
  fig = plt.figure(1, figsize=(14.5, 6.5))
  
  #number of rows/cols of subplots 
  ax = fig.add_subplot(1, 1, 1)
  
  #max num ticks in axis
  max_yticks = 20
  max_xticks = 10 #irrelevant due to log scale
  yloc = plt.MaxNLocator(max_yticks)
  xloc = plt.MaxNLocator(max_xticks)
  ax.yaxis.set_major_locator(yloc)
  ax.xaxis.set_major_locator(xloc)

  #Use log scale  
  #ax.set_xscale('log')
  # ax.set_yscale('log')

  #plot data
  time = [p[0]*1000 for p in dataList[0]]
  trace1 = [p[col] for p in dataList[0]]
  trace2 = [p[col2] for p in dataList[0]]
  plt.plot(time, trace1, "-", alpha=1)
  plt.plot(time, trace2, "-", alpha=1)
  # trace2 = [p[3] for p in dataList[0]]
  # plt.plot(time, trace2, "-", alpha=1)
  #plt.plot(time, trace1, "-", alpha=0.8)
  print(np.average(trace1))
  print (len(dataList))  
  for i in range (1,len(dataList)):
    if col2!=-1 :
      print (col2)  
      trace1 = [p[col] for p in dataList[i]]
      trace2 = [p[col2] for p in dataList[i]]
      plt.plot(time, trace1, ":", alpha=1)
      plt.plot(time, trace2, ":", alpha=1)
      #plt.plot(time, trace1, "-")
    
    

  #labels  
  plt.xlabel("Tid [ms]")
  plt.ylabel(r"Spenning [V]")
  # plt.ylabel(r"Magnitude (Peak Hold Cont.) [dB$\tilde{V}$]")
  
  #legend. Source: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
  plt.legend(dataLabel, bbox_to_anchor=(0.5, -0.15), loc="lower center",fancybox=True, ncol=3, borderaxespad=0)
  plt.tight_layout(rect=[0,0,1,0.98])

  #ellipse = Ellipse(xy=(580, -24), width=900, height=10, edgecolor='r', fc='None', lw=2)
  #ax.add_patch(ellipse)
  #add rectangle
  # plt.gca().add_patch(Rectangle((250,-100),1000,80,edgecolor='red',facecolor='none',lw=2))
  
  #Final touch
  #plt.title('Spektrum diagram')
  plt.grid(True)
  plt.show()

#phase(dataList, dataLabel,2)
plt.rcParams.update({'font.size': 16})



#bodefiles = ["bode/3V3filter_bode_v1.csv", "bode/3V3filter_bode_v2_11ohm_series.csv","bode/3V3filter_bode_v2_17ohm_series.csv","bode\3V3filter_bode_v2_33ohm_series.csv","bode/3V3filter_bode_v2_100ohm_series.csv","bode/3V3filter_bode_v2.csv"]
#bodefiles = ["bode/3V3filter_bode_v1.csv","bode/3V3filter_bode_v2_11ohm_series.csv","bode/3V3filter_bode_v2_17ohm_series.csv","bode/3V3filter_bode_v2_100ohm_series.csv","bode/3V3filter_bode_v2.csv"]

# #amplitudetest
# bodefiles = ["bode/3V3filter_bode_v4_uten_last.csv","bode/3V3filter_bode_v4_1V_amplitude_uten_last.csv"]
# dataLabel = ["0.2V amplitude","1V amplitude"]
# bodeDiagram(bodefiles, dataLabel,1)

# #seriemotstand test
# bodefiles = ["bode/3V3filter_bode_v4_10.6ohm_uten_last.csv","bode/3V3filter_bode_v4_uten_last.csv"]
# dataLabel = ["Med seriemotstand","uten seriemotstand"]
# bodeDiagram(bodefiles, dataLabel,1)

# #shifted view
# bodefiles = ["bode/3V3filter_bode_v4_10.6ohm_uten_last.csv"]
# dataLabel = ["Med seriemotstand"]
# bodeDiagram(bodefiles, dataLabel,3)

# average test
# bodefiles = ["bode/amplitude/3V3filter_bode_v4_10mV_mean1.csv","bode/amplitude/3V3filter_bode_v4_10mV_mean10.csv","bode/amplitude/3V3filter_bode_v4_10mV_mean20.csv","bode/amplitude/3V3filter_bode_v4_10mV_mean50.csv","bode/amplitude/3V3filter_bode_v4_10mV_mean100.csv"]
# dataLabel = ["1 sample","10 samples","20 samples","50 samples","100 samples"]
# bodeDiagram(bodefiles, dataLabel,4, False)

# # amplitude test -> discover wedge issue
# bodefiles = ["bode/amplitude-med-wedge/3V3filter_bode_v4_10mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_20mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_50mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_100mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_200mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_500mV_mean10.csv","bode/amplitude-med-wedge/3V3filter_bode_v4_1000mV_mean10.csv"]
# dataLabel = ["10 mV","20 mV","50 mV","100 mV","200 mV","500 mV","1000 mV"]
# bodeDiagram(bodefiles, dataLabel,1, False,5)
# bodeDiagram(bodefiles, dataLabel,2, True,5)

# amplitude test without wedge
bodefiles = ["bode/amplitude-uten-wedge/3V3filter_bode_v4_10mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_20mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_50mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_100mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_200mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_500mV_mean10.csv","bode/amplitude-uten-wedge/3V3filter_bode_v4_1000mV_mean10.csv"]
dataLabel = ["10 mV","20 mV","50 mV","100 mV","200 mV","500 mV","1000 mV"]
bodeDiagram(bodefiles, dataLabel,1, False,5)
bodeDiagram(bodefiles, dataLabel,2, True,5)

# bodefiles = ["bode\filter3V3_bode_v3_11ohm_series.csv","bode\filter3V3_bode_v4_11ohm_series.csv"]
# dataLabel = ["filter3V3_v3_11ohm_series","filter3V3_v4_11ohm_series"]

# bodeDiagram(bodefiles, dataLabel)

spektrumFiles = ["Data\D7 spektrum 100 Amaks, 5mA.csv","Data\D7 spektrum 100k Amaks, 5mA.csv"]

# "Jord","$v_2$","$v_1$","$R_2$ = 718$\Omega$","$R_2$ = 5k$\Omega$","$R_2$ = 10,2k$\Omega$"
#spektrumDiagram(spektrumFiles,dataLabel)

dataLabel = ["VIN ved 100$\Omega$ & $A_{10}$","VOUT ved 100$\Omega$ & $A_{10}$","VIN ved 100k$\Omega$ & $A_{10}$","VOUT ved 100k$\Omega$ & $A_{10}$","1","2","3"]

scopeFiles = ["Data\D7 skop 100Ohm A10, 90mA.csv","Data\D7 skop 100k A10, 90mA.csv"]
# scope(scopeFiles,dataLabel)


dataLabel = ["VIN 100k","VOUT 100k","VIN 100","VOUT 100","1","2","3"]

scopeFiles2 = ["Data\D7 skop RL 100 A10 4mV.csv"]
# scope(scopeFiles2,dataLabel)






faseFiles= ["skop squarewave only close.csv","skop impulse and square close.csv"]
# dataLabel.reverse()
# faseFiles.reverse()
# faseDiagram(faseFiles,dataLabel)