from fuzzywuzzy import fuzz
import json

f = open("test", "r")
a = json.loads(f.read())
b = []
for i in a:
    Ratio = fuzz.ratio(i['str1'].lower(),i['str2'].lower())
    Partial_Ratio = fuzz.partial_ratio(i['str1'].lower(),i['str2'].lower())
    Token_Sort_Ratio = fuzz.token_sort_ratio(i['str1'],i['str2'])
    Token_Set_Ratio = fuzz.token_set_ratio(i['str1'],i['str2'])
    i['Ratio']= Ratio
    i['Partial_Ratio']= Partial_Ratio
    i['Token_Sort_Ratio']= Token_Sort_Ratio
    i['Token_Set_Ratio']= Token_Set_Ratio
    # if i['Token_Set_Ratio'] == 100 and i['Ratio'] != 100 and i['Partial_Ratio'] != 100 and i['Token_Sort_Ratio'] != 100:
    #     print(i)
    if i['Token_Set_Ratio']!=100:
        print(i)
    b.append(i)

"""
Sample file: test in same directory
[{"str1":"MADERIA, GLORIA A.", "str2":"MADERIA, GLORIA","result":""},
{"str1":"CROCE, ROBERT A.", "str2":"CROCE, ROBERT","result":""}]
"""
