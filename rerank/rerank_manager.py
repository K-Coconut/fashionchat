#coding=utf-8
form .tree_reranker import TreeReranker
class RerankManager(object):
    def __init__(self, config):
        self.reranker = None 
        if ["_config_tree_reranker"] in config:
            self.reranker = TreeReranker(None)
        else:
            import .reranker.DefaultReranker as DefaultReranker
            self.reranker = DefaultReranker(None)
    
    def rerank(self, query, candidates, args): 
        if not self.reranker:
            return candidates
        return self.reranker.rerank(query, candidates, args) 

