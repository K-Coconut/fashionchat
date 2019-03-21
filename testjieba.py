# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import jieba

from lt.ltools import *
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
from resource import em

jieba.load_userdict('cut_dict')

def cut(query,mode='cut',**kwargs):
    if mode == 'cut':
        seg_list = jieba.cut(query, cut_all=kwargs['flag'])
        print json.dumps(list(seg_list),encoding='utf-8',ensure_ascii=False)
        print(", ".join(seg_list))
    elif mode == 'search':
        seg_list = jieba.cut_for_search(query)  # 搜索引擎模式

        print(", ".join(seg_list))

query = '你知道耐克中国官网发耐克AJ1画报吗'

# while True:
#     query = raw_input('问题:')
#     cut(query,mdoe='cut',flag=False)
#

def te(qu='国区会不会发耐克AJ1画报啊'):
    s = []
    t = LTool(None)
    qu = qu.decode("utf-8").strip().replace(" ", "").lower()
    cutter = resource.jieba
    cut_list = []
    l = list(cutter.cut(qu.strip()))
    for i in range(len(l)):
        n, d = em.find(l[i])
        if d:
            print '首:', n, d
            c = i + 1
            while True:
                if c > len(l):
                    break
                word = ''.join(l[i:c + 1])
                print 'word:', word
                n1, d1 = em.find(word)
                if d1:
                    print c - i, '轮', n1, d1
                    n,d=n1,d1
                    c += 1
                    continue
                else:
                    break
            s.append((n,d))
    print s

with open('F:\python_project\AI\slot\ShoeDict.txt') as fr:
    for line in fr:
        sps = line.decode("utf-8").strip().replace(" ", "").lower().split("\t")
        for i in sps:
            jieba.add_word(i.strip())

