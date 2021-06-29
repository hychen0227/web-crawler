import requests
import random
import time
for i in range(88,111):
 date = '{a}/1/1-{a}/12/31'.format(a=i)
 payload={
 'tmpQuerySentence':'',
 'timeRange':(date),
 'querySentence':'淡水紅毛城 or 鹿港龍山寺 or 台南孔子廟',
 'tenderStatusType':'決標',
 'sortCol':' AWARD_NOTICE_DATE',
 'timeRangeTemp':(date),
 'sym':'on',
 'itemPerPage':'50000'
 } #Form Data
 headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
 print(date)
 res = requests.post("https://web.pcc.gov.tw/prkms/prms-searchBulletionClient.do?root=tps", data=payload)
 f = open('raw.txt','a',encoding='utf-8')
 f.write (res.text)
 print('complete')
 delay_choices = [2, 4, 6, 8]  #延遲的秒數
 delay = random.choice(delay_choices)  #隨機選取秒數
 delaytime = 'delay time {b}s ...'.format(b=delay)
 print(delaytime)
 time.sleep(delay)  #延遲
 f.close()
######
#grep -C6 '國定古蹟' raw.txt | grep -E '國定古蹟|無法決標' > 國定古蹟.txt


