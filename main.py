# -*- coding: UTF-8 -*-
import pandas as pd

df_1 = pd.read_excel('dict_revised_2015_20160523_1.xls')
df_2 = pd.read_excel('dict_revised_2015_20160523_2.xls')
df_3 = pd.read_excel('dict_revised_2015_20160523_3.xls')

a =  list(df_1['字詞名'].values)
b =  list(df_2['字詞名'].values)
c =  list(df_3['字詞名'].values)
d = a + b + c

word_dict = {}
for i in d:
    word_dict[i] = 1


ans = []

def check(t):
    print(t)
    try:
        if word_dict[t] == 1:
            print('find')
            ans.append(t)
            return True
    except:
        if len(t) == 1:
            ans.append(t)
            return True
        else:
            print('Not find')
            return False

def segment(t):
    for i in range(len(t)):
        if check(t[i:]):
            segment(t[:i])
            break


txt = '這個布丁是在無聊的世界中找尋樂趣的一種不能吃的食物'
segment(txt)

print(ans[::-1])
