## all def files

def json_parser(input_json,brand_name):
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
