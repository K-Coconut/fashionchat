#coding=utf-8
import json
import resource

from lt.ltools import LTool
from retriver.retriver_manager import RetriverManager


def forprint(_d):
    return json.dumps(_d,encoding='utf-8',ensure_ascii=False)


class Tree(object):
    def __init__(self, config):
        self.ltool = LTool(config)
        self.__load(config)

    def __load(self, config):
        self.__dict = self.__load_raw_file(config)
        self._node_slot_dict = self.__post_load(self.__dict, config)
        # print forprint(self._node_slot_dict)

    # 构建树的层级,问题:层级数,取最大
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

    # 提出节点需要的槽位
    def __post_load_needed_slot(self, node, _slot_dict, _node_slot_dict):
        # 若_node_slot_dict已经存在node的槽位列表,取最短的;目的是获取某个节点至少需要的槽位
        if node in _node_slot_dict:
            _t_list = _node_slot_dict[node]
            if len(_slot_dict.keys()) < len(_t_list):
                _node_slot_dict[node] = _slot_dict.keys()

        # 若不存在则直接取当下槽位
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
            # print 'key:',key
            # print 'value',value
            # print 'cut_list:',forprint(cut_list)
            # print 'norm_query:',forprint(norm_query)
            # print '_slot_dict:',forprint(_slot_dict)

            # key:问题,value:节点,_slot_dict:节点对应的槽位
            self.__post_load_needed_slot(value, _slot_dict, _node_slot_dict)
            t_dict[norm_query] = value

        # 将__t增加到__dict中
        __dict.update(t_dict)
        # print 't_dict:',forprint(t_dict)
        # print '__dict:',forprint(__dict)
        return _node_slot_dict

    def __load_raw_file(self, config):
        file_name = config["_conf_file_name"]
        __dict = {}
        node_set = set()

        # 默认0列为问题,1列为节点
        key_col = 0
        value_col = 1

        # 若配置文件中指定问题的列及节点的列
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
        # print 'node_set',forprint(list(node_set))
        # print '__dict:',forprint(__dict)
        # print 'level_dict:',forprint(self.level_dict)
        return __dict


    def get_node(self, query):
        query = query.replace(" ", "").lower()
        ltool = self.ltool
        node = None
        # print json.dumps(self.__dict,encoding='utf-8')
        if query in self.__dict:
            node =  self.__dict[query]
        else:
            cut_list = ltool.cut(query)
            print 'cut_list:',forprint(cut_list)
            norm_query = ltool.get_norm_query(cut_list)
            print 'norm_query:',norm_query.encode('utf-8')

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
            # 若分数高于0.99,直接返回最长的节点
            if score > 0.99:
                return node_list[-1]
            # 若分数低于0.55,跳过
            if score < 0.55:
                continue
            for node in node_list:
                level = self.get_node_level(node)
                if level not in level_dict:
                    level_dict[level] = {}
                if node not in level_dict[level]:
                    level_dict[level][node] = []
                level_dict[level][node].append((candi, score))
        print 'level_dict:',forprint(level_dict)

        # 将level_dict中的所有层级的节点的分数计算总和,若当前节点的分数超过1.5则直接返回
        for level in range(0, 100):
            if level in level_dict:
                for node in level_dict[level]:
                    score = 0.0
                    for item in level_dict[level][node]:
                        score += item[1]
                    if score > 1.5:
                        return node

if __name__=="__main__":
    tree_config = resource.tree_config
    tree = Tree(tree_config)
    candidates = {u'\u8010\u514bAJ1\u753b\u62a5SNKRS\u53d1\u5417': {'node': [u'\u53d1\u552e', u'\u53d1\u552e/\u6e20\u9053', u'\u53d1\u552e/\u6e20\u9053/\u7ebf\u4e0a', u'\u53d1\u552e/\u6e20\u9053/\u7ebf\u4e0a/\u5b98\u65b9\u7ebf\u4e0a'], 'score': 0.5152326226234436}, u'SNKRS\u6709\u6ca1\u6709\u8010\u514bAJ1\u753b\u62a5\u8fd9\u978b': {'node': [u'\u53d1\u552e', u'\u53d1\u552e/\u6e20\u9053', u'\u53d1\u552e/\u6e20\u9053/\u7ebf\u4e0a', u'\u53d1\u552e/\u6e20\u9053/\u7ebf\u4e0a/\u5b98\u65b9\u7ebf\u4e0a'], 'score': 0.5851699113845825}}
    while True:
        query = raw_input('问题:')
        node = tree.get_final_node(candidates)
        # node = tree.get_node(query)
        print 'node:',node