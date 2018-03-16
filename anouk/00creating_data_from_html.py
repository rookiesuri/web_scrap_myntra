from bs4 import BeautifulSoup
input_html="C:\\Users\\soori\\work\\00.web_scrap\\anouk\\anouk_all_products.html"
filename= open(input_html,'r')
soup= BeautifulSoup(filename,"html5lib")
import re
print type(soup)
i=0


####product short title#######
# y= soup('li')[65]
#
# print y.prettify()
# print type(str(y.find("div",{"class":"product-brand"}).string)) # brand
# print type(str(y.find('a')['href']))
# print type(y.find('h4').string)
# try:
#     print y.find("span",{"class":"product-discountedPrice"}).contents[4] #discountedPrice
#     print y.find("span",{"class":"product-strike"}).contents[4]
# except:
#     z= y.find("div",{"class":"product-price"}).contents[0]
#     abc= re.sub("<.*?>", "",str(z) )
#     print abc.replace('Rs. ',"")

#####################
# def write_txt(file_to_write,list_input):
#     for item in file_to_write:
#         file_to_write.write("%s\n" % item)
import csv
thefile = open('input_links.csv', 'w')
i=0
for y in soup.find_all('li'):
    z=[]
    z.append(str(y.find("div",{"class":"product-brand"}).string))
    z.append(str((y.find('a')['href'])))
    z.append(y.find('h4').string)
    try:
        z.append(y.find("span",{"class":"product-discountedPrice"}).contents[4])
        z.append(y.find("span",{"class":"product-strike"}).contents[4])
    except:
        sub_price=y.find("div",{"class":"product-price"}).contents[0]
        sub_price=re.sub("<.*?>", "",str(sub_price))
        z.append(sub_price.replace("Rs. ",""))
    i=i+1
    wr = csv.writer(thefile, quoting=csv.QUOTE_ALL)
    wr.writerow(z)

print i
