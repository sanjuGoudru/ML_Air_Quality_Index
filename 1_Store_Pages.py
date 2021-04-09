# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:15:25 2021

@author: Sanjay G R
"""

## This will store the climate data of banglore from 2013 to 2019 of all the months in 'Html_Data' folder
import os, time,requests,sys

def retrieve_html():
    for year in range(2013,2020):
        for month in range(1,13):
            print('{} {}'.format(year,month))
            if month > 9:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            #print(url)
    
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
            
            if not os.path.exists('./Data/Html_Data/{}'.format(year)):
                os.makedirs('./Data/Html_Data/{}'.format(year))
            with open('./Data/Html_Data/{}/{}.html'.format(year,month),'wb') as output:
                output.write(text_utf)
                
        sys.stdout.flush()
            
            
if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    retrieve_html()
    stop_time = time.time()
    print('Time taken: {}'.format(stop_time-start_time))