#coding=utf-8
import json

import resource


class QueryFilter(object):
    def __init__(self, config):
        self.__dict = self.__load(config)

    def __load(self, config):
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

    def get(self):
        return self.__dict

    def hit(self, query):
        __dict = self.get()
        if query in __dict:
            return __dict[query]
        return None

if __name__ == '__main__':
    tree_config = resource.tree_config
    t=QueryFilter(tree_config)
    print json.dumps(t.get(),ensure_ascii=False,encoding='utf-8')
    while True:
        query = raw_input('问题:')
        query = query.decode('utf-8')
        print t.hit(query)