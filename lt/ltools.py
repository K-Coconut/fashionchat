#coding=utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
import json

import resource

def add_dict():
    for  f in os.listdir('F:\python_project\AI\slot'):
        with open('F:\python_project\AI\slot\\'+f) as fr:
            for line in fr:
                sps = line.decode("utf-8").strip().replace(" ", "").lower().split("\t")
                for i in sps:
                    resource.jieba.add_word(i.strip())


def forprint(_d):
    return json.dumps(_d,encoding='utf-8',ensure_ascii=False)

class LTool(object):
    def __init__(self, config):
        pass

    # cut_list: [["耐克", "nike", ["Brand"]], ["aj1", "airjordan1", ["Series"]], ["画报", "画报", []], ["网上", "网上", []], ["发售", "发售", []], ["有", "有", []], ["说法", "说法", []], ["了", "了", []], ["吗", "吗", []]]
    def get_norm_query(self, cut_list):
        # to-do:按字典名获取norm query
        # 获取将槽点转换成标准名后的问题
        return "".join(_i[1] for _i in cut_list)
    #
    # def get_norm_query(self, cut_list,query):
    #     for _i in cut_list:
    #         query = query.replace(_i[0],_i[1])
    #     return query

    def get_query_slot(self, cut_list):
        slot_dict = {}
        for word, norm_word, slot_list in cut_list:
            for slot_name in slot_list:
                slot_dict[slot_name] = norm_word
        return slot_dict


    #合并分词结果(取最长合并)
    def cut(self, query):
        res = []
        qu = query.decode("utf-8").strip().replace(" ", "").lower()
        cutter = resource.jieba
        l = list(cutter.cut(qu.strip()))
        for i in range(len(l)):
            n, d = resource.em.find(l[i])
            if d:
                c = i + 1
                while True:
                    if c > len(l):
                        break
                    word = ''.join(l[i:c + 1])
                    n1, d1 = resource.em.find(word)
                    if d1:
                        n, d = n1, d1
                        c += 1
                        continue
                    else:
                        break
                res.append((l[i],n, d))
        return res

    def cut1(self, query):
        cutter = resource.jieba
        cut_list = []
        _list = list(cutter.cut(query.strip()))
        for word in _list:
            normal_word, dict_names = resource.em.find(word)
            cut_list.append((word, normal_word, dict_names))

        print 'cut_list:',forprint(cut_list)
        return cut_list

if __name__=='__main__':
    t=LTool(None)
    while True:
        query = raw_input('问题:')
        print t.cut(query)