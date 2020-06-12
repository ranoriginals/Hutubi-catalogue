# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:55:02 2019

@author: ranor
"""

import re
import pandas as pd
import time
import requests
import random
from bs4 import BeautifulSoup as BS

baseurl = 'http://data.earthquake.cn/datashare/report.shtml?'


def post(catalogue, page_num=1, max_page_num=10):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    randnum = random.uniform(0,1)
    
    data = {'randnum':'randnum={:.17f}'.format(randnum),
            'DISPLAY_TYPE': 1,
            'PAGEID': 'earthquake_zhengshi',
            'begtime': '2011-01-01',
            'minM': 0.05,
            'maxM': 10,
            'minLon': 86.5,
            'maxLon': 87.5,
            'minLat': 43.5,
            'maxLat': 44.5,
            'minDepths': 0,
            'maxDepths': 1000,
            'endtime': '2011-12-31',
            'catalog_ALLDATASETS_RECORDCOUNT': 'catalog__default_default_default_key__default_default_default_key=4247;',
            'catalog_RECORDCOUNT': 184,
            'catalog_PAGECOUNT': max_page_num,
            'refreshComponentGuid': 'earthquake_zhengshi_guid_catalog',
            'catalog_PAGENO': page_num,
            'WX_ISAJAXLOAD': 'true'}
    session = requests.session()
    content = session.post(baseurl, headers=headers, data=data)
    process(content, catalogue)
    

def process(content, catalogue):
#    table = re.findall(r'<tr id=.+?>.+?<div style=.*?>(.+?)</div>.+?<div style=.*?>(.+?)</div>.+?<div style=.*?>(.+?)</div>.+?<div style=.*?>(.+?)</div>.+?<div style=.*?>(.+?)</div></td>', content.text)
#    print(table)
#    catalogue = pd.DataFrame(columns=['time','evlo','evla','dep','mag'])
    soup = BS(content.text,'lxml')
    row = soup.find_all('tr',attrs={"class":re.compile(r"cls-data-tr-.+?")})
#    row = soup.find_all('tr id=')[:]
    for event in row[1:]:
#        print(event)
        info = [item.string for item in event.find_all('div')][:5]
        catalogue.loc[len(catalogue.index)] = info
#    return catalogue
        
        
def main():
    catalogue = pd.DataFrame(columns=['time','evlo','evla','dep','mag'])
    max_page = 10
    for i in range(max_page):
        time.sleep(0.5)
        post(catalogue, page_num=i+1, max_page_num=max_page)
    #print(catalogue)
    catalogue.to_csv('2011.csv')


if __name__ == '__main__':
    main()
    
        
        
    
