#coding=utf-8

class EntityManager(object):
    def __init__(self, list_file_name):
        self.entity_list = self._get_all_entity(list_file_name)
        

    def find(self, word):
        for e in self.entity_list:
            if word in e.dict:
                return (word, e.dict[word], e.name)
        return (word, None, None)

    def _get_entity_name_list(self, list_file_name) 
        _list = []
        with open(list_file_name) as fr:
            for line in fr:
                line = line.decode("utf-8").strip()
                _list.append(line)
        return _list

    def _get_all_entity(self, list_file_name):
        entity_list = []
        for e_name in self._get_entity_name_list(list_file_name):
            e = EntityDict(e_name) 
            entity_list.append(e)
        return entity_list
                


class EntityDict(object):
    def __init__(self, file_name, name=None):
        self.name = name 
        self.dict = _loadfile(file_name)
        self._get_name(file_name)
        pass

    def _get_name(self, file_name):
        if self.name:
            return self.name
        else:
            sps = file_nam.split("/") 
            self.name = sps[-1]
        return self.name
        
    def _loadfile(self, file_name):
        _dict = {}
        with open(file_name) as fr:
            for line in fr:
                sps = line.decode("utf-8").strip().split("\t")
                _dict[sps[0]] = sps[0]
                for _i in sps[1:]:
                    _dict[_i] = sps[0]
        return _dict
