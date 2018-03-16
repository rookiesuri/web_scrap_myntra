## reading json from a textfile
file = open('testfile.txt','r')
import json

outfile=json.load(file)

# print type(outfile)
z=0
json2 =outfile['searchData']
# print type(json2)
# for k,v in json2.items():
#     print k
json3=json2['results']
# for k,v in json3.items():
#     print k
z=json3['totalProductsCount']
json4=json3['filters']
# print type(json4)
print z
# print type(json4[6]) ### price range filters
# for k,v in json4[6].items():
#     print k
json5 = json4[6]['values']
print type(json5)
for k,v in json5.items():
    print k
json6 = json4[6]['values']['breakUps'] #not using json5
print json6[1]['occurrence']
########setting one single json######
