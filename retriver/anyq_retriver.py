#coding=utf-8
from retriver import Retriver
import requests
import json

class AnyqRetriver(Retriver):
    def __init__(self, config)
        self.port = config["_config_port"]
        self.hostname = config["_config_hostname"]
        self.url_tmp = config["_config_urltmp"]
        self.url = self.url_tmp % (self.hostname, self.port)
          

    def _parse_result(self, res_text): 
        json_data = json.loads(res_text)
        json_dict = {}
        for j in json_data:
            json_dict[j["question"]] = {}    
            json_dict[j["question"]]["score"] = j["confidence"]
        return json_dict 


    def call(self, query):  
        res = requests.get(url, {"question": query})
        return self._parse_result(res.text)
