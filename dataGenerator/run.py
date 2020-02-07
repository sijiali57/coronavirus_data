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
import time

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

def downloadDataToDF(url):
    r=requests.request('GET', url)
    data=r.json()
    return pd.DataFrame.from_records(data['results'])

def downloadData(url):
    r=requests.request('GET', url)
    data=r.json()
    return data['results']

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

def areaMapping(data):
    country=[]
    provice=[]
    totalConfirmed=[]
    totalSus=[]
    totalDead=[]
    totalCure=[]
    confirmed=[]
    updateTime=[]
    sus=[]
    cure=[]
    dead=[]
    city=[]


    for i in range(0, len(data)):
        b=data[i]
        country_info = b['country']
    #     provinceShortName_info = b['provinceShortName']
        province_info = b['provinceName']
        confirmedCount_info = b['confirmedCount']
        suspectedCount_info = b['suspectedCount']
        curedCount_info = b['curedCount']
        deadCount_info = b['deadCount']
        updateTime_info=b['updateTime']
        if b['cities'] != None:        
            j_range=len(b['cities'])
            for j in b['cities']:
                country.append(country_info)
                provice.append(province_info)
                totalConfirmed.append(confirmedCount_info)
                totalSus.append(suspectedCount_info)
                totalDead.append(deadCount_info)
                totalCure.append(curedCount_info)
                city.append(j['cityName'])
                confirmed.append(j['confirmedCount'])
                sus.append(j['suspectedCount'])
                cure.append(j['curedCount'])
                dead.append(j['deadCount'])
                updateTime.append(updateTime_info)
        else:
            country.append(country_info)
            provice.append(province_info)
            totalConfirmed.append(confirmedCount_info)
            totalSus.append(suspectedCount_info)
            totalDead.append(deadCount_info)
            totalCure.append(curedCount_info)
            city.append(province_info)
            confirmed.append(confirmedCount_info)
            sus.append(suspectedCount_info)
            cure.append(curedCount_info)
            dead.append(deadCount_info)
            updateTime.append(updateTime_info)
    
    output={'Country':country,
            'Province':provice,
            'TotalConfirmedCount':totalConfirmed,
            'TotalSuspectedCount':totalSus,
            'TotalDeadCount':totalDead,
            'TotalCuredCount':totalCure,
            'City':city,
            'CityCount':confirmed,
            'CitySuspectedCount':sus,
            'CityCuredCount':cure,
            'CityDeadCount':dead,
            'DataUpdateTime':updateTime}
    return output
    

if __name__ == '__main__':
    start_time = time.time()

    overall = downloadDataToDF(OVERALL_URL)
    dataMapping(overall)
    overall.to_csv('~/coronavirus_data/dataSource/overall.csv', index=False, encoding='utf_8_sig')
    print("overall file downloaded successfully")

    end_time_1 = time.time()
    part_1_time = end_time_1-start_time
    print ("overall running time: ", part_1_time)
    
    area = downloadData(AREA_URL)
    area_output=areaMapping(area)
    area_output =pd.DataFrame(area_output)
    area_output['DataUpdateTime']=convertTime(area_output['DataUpdateTime'])
    area_output['City']=tranlateToEng(area_output['City'])
    area_output['Country']=tranlateToEng(area_output['Country'])
    area_output.to_csv('~/coronavirus_data/dataSource/area_breakDown.csv', index=False, encoding='utf_8_sig')
    
    end_time = time.time()
    process_time = end_time - start_time
    print("area file downloaded successfully")
    print("total running time: ", process_time)
    


