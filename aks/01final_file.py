import urllib2
from bs4 import BeautifulSoup

import csv
import json
import time
import re
import sys

url_head='https://www.myntra.com/'
user_agent = 'Mozilla/5.0'
#'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
thefile = open('test_prod_desc.csv', 'w')
wr = csv.writer(thefile, quoting=csv.QUOTE_ALL)
f=open('all_styles_aks.csv') ## all brand names
z=csv.reader(f,delimiter=',')
for rows in z:
    # print rows[1]
    i=0
    try:
        to_csv=[]
        url=url_head+rows[1]
        # print url
        req=urllib2.Request(url,None,headers)
        response=urllib2.urlopen(req)
        page=response.read()
        soup=BeautifulSoup(page)
        z=soup('script')[6]
        str1=str(z).replace('<script>window.__myx = ','')
        str2=str1.replace('</script>','')
        input_json =json.loads(str2)
        prd_desc=re.sub("<.*?>", "", input_json['pdpData']['descriptors'][0]['description'])
        to_csv.append(rows[1])
        to_csv.append(prd_desc)
        if input_json['pdpData']['descriptors'][2]['title']=='materials_care_desc':
            mat_desc=input_json['pdpData']['descriptors'][2]['description']
        else:
            mat_desc=input_json['pdpData']['descriptors'][3]['description']

        material_desc=re.sub("<.*?>", "", mat_desc)
        material_desc=re.sub("[^\x00-\x7f]"," ",material_desc)
        to_csv.append(material_desc)
        # print to_csv
        wr.writerow(to_csv)
    except :
         to_csv.append(rows[1])
         to_csv.append('NA')
         print url_head+rows[1]
    time.sleep(5)
    sys.stdout.write("-")
    sys.stdout.flush()
