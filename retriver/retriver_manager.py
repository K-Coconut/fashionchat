#coding=utf-8

class RetriverManager(object):

    def __init__(self, config)
        self.retriver = None 
        if ["_config_anyq"] in config:
            import .anyq_retriver.AnyqRetriver as AnyqRetriver
            self.retriver = AnyqRetriver(config['_config_anyq'])
    
    def retrive(self, querys, nlu_parse_results)  
        if not self.retriver:
            return {}
        return self.retriver.call(querys, nlu_parse_results) 

