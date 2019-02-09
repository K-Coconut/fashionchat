#coding=utf-8
import resource

class LTool(object):
    def __init__(self, config):
        pass
            
    def get_norm_query(self, cut_list):
        return "".join(_i[1] for _i in cut_list)


    def get_query_slot(self, cut_list):
        slot_dict = {}
        for word, norm_word, slot_list in cut_list:
            for slot_name in slot_list:
                slot_dict[slot_name] = norm_word
        return slot_dict


    def cut(self, query):        
        cutter = resource.jieba 
        cut_list = []
        _list = list(cutter.cut(query.strip()))
        for word in _list: 
            normal_word, dict_names = resource.em.find(word)
            cut_list.append((word, normal_word, dict_names)) 
        return cut_list


