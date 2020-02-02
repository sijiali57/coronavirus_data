# Coronavirus Data Visulazation

*All data from this repo is based on [DXY-2019-nCoV-Crawler API](https://github.com/BlankerL/DXY-2019-nCoV-Crawler). If you want to see the original raw data please use this repo.*

if the API server is down then this repo won't be updated until the server is back. Please use below API status to check the server status:

[![API Status](https://img.shields.io/website?url=https%3A%2F%2Flab.isaaclin.cn)](https://lab.isaaclin.cn/nCoV/)


_______________

This repo is for displaying the current coronavirus latest status (confirmed cases, suspected cases, recovered cases and death cases).


There are 2 main data sources:

* Overall by daily rates

```
abroadRemark         object
confirmedCount       int64
countRemark          object
curedCount           int64
dailyPic             object
deadCount            int64
generalRemark        object
infectSource         object
passWay              object
remark1              object
remark2              object
remark3              object
remark4              object
remark5              object
summary              object
suspectedCount       int64
updateTime           int64
virus                object
generalRemark_eng    object
infectSource_eng     object
passWay_eng          object
remark1_eng          object
remark2_eng          object
virus_eng            object
dataDate             object

```

* States, cities by daily rates

```
Country                object
Province               object
TotalConfirmedCount    int64
TotalSuspectedCount    int64
TotalDeadCount         int64
TotalCuredCount        int64
City                   object
CityCount              int64
CitySuspectedCount     int64
CityCuredCount         int64
CityDeadCount          int64
DataUpdateTime         object
```



####Update Time: Everyday 9, 12, 16, 22 UTC time

*Changelog:* 

1.0.0 - 2020-01-31 - "translated overall.csv to english based on Google Translate API"

1.1.0 - 2020-02-01 - "break down area into simple scv file"


