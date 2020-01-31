"""
@ProjectName: coronavirus_data
@APISource: DXY-2019-nCoV-Crawler
@FileName: run.py
@Author: sijiali57
@Date: 2020/1/31
"""

from googletrans import Translator
import requests
import pandas as pd
import datetime

OVERALL_URL ="https://lab.isaaclin.cn/nCoV/api/overall?latest=0"
AREA_URL = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1'

def tranlateToEng(input_text):
    output=[]
    input_text = input_text.astype(str) 
    for i in input_text:
        translator = Translator()
        eng = translator.translate(i).text
        output.append(eng)
    return output

def convertTime(x):
    output=[]
    for i in x:
        a=datetime.datetime.fromtimestamp( i/ 1e3)
        a=a.strftime('%Y%m%d%H%m')
        output.append(a)
    return output

def downloadData(url):
    r=requests.request('GET', url)
    data=r.json()
    return pd.DataFrame.from_records(data['results'])

def dataMapping(data):
# comment out due to GoogleTranslate API call limits - if run this too many times, then google will temp block your IP
#     data['generalRemark_eng']=tranlateToEng(data['generalRemark'])
#     data['infectSource_eng']=tranlateToEng(data['infectSource'])
#     data['passWay_eng']=tranlateToEng(data['passWay'])
#     data['remark1_eng']=tranlateToEng(data['remark1'])
#     data['remark2_eng']=tranlateToEng(data['remark2'])
#     data['virus_eng']=tranlateToEng(data['virus'])
    data['generalRemark_eng'] ="The number of suspected cases of data from the National Health health committee, currently national data, not sub-provinces etc."
    data['infectSource_eng'] ="Wild animals, may bat for the Chinese chrysanthemum head"
    data['passWay_eng'] ="Via respiratory droplets, may also be spread through contact with"
    data['remark1_eng']="Susceptible people: The population is generally susceptible. The elderly and those with underlying diseases are more ill after infection, and children, infants and young children also have symptoms"
    data['remark2_eng']="Incubation period: Generally 3 ~ 7 days, the longest is no more than 14 days, contagious period exists"
    data['virus_eng']="2019-nCoV"
    data['dataDate']=convertTime(data['updateTime'])

if __name__ == '__main__':
#     overall = downloadData(OVERALL_URL)
#     dataMapping(overall)
#     overall.to_csv('~/coronavirus_data/dataSource/overall.csv', index=False, encoding='utf_8_sig')
    area = downloadData(AREA_URL)
    area.to_csv('~/coronavirus_data/dataSource/overall.csv', index=False, encoding='utf_8_sig')
    print("files downloaded successfully")
