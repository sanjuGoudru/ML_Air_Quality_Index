# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:24:17 2021

@author: Sanjay G R
"""

import pandas as pd, matplotlib.pyplot as plt
import time

def avg_data_per_year(year):
    temp_i = 0
    average = []
    
    for rows in pd.read_csv('./Data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_var,avg = 0,0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i not in ['NoData','PwrFail','InVld','---']:
                    temp = float(i)
                    add_var = add_var + temp
        
        avg = add_var/24
        temp_i = temp_i +1
        
        average.append(avg)
    #print('Returning avg:',len(average))
    return average



def plot_data(average,year):
    #print('In plot')
    plt.plot(range(len(average)),average,label='{}'.format(year))
    
if __name__ == '__main__':
    start_time = time.time()
    
    avg_lst = []    
    for year in [2013,2014,2015,2016,2017,2018]:
        average = avg_data_per_year(year)
        avg_lst.append(average)
        plot_data(average,year)
    
    plt.xlabel('Day')
    plt.ylabel('PM2.5')
    plt.legend(loc='upper right')
    plt.show()
    stop_time = time.time()
    
    #print('Time taken: {}'.format(stop_time-start_time))