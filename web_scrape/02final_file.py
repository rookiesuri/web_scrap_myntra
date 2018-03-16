import urllib2
user_agent = 'Mozilla/5.0'
#'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

def json_parser(input_json,brand_name):
    import json
    total_levels=len(input_json['searchData']['results']['filters'][6]['values']['breakUps'])
    z=[]
    for i in range(0,total_levels):

            z1=[]
            z1.append(test)
            z1.append(i)
            z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMin'])
            z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMax'])
            z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['occurrence'])
            z.append(z1)
    return z

def write_txt(file_to_write,list_input):
    for item in file_to_write:
        file_to_write.write("%s\n" % item)


url_pattern1="https://www.myntra.com/women-kurtas-kurtis-suits?f=brand%3A"

##getting input from csv
import csv
f=open('input_list_kurtas.csv') ## all brand names
z=csv.reader(f,delimiter=',')
list_input=[]

for rows in z:
    list_input.append(rows) ## creating a list with brands
# req = urllib2.Request('https://www.myntra.com/women-kurtas-kurtis-suits?f=brand%3AAnouk%3A%3Acategories%3AKurtas', None, headers)
# response = urllib2.urlopen(req)
# page = response.read()
thefile = open('test.csv', 'w')
import time
import json
from bs4 import BeautifulSoup
for x in list_input:
    url_pattern1="https://www.myntra.com/women-kurtas-kurtis-suits?f=brand%3A"+str(x[0])+"%3A%3Acategories%3AKurtas"
    print url_pattern1
    test=str(x[0])
    #print url_pattern1
    req=urllib2.Request(url_pattern1,None,headers)
    response=urllib2.urlopen(req)
    page=response.read()
    soup=BeautifulSoup(page)
    z=soup.findAll('script')
    str1=str(z[8]).replace('<script>window.__myx = ','')
    str2=str1.replace('</script>','')
    input_json_created=json.loads(str2)
    input_list=json_parser(input_json_created,x)
    print input_list ## input to external file

    for item in input_list:
        thefile.write("%s\n" % item)
        print 'write complete'
    time.sleep(60)
