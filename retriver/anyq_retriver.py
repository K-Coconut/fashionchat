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
        json_data = json.load(res_text)
        #[{"query" :score}]
        return json_data


    def call(self, querys, nlu_parse_results)  
        results = {}
        for q in querys:
            res = requests.get(url, {"query": q})
            results[q] = self._parse_result(res.text)
        return results
