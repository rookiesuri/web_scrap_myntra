#parsing nested json

file = open('testfile.txt','r')
import json

outfile=json.load(file)

print type(outfile['searchData']['results']['filters'][6]['values']['breakUps'])
total_levels=len(outfile['searchData']['results']['filters'][6]['values']['breakUps'])
#after filters dict---->list
#after 6 list-- > dict
##after breakups dict--->list
z=[]
for i in range(0,total_levels):
    low_limit= outfile['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMin']
    high_limit=outfile['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMax']
    total_styles=outfile['searchData']['results']['filters'][6]['values']['breakUps'][i]['occurrence']
    z.append([low_limit,high_limit,total_styles])
print z

thefile = open('test.csv', 'w')
for item in z:
    thefile.write("%s\n" % item)
    thefile.close
# test='anouk'
# def json_parser(input_json,test):
#     total_levels=len(input_json['searchData']['results']['filters'][6]['values']['breakUps'])
#     z=[]
#     for i in range(0,total_levels):
#
#             z1=[]
#             z1.append(test)
#             z1.append(i)
#             z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMin'])
#             z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['rangeMax'])
#             z1.append(input_json['searchData']['results']['filters'][6]['values']['breakUps'][i]['occurrence'])
#             z.append(z1)
#     return z
# print json_parser(outfile,test)
