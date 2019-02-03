#coding=utf-8
from lt.ltools import LTool

class Tree(object):
    def __init__(self, config):
        self.ltool = LTool(config) 
        self.__load(self, config)

    def __load(self, config):
        self.__dict = self.__load_raw_file(self, config)
        self._node_slot_dict = self.__post_load(self, self.__dict, config)

        
    def __post_load_needed_slot(self, node, _slot_dict, _node_slot_dict):
        if node in _node_slot_dict:
            _t_list = _node_slot_dict[node]
            if len(_slot_dict.keys()) < len(_t_list):
                _node_slot_dict[node] = _slot_dict.keys()    
        else:
            _node_slot_dict[node] = _slot_dict.keys()


    def __post_load(self, __dict, config):
        ltool = self.ltool 
        _node_slot_dict = {}  
        for key in __dict:
            value = __dict[key]
            cut_list = ltool.cut(key)
            norm_query = ltool.get_norm_query(cut_list)
            _slot_dict  = ltool.get_query_slot(cut_list)
            self.__post_load_needed_slot(self, value, cut_list, _node_slot_dict):
            __dict[norm_query] = value  
        return _node_slot_dict
        
    def __load_raw_file(self, config):
        file_name = config["_conf_file_name"]
        __dict = {}
        key_col = 0
        value_col = 1
        if "_conf_key_col" in config and "_conf_value_col" in config:
            key_col =  config["_conf_key_col"] 
            value_col = config["_conf_value_col"]
        with open(file_name) as fr:
            for line in fr:
                sp = line.decode("utf-8").strip().split("\t")
                key = sp[key_col]
                value = sp[value_col]
                __dict[key] = value
        return __dict

    

    def get_node(self, query):
        ltool = self.ltool 
        node = None
        if query in self.__dict:
            node =  self.__dict[query]
        else:
            cut_list = ltool.cut(query)
            norm_query = ltool.get_norm_query(cut_list)

            if norm_query in self.__dict:
                node = self.__dict[norm_query]

        
    

