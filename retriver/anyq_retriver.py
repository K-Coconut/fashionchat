#coding=utf-8
from retriver import Retriver
import requests
import json

# AnyQ召回
class AnyqRetriver(Retriver):
    def __init__(self, config):
        self.port = config["_config_port"]
        self.hostname = config["_config_hostname"]
        self.url_tmp = config["_config_urltmp"]

    def _parse_result(self, res_text): 
        json_data = json.loads(res_text)
        json_dict = {}
        for j in json_data:
            json_dict[j["question"]] = {}    
            json_dict[j["question"]]["score"] = j["confidence"]
        return json_dict 

    def call(self, query):  
        self.url = self.url_tmp % (self.hostname, self.port, query)
        self.url=self.url.replace('127.0.0.1','129.211.128.129')
        res = requests.get(self.url)
        #return result
        #{“我要去买耐克”:{“score”:0.8}, “我想去买耐克”:{score:”0.8”}}
        return self._parse_result(res.text)

