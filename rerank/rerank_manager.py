#coding=utf-8

class RerankManager(object):
    def __init__(self, config):
        self.reranker = None 
        if ["_config"] in config:
            pass
        else:
            import .reranker.DefaultReranker as DefaultReranker
            self.reranker = DefaultReranker(None)
    
    def rerank(self, query, q_nlu_parse_result, candidates, nlu_parse_results): 
        if not self.reranker:
            return candidates
        return self.reranker.rerank(querys, q_nlu_parse_result,  candidates, nlu_parse_results) 

