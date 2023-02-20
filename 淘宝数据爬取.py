import requests
import re
import json
import csv

with open('tb.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['raw_title','pic_url','detail_url','view_price','item_loc','view_sales','nick','shopName'])
headers ={
    'cookie':'',
    'referer' : 'https://s.taobao.com/',
    'user-agent':''
          }#输入头寸信息
for i in range(1,11): #爬取前10页
    print('正在爬取第',i,'页')
    url='https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180207&ie=utf8&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s={}'.format('关键词'，i)
    reponse = requests.get(url=url,headers=headers)
    html_data = reponse.text
    json_str = re.findall('g_page_config =(.*);',html_data)[0]
    json_dict = json.loads(json_str)
    auctions=json_dict['mods']['itemlist']['data']['auctions']
    for auction in auctions:
        try:
            raw_title= auction['raw_title']
            pic_url= auction['pic_url']
            detail_url= auction['detail_url']
            view_price= auction['view_price']
            item_loc= auction['item_loc']
            view_sales= auction['view_sales']
            nick= auction['nick']
            shopName = auction['shopName']
            with open('tb.csv',mode='a',encoding='utf-8',newline='') as f:
                csv_writer=csv.writer(f)
                csv_writer.writerow([raw_title,pic_url,detail_url,view_price,item_loc,view_sales,nick,shopName])
        except:
            pass
