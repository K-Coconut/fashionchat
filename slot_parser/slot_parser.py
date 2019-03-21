#coding=utf-8

class SlotParser(object):
    def __init__(self):
        pass

    # nlu_result: [["上海", "上海", ["city"]], ["耐克", "nike", ["Brand"]], ["店", "店", []], ["什么", "什么", []], ["时候", "时候", []], ["发", "发", []], ["耐克", "nike", ["Brand"]], ["AJ1", "AJ1", []], ["画报", "画报", []]]
    def parse(self, query, nlu_parse_result):
        slot_dict = {}
        for word, norm_word, dict_names in nlu_parse_result:
            for _name in dict_names:
                slot_dict[_name] = norm_word
        return slot_dict
        

