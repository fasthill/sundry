import pandas as pd
import ast
import wget
import re

# url = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/bitly_usagov/example.txt'
# data = wget.download(url)

with open("example.txt", 'r', encoding='utf-8') as f:
    data = f.readlines()

def convert_to_new_string(old_string):
    pattern =  re.compile(':.*?".*?(").*?(").*?"\s*,')  # find location issued errors while converting to df
    match = re.search(pattern, old_string)
    sq = "'"
    first_location = match.start(1)
    second_location = match.start(2)
    new_string = old_string[:first_location] \
                 + sq + old_string[first_location+1:second_location] \
                 + sq + old_string[second_location+1:]
    return new_string

fw = open("failed_data.txt", 'w')  # for the data set with double quotation mark, fix later on!

df = pd.DataFrame()
for dic_string in data:
    dic_string = dic_string.replace('null', '"NULL"')  # induce error where there is null as values
    dic_string = dic_string.replace('\/', '/')  # delete "\" in front of "/".
    dic_string = re.sub(r'[\[\]]', '"', dic_string)  # change list format to string format. cause it duplicates lines as many as len of list
    try:
        dic = ast.literal_eval(dic_string)
    except:
        dic_string = convert_to_new_string(dic_string)
        try:
            dic = ast.literal_eval(dic_string)
        except:
            fw.write(dic_string)
            pass
        pass

    df = pd.concat([df, pd.DataFrame(dic, index=[0])], ignore_index=True)  # index=[0], make index for string only

fw.close()
df.to_csv('example.csv', index=False)