#coding=utf-8

def SlotParser(object):
    def __init__(self):
        pass
     
    def parse(self, query, nlu_parse_result):
        slot_dict = {}
        for word, norm_word, dict_names in nlu_parse_result:
            for _name in dict_names:
                slot_dict[_name] = norm_word
        return slot_dict
        

