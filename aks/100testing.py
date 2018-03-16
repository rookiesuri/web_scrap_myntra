# input="""<div class="pdp-productDescriptors"><input type="checkbox" class="pdp-inputProductDetails" id="productDetails" value="productDescriptors"><label class="pdp-inputProductDetailsLabel" for="productDetails"><!-- react-text: 168 -->Product Details<!-- /react-text --><span class="pdp-expandProductDetails"></span></label><div class="pdp-productDescriptorsContainer"><div><h4 class="pdp-product-description-title">Product Details</h4><p class="pdp-product-description-content">Navy <a href="/solid?src=pd" class="seolink">solid</a> straight <a href="/kurta?src=pd" class="seolink">kurta</a>, has a round neck, <a href="/short?src=pd" class="seolink">short</a> sleeves, curved hem</p></div><div class="pdp-sizeFitDesc"><h4 class="pdp-completeTheLook pdp-product-description-title">Complete The Look</h4><p class="pdp-style-note">This breathable and stylish kurta from Libas is a must-have item for any wardrobe. For your next dinner party or family gathering, this navy piece pairs well with dark leggings and chic flats.</p></div><div class="pdp-sizeFitDesc"><h4 class="pdp-sizeFitDescTitle pdp-product-description-title">Size &amp; Fit</h4><p class="pdp-sizeFitDescContent pdp-product-description-content">The model (height 5'7") is wearing a size S</p></div><div><h4 class="pdp-product-description-title">Material &amp; Care</h4><p class="pdp-product-description-content">Polyester crepe <br>Hand-wash</p></div></div></div>"""
# from bs4 import BeautifulSoup
# z=BeautifulSoup(input)
# print type(z)
#
# print str(z.find("p").get_text())
# print z('p')[2]
# import csv
# f=open('all_styles_aks.csv') ## all brand names
# z=csv.reader(f,delimiter=',')
# for rows in z:
#     print rows[1]
# import urllib2
# from bs4 import BeautifulSoup
# url='https://www.myntra.com/kurtas/libas/libas-women-navy-solid-straight-kurta/1817314/buy'
# user_agent = 'Mozilla/5.0'
# #'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
# headers = { 'User-Agent' : user_agent }
#
# req=urllib2.Request(url,None,headers)
# response=urllib2.urlopen(req)
# page=response.read()
# soup=BeautifulSoup(page)
# z=soup('script')[6]
# str1=str(z).replace('<script>window.__myx = ','')
# str2=str1.replace('</script>','')
# import json
# input_json =json.loads(str2)
# print (input_json['pdpData']['descriptors'][0]['description'])## gets the product title
# print (input_json['pdpData']['descriptors'][2]['description'])
# import re
# notag = re.sub("<.*?>", " ", input_json['pdpData']['descriptors'][0]['description']) ## removing tags
# print notag
#
# import csv
# t=open('test_csv_writer.csv','w')
# wr=csv.writer(t)
# for x in range(1,4):
#     y = xrange(x)
#     wr.writerow(y)

##optimizing json
# import json
# import csv
# f=open('json_test2.json')
# json_input=json.loads(f.read())
# if json_input['pdpData']['descriptors'][3]['title']=='materials_care_desc':
#     z=json_input['pdpData']['descriptors'][3]['description']
# else:
#     z=json_input['pdpData']['descriptors'][2]['description']
# print z
###################################
#####unicode####################
# s='Cotton Machine-wash'
# print s
# import re
# z=re.sub("<.*?>", "", s)
# y=re.sub("[^\x00-\x7f]"," ",z)
# print y
############################################

###############
#####toolbar
import time
import sys

toolbar_width = 400

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    # print i
    sys.stdout.flush()

sys.stdout.write("\n")
