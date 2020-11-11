import requests
import lxml
from bs4 import BeautifulSoup
import os
import json
import redis
import re
import mysql_database
import time


headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=9FF25DAD968672044753E457B1BB7EBA:FG=1; PSTM=1553586136; BIDUPSID=40AF2BCF0D6E88186C2F1F1E4396503D; BD_UPN=12314753; __cfduid=d7e6ff274ecb0649ad79e3fa6a26182df1556097198; MCITY=-%3A; H_WISE_SIDS=130611_126893_132920_130510_133471_120219_131601_133016_132909_133046_131247_132440_130763_132378_131517_118890_118873_118840_118826_118791_107316_133158_132781_130120_122034_133116_133352_129649_132250_124635_132540_133837_133473_131905_128892_133847_132552_133838_133386_129645_131423_110085_131115_134152_127969_123290_131753_131299_132283_127416_134150_132696; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sugstore=0; BDUSS=ls5po06gtsfks28q0kiu5dl6t0; ispeed_lsm=2; delPer=0; BD_HOME=0; BD_CK_SAM=1; PSINO=1; BDRCVFR[gUg2cUtcsBT]=_M5urk4djP3fA4-ILn; shifen[127711678134_87058]=1565319725; shifen[59009451547_5254]=1565319727; shifen[92869477230_20486]=1565319729; COOKIE_SESSION=54778_12_9_9_26_36_0_0_5_8_27_0_0_62276_51_18_1565264995_1565319704_1565319722%7C9%2362299_25_1565319722%7C9; shifen[71016554660_38932]=1565319731; BCLID=9967430828201805355; BDSFRCVID=oP4OJeC62ZZSF_3wEy4pMCC4pL-8kQ5TH6aoL9kcxcv5tqbl4pwnEG0PDf8g0Ku-KDxeogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tbAf_KthJDvbfP0kKb5_-Jtt-eT22-us266l2hcH0KLKftPG04T-5ntOKfru3MtJ-nr3VR5LJMb1MRjv5-bsXp8uyMJpKU5eBb-q2h5TtUJMeCnTDMRhqJ_lDU7yKMnitIj9-pnKHlQrh459XP68bTkA5bjZKxtq3mkjbIOFfD_hhDtlD58aen-W5gTfaRJ--jAX3b7EHJO_bnvxBUnkbfJBD4QWtRO2J6v4XC-5BlOTM-t4jfj-ejL7yajK2-_DKCnzKUIhB-o6jf7JLPcpQT8ry-FOK5OibCuLKMQXab3vOIJzXpO15CuzBN5thURB2DkO-4bCWJ5TMl5jDh05y6TLeHufJjDHtR38Q6rs2RrOjttk-PI3KJD3XP6-35KH0mFjbtJ8bh5BMMcELU-MK5jXDn-f2q37JD6y_5CXLhrVVh-RDqQEWRKSy4oxJpODBRbMopvaKtj4OCovbURvD-ug3-7qex5dtjTO2bc_5KnlfMQ_bf--QfbQ0abZqjDOJRAj_IIQ2brofnRNKnr5q4tHeUjv3xRZ5mAqoJT82IbTM43H2jO_Xftdjh0HJjJgJKonaIQqaKoasU3hWqPByPFRyR3uth343bRTBqCy5KJvfj6FWloYhP-UyN3LWh37btjlMKoaMp78jR093JO4y4Ldj4oxJp8eWJLfoIIbJI_abP365ITM2J8yheT22-usaa4J2hcH0KLKoxcbQlP55UL-jh3u3MtJ-gtLVnvlJxb1MRjvX5rO-nkS5GoJb4jQJTRfWq5TtUJUeCnTDMRhqfPv2MoyKMnitIj9-pnKHlQrh459XP68bTkA5bjZKxtq3mkjbIOFfJOKHIC4D6_WjxK; Hm_lvt_9f14aaa038bbba8b12ec2a4a3e51d254=1565320771; Hm_lpvt_9f14aaa038bbba8b12ec2a4a3e51d254=1565320771; H_PS_645EC=2ad7oTX%2B7gW1SjkXFy5uaioAU6CbyVgRv5ZoORS2vL6pcGjbgf%2B0KZ3SJKo; BDRCVFR[C0p6oIjvx-c]=rJZwba6_rOCfAF9pywd; H_PS_PSSID=; BDSVRTM=100',
    'Host': 'www.baidu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E6%9D%A8%E7%B4%AB',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

}


def geta_sigurl_infomation(url):
    #url='https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=杨紫&medium=0&x_bfe_rqs=03E80&tngroupname=organic_news&rsv_dl=news_b_pn&pn=10'
    text=requests.get(url,headers=headers)
    soup=BeautifulSoup(text.text,'lxml')
    html_key_divs=soup.find_all(attrs={"class": "result"})

    for html_key_div in html_key_divs:
        id=html_key_div['id']
        title=html_key_div.find_all('a')[0].get_text()
        href=html_key_div.find_all('a')[0]['href']
        medium=html_key_div.find_all('p')[0].get_text().replace('\n','').replace('\t','').replace(' ','')
        medium_get=medium.split('\xa0')[0]
        time_get=medium.split('\xa0')[-1]
        detail=html_key_div.select('div>div')[-1].get_text().replace('\n','').replace('\t','').replace('百度快照','').split(' ')
        detail_get=[x for x in detail if x!=''][-1]
        sql_insert = str(
            "INSERT INTO stars(id,title,href,medium_get,time_get,detail_get) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')").format(
            id, title, href, medium_get, time_get, detail_get).replace('\n', '').replace('\t', '')

        mysql_database.table_data_insert(databasename='spider',sql=sql_insert)

        time.sleep(1)






