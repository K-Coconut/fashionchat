#coding=utf-8
import util.config as cf

class RetriverManager(object):

    def __init__(self, config):
        self.retriver = None 
        if "_config_anyq" in config:
            from .anyq_retriver import AnyqRetriver
            self.retriver = AnyqRetriver(cf.loadconfig(config['_config_anyq']))
    
    def retrive(self, query):
        if not self.retriver:
            return {}
        return self.retriver.call(query) 

