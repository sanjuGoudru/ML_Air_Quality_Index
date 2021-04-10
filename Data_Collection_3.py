# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:40:39 2021

@author: Sanjay G R
"""

from Cleaning_Data_2 import avg_data_per_year
import requests, sys, os, csv, pandas as pd
from bs4 import BeautifulSoup


def met_data(month,year):
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    plain_text = file_html.read()
    
    tempD,finalD = [],[]
    
    soup = BeautifulSoup(plain_text,'lxml')
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
                
    rows = len(tempD) / 15
    
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
        

    finalD.pop(len(finalD)-1)
    finalD.pop(0)
    
    for a in range(len(finalD)):
        finalD[a].pop(14)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(6)
        finalD[a].pop(4)
        finalD[a].pop(0)
        
    return finalD


def data_combine(years,cs):
    data_arr = []
    for year in years:
        for a in pd.read_csv('Data/Real_Data/real_'+str(year)+'.csv',chunksize=cs):
            df = pd.DataFrame(data=a)
            print(year,' : ',len(df))
            data = df.values.tolist()
        data_arr.append(data)
    print('Data Arr : ',len(data_arr))
    
    with open('Data/Real_Data/Real_Combine.csv','w',newline='') as csvfile:
        wr = csv.writer(csvfile,dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm','H', 'VV', 'V', 'VM', 'PM 2.5'])
        for data in data_arr:
            wr.writerows(data)

if __name__ == '__main__':
    if not os.path.exists('Data/Real_Data'):
        os.makedirs('Data/Real_Data')
    
    for year in range(2013,2019):
        final_data = []
        
        for month in range(1,13):
            temp = met_data(month,year)
            final_data = final_data+temp
                
        pm = avg_data_per_year(year)
        
        if len(pm) == 364:
            pm.insert(364,'-')
        
        if year==2016:
            pm.insert(365,'-')
        
        for i in range(len(final_data)):
            final_data[i].insert(7, pm[i])
        
        #print(year,' : ',len(final_data))
        with open('Data/Real_Data/real_'+str(year)+'.csv','w',newline='') as csvfile:
            wr = csv.writer(csvfile,dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == '-':
                        flag = 1
                            
                if flag != 1:
                    if len(row) != 8:
                        print(row,'------\n')
                    wr.writerow(row)
                    

    data_combine(range(2013,2019),600)
    
    
    
    #with open('Data/Real_Data/Real_Combine.csv','w') as csvfile:
        
    
##def data_combine(year):
##    for a in pd.read_csv()                