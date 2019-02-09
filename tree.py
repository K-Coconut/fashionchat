#coding=utf-8
from lt.ltools import LTool

class Tree(object):
    def __init__(self, config):
        self.ltool = LTool(config) 
        self.__load(config)

    def __load(self, config):
        self.__dict = self.__load_raw_file(config)
        self._node_slot_dict = self.__post_load(self.__dict, config)
    
    def _get_level_dict(self, node_set):
        level_dict = {}

        for node in node_set:
            sps = node.split("/")
            level = 0
            for i in range(len(sps), 0, -1):
                _t_node = "/".join(sps[:i])
                if _t_node in level_dict:
                    _t_level = level_dict[_t_node]
                    if _t_level > level:
                        level = _t_level
                level_dict[_t_node] = level
                level += 1
        self.level_dict = level_dict
                         
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
        t_dict = {}
        for key in __dict:
            value = __dict[key]
            cut_list = ltool.cut(key)
            norm_query = ltool.get_norm_query(cut_list)
            _slot_dict  = ltool.get_query_slot(cut_list)
            self.__post_load_needed_slot(value, _slot_dict, _node_slot_dict)
            t_dict[norm_query] = value  
        __dict.update(t_dict)
        return _node_slot_dict
        
    def __load_raw_file(self, config):
        file_name = config["_conf_file_name"]
        __dict = {}
        node_set = set()
        key_col = 0
        value_col = 1
        if "_conf_key_col" in config and "_conf_value_col" in config:
            key_col =  config["_conf_key_col"] 
            value_col = config["_conf_value_col"]
        with open(file_name) as fr:
            for line in fr:
                sp = line.decode("utf-8").strip().split("\t")
                key = sp[key_col].replace(" ", "").lower()
                value = sp[value_col]
                __dict[key] = value
                node_set.add(value)
        self._get_level_dict(node_set)
        return __dict

    
    def get_node(self, query):
	query = query.replace(" ", "").lower()
        ltool = self.ltool 
        node = None
        if query in self.__dict:
            node =  self.__dict[query]
        else:
            cut_list = ltool.cut(query)
            norm_query = ltool.get_norm_query(cut_list)

            if norm_query in self.__dict:
                node = self.__dict[norm_query]
        return node
    
     
    def get_node_need_slot(self, node):
        if node in self._node_slot_dict:        
            return self._node_slot_dict[node]   
        return []


    def get_node_level(self, node):
        if node in self.level_dict:
            return self.level_dict[node]

    def get_final_node(self, candidates):
        level_dict = {} 
        for candi in candidates:
            node_list = candidates[candi]["node"] 
            score = candidates[candi]["score"]
            if score > 0.99:
                return node_list[-1]
            if score < 0.55:
                continue
            for node in node_list:
                level = self.get_node_level(node)
                if level not in level_dict:
                    level_dict[level] = {}
                if node not in level_dict[level]:
                    level_dict[level][node] = []

                level_dict[level][node].append((candi, score))

        for level in range(0, 100):
            if level in level_dict: 
                for node in level_dict[level]:
                    score = 0.0
                    for item in level_dict[level][node]:
                        score += item[1] 
                    if score > 1.5:
                        return node
