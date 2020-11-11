
import mysql_database
import sigle_url_spider
import time

def urls_get(keyword,num=600):
    url_frist='https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=4&bsst=1&rsv_dl=news_t_sk&tn=news&word={}'.format(keyword)
    urls=[]
    urls.insert(0,url_frist)
    for i in range(1,num):
        num = 10 * i
        url_list = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={}&medium=0&x_bfe_rqs=03E80&'.format(keyword)\
                + 'tngroupname=organic_news&rsv_dl=news_b_pn&pn={}'.format(num)
        urls.append(url_list)
        #print(url_list)
    return urls


if __name__ == '__main__':
    sql_creat = 'CREATE TABLE IF NOT EXISTS songguo(id VARCHAR(625) NOT null,title VARCHAR(625) NOT null,href VARCHAR(625) NOT null, medium_get VARCHAR(625),time_get VARCHAR(625) not null ,detail_get VARCHAR(825) not null)'

    mysql_database.database_creat(databasename='songguo')
    mysql_database.table_creat(databasename='songguo',sql=sql_creat)
    for url in urls_get(keyword='松果出行'):
        sigle_url_spider.geta_sigurl_infomation(url)

