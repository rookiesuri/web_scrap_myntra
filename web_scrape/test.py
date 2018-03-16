import urllib2
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

req = urllib2.Request('https://www.myntra.com/women-kurtas-kurtis-suits?f=brand%3AAnouk%3A%3Acategories%3AKurtas', None, headers)
response = urllib2.urlopen(req)
page = response.read()
# x=open('testfile.txt','w')
# x.write(page)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
print type(soup)

# window.__myx
import json
z=soup.findAll('script')
#print z[7]
# x=open('testfile.txt','w')
# x.write(str(z[8]))
str1=str(z[8]).replace('<script>window.__myx = ','')
str2=str1.replace('</script>','')
# x=open('testfile.txt','w')
# x.write(str2)
dit=json.loads(str2)
print type(dit)
