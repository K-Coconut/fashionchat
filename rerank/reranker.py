#coding=utf-8


class Reranker(object):
    def __init__(self, config):
        pass
    
    def rerank(self, query,candidates, args):  
        pass

class DefaultReranker(Reranker):
    def __init__(self, config):
        pass
    
    def rerank(self, query, candidates, args):  
        return candidates
