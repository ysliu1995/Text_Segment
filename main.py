# -*- coding: UTF-8 -*-
import json
import pandas as pd

class TextSegment:

    def __init__(self):
        self.word_dict = {}
        self.ans = []

    def GenDict(self):

        df_1 = pd.read_excel('dict_revised_2015_20160523_1.xls')
        df_2 = pd.read_excel('dict_revised_2015_20160523_2.xls')
        df_3 = pd.read_excel('dict_revised_2015_20160523_3.xls')

        a =  list(df_1['字詞名'].values)
        b =  list(df_2['字詞名'].values)
        c =  list(df_3['字詞名'].values)
        d = a + b + c

        self.word_dict = {}
        for i in d:
            self.word_dict[i] = 1

        dict_file = json.dumps(self.word_dict)

        file = open('word.json', 'w')
        file.write(dict_file)
        file.close()

    def LoadDict(self):

        with open("word.json",'r') as load_f:
            self.word_dict = json.load(load_f)

    def check(self, t):
        # print(t)
        try:
            if self.word_dict[t] == 1:
                # print('find')
                self.ans.append(t)
                return True
        except:
            if len(t) == 1:
                self.ans.append(t)
                return True
            else:
                # print('Not find')
                return False

    def segment(self, t):
        for i in range(len(t)):
            if self.check(t[i:]):
                self.segment(t[:i])
                break

    def main(self):

        txt = '這個布丁是在無聊的世界中找尋樂趣的一種不能吃的食物'

        # self.GenDict()
        self.LoadDict()
        self.segment(txt)

        print(self.ans[::-1])


if __name__ == '__main__':

    s = TextSegment()
    s.main()
    