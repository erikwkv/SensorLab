from turtle import color, width
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import csv
from matplotlib.patches import Ellipse, Rectangle
import numpy as np
from itertools import islice
from scipy.signal import freqs



def readCSV(path, skip=0):
  data = []
  header = []  # removes first line of file
  filename = path
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip the first lines
    csvreader = islice(csvreader, skip, None)
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
  for file in range (0,len(dataList)):
    time = [p[0] for p in dataList[file]]
    colors = list(mcolors.TABLEAU_COLORS) + list(mcolors.BASE_COLORS) + list(mcolors.CSS4_COLORS)
    
    if col2==1:
      trace1 = [p[col2] for p in dataList[file]]
      plt.plot(time, trace1, "--", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file])
      trace2 = [p[col] for p in dataList[file]]
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[file] +" (output)", color=colors[file])

    elif col2==2: #relative plot of channel 2-1
      trace = [p[2]-p[1] for p in dataList[file]]
      plt.plot(time, trace, "-", alpha=0.8,label = dataLabel[file], color=colors[file])
    
    elif col2==3: #relative plot of channel 2-1 and ch1 and ch2
      trace1 = [p[1] for p in dataList[file]]
      plt.plot(time, trace1, "-", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file*3])
      trace2 = [p[2] for p in dataList[file]]
      plt.plot(time, trace2, "-", alpha=0.8, label = dataLabel[file] +" (output)", color=colors[file*3+1])

      trace3 = [p[2]-p[1] for p in dataList[file]]
      plt.plot(time, trace3, "-", alpha=0.8, label = dataLabel[file] +" (normalisert)", color=colors[file*3+2])

    elif col2==4: #both plot with input and output, but all data offset 10 dB
      # trace1 = [p[1]+file*10 for p in dataList[file]]
      # plt.plot(time, trace1, "--", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file])
      trace2 = [p[2]+file*10 for p in dataList[file]]
      # plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[file] +" (output)", color=colors[file])
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[file], color=colors[file])

    elif col2==5: #relative plot of channel 2-1 and ch1 and ch2 and simulation
      trace1 = [p[1] for p in dataList[file]]
      plt.plot(time, trace1, "-", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file*4])
      trace2 = [p[2] for p in dataList[file]]
      plt.plot(time, trace2, "-", alpha=0.8, label = dataLabel[file] +" (output)", color=colors[file*4+1])

      trace3 = [p[2]-p[1] for p in dataList[file]]
      plt.plot(time, trace3, "-", alpha=0.8, label = dataLabel[file] +" (normalisert)", color=colors[file*4+2])

      #simulated filter
      freqs = np.linspace(0.1,20_000_000,200_000_000)
      # R_1 = 0.2
      R_2 = 7.5
      L = 403e-3
      # C_1 = 520e-6
      C_2 = 470.1e-6
      # amp = abs(H_tot(omegas,L,C_1,C_2,R_1,R_2))

      amp1 = np.abs(1/(1-(2*np.pi*freqs)**2*C_2*L+1j*(2*np.pi*freqs)*R_2*C_2))

      w_c = np.sqrt((np.sqrt(C_2**2 *R_2**4 - 4*C_2*L *R_2**2 + 8*L**2) - C_2* R_2**2 + 2* L)/(C_2* L**2))/np.sqrt(2)
      
      f_c = w_c/(2*np.pi)
      print(f_c)

      plt.plot(freqs,20*np.log10(amp1), label = "Simulert filter", color=colors[file*4+3])

    elif col2==6: #relative plot of channel 2-1 and ch1 and ch2
      
      if file < 2:
        trace1 = [p[2] - p[1] for p in dataList[file]]
        plt.plot(time, trace1, "-", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file*3])
      else:
        trace1 = [p[3]*2 for p in dataList[file]]
        plt.plot(time, trace1, "-", alpha=0.8, label = dataLabel[file]+" (input)", color=colors[file*3])
        

    else:  
      trace2 = [p[col] for p in dataList[file]]
      plt.plot(time, trace2, "-", alpha=0.8,label = dataLabel[file], color=colors[file])
    

  #labels  
  plt.xlabel("Frekvens [Hz]")
  plt.ylabel("Magnitude [dB]")
  
  
  
  #Final touch
  if (line):
    plt.axhline(y=-3, color='r', linestyle='dotted', label='-3dB')

    if col2==5:
        plt.axvline(x=13.133, ymin=-0.95, ymax=0.98, linestyle = (0,(2,5)), color = 'tab:red',label='$f_c  = 13.133$ Hz')
        plt.axhline(y=-28.257095972522, color='b', linestyle='dotted', label='-28.3dB')
        plt.axvline(x=18_000_000, ymin=-0.95, ymax=0.98, linestyle = (0,(1,5)), color = 'tab:blue',label='$f_{støy}  = 18$ MHz')
  # ellipse = Ellipse(xy=(580, -24), width=900, height=10, 
  #                       edgecolor='r', fc='None', lw=2)
  # ax.add_patch(ellipse)
  
  #ypoints = [(0,580),(-44,580)]

  #plt.plot(ypoints, linestyle = 'dotted')
#   plt.axvline(x=5900, ymin=-0.95, ymax=0.95, linestyle = (0,(2,5)), color = 'cyan',label='$f_s = 5650$ Hz')
#   plt.axvline(x=2950, ymin=-0.95, ymax=0.95, linestyle = (0,(2,5)), color = 'magenta',label=r'$\frac{ f_s}{2} = 2950$ Hz')
  # plt.axvline(x=13.133, ymin=-0.95, ymax=0.98, linestyle = (0,(2,5)), color = 'tab:red',label='$f_c  = 13.133$ Hz')
  # plt.axvline(x=18_000_000, ymin=-0.95, ymax=0.98, linestyle = (0,(1,5)), color = 'tab:blue',label='$f_{støy}  = 18$ MHz')
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
  for i in range (0,len(fileList)-1):
    dataList.append(readCSV(fileList[i], 25))

  dataList.append(readCSV(fileList[len(fileList)-1], 0))
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
  print("\n\nStatistics\n\n")
  print("Signal length: ", (time[-1]-time[0])*1000, "ms")  
  print("Samples: ", len(time))
  variance1 = np.var(trace1)
  variance2 = np.var(trace2)
  print("Variance of trace1: ", round(variance1, 8))
  print("Variance of trace2: ", round(variance2, 8))
  std_dev1 = np.std(trace1)
  std_dev2 = np.std(trace2)
  print("Standard deviation of trace1: ", round(std_dev1*1000, 2) , "mV")
  print("Standard deviation of trace2: ", round(std_dev2*1000, 2) , "mV")
  print("Mean of trace1: ", round(np.mean(trace1)*1000, 2), "mV")
  print("Mean of trace2: ", round(np.mean(trace2)*1000, 2), "mV")
  print("Peak to peak of trace1: ", round((max(trace1)-min(trace1))*1000, 2), "mV")
  print("Peak to peak of trace2: ", round((max(trace2)-min(trace2))*1000, 2), "mV")
  print("RMS of trace1: ", round(np.sqrt(np.mean(np.square(trace1)))*1000, 2), "mV")
  print("RMS of trace2: ", round(np.sqrt(np.mean(np.square(trace2)))*1000, 2), "mV")

  print("Damping factor of variance (dB): ", round(20 * np.log10(np.sqrt(variance2/variance1)), 2))
  print("Damping factor of standard deviation (dB): ", round(20 * np.log10(std_dev2/std_dev1), 2))
  print("Damping factor of mean (dB): ", round(20 * np.log10(np.mean(trace2)/np.mean(trace1)), 5))
  print("Damping factor of peak to peak (dB): ", round(20 * np.log10((max(trace2)-min(trace2))/(max(trace1)-min(trace1))), 2))
  # print("Damping factor of RMS (dB): ", round(20 * np.log10(np.sqrt(np.mean(np.square(trace1)))/np.sqrt(np.mean(np.square(trace2))), 2)))


  #labels  
  plt.xlabel("Tid [ms]")
  plt.ylabel(r"Spenning [V]")
  # plt.ylabel(r"Magnitude (Peak Hold Cont.) [dB$\tilde{V}$]")
  
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

#phase(dataList, dataLabel,2)
plt.rcParams.update({'font.size': 16})

#Plotting theoretical bode diagram from the frequency response of the filter.
def theoretical_bode_plot(R,C,L):
  freqs = np.linspace(0.1,10000,100000)
  R_2 = 6.6+11
  L = 403e-3
  # C_1 = 520e-6
  C_2 = 470.1e-6
  def freq_resp(R,C,L,freqs):
    return np.abs(1/(1-(2*np.pi*freqs)**2*C*L+1j*(2*np.pi*freqs)*R*C))

  #cut-off frequency
  w_c = np.sqrt((np.sqrt(C_2**2 *R_2**4 - 4*C_2*L *R_2**2 + 8*L**2) - C_2* R_2**2 + 2* L)/(C_2* L**2))/np.sqrt(2)
  f_c = w_c/(2*np.pi)
  amp_resp = abs(freq_resp(R,C,L,freqs))

  fig, ax = plt.subplots(1,figsize=(10,10))
  ax.set_xscale('log')
  ax.plot(freqs,20*np.log10(amp_resp))
  #-3dB line
  print(f_c)
  ax.axhline(y=-3,color='red',linestyle='--')
  #cut-off frequency
  ax.axvline(x=f_c,color='red',linestyle='--',label=f'f_c = {f_c:.2f} Hz')
  ax.set_title(f"Frekvensrespons av pi-filteret")
  ax.set_xlabel("Frekvens [Hz]")
  ax.set_ylabel("Relativ amplitude [dB]")
  ax.legend()
  ax.grid()
  plt.show()
  fig.savefig('bode_theoretical.png')

# theoretical_bode_plot(15,470.1e-6,403e-3)


bodefiles = ["bode/filter3V3_bode_v3_11ohm_series.csv","bode/filter3V3_bode_v4_11ohm_series.csv"]
dataLabel = ["filter3V3_v3_11ohm_series","filter3V3_v4_11ohm_series"]


bodefiles = ["Lab4\BP-A-MCP6002-samples201.csv","Lab4\BP-B-MCP6002-samples201.csv","Lab4\Simulert-bodeplot.csv"]
label = ["A","B","Simulert"]
bodeDiagram(bodefiles, label,6, True,4)

# # scope test of filter 
# dataLabel = ["input","output"]
# scopeFiles2 = ["bode/3V3filter_skop.csv"]
# scope(scopeFiles2,dataLabel)













faseFiles= [""]
# dataLabel.reverse()
# faseFiles.reverse()
# faseDiagram(faseFiles,dataLabel)