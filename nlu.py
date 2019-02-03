#coding=utf-8
import resource
import tree
from retriver.retriver_manager import  RetriverManager
from rerank.rerank_manager import RerankManager


tree_config     = resource.tree_config
rerank_config   = resource.rerank_config
retriver_config = resource.retriver_config


g_tree = tree.Tree(tree_config)
g_retriver_m = RetriverManager(retriver_config)
g_reranker_m = RerankManager(rerank_config)


