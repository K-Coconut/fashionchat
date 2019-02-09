#coding=utf-8
import resource
import tree
from lt.ltools import LTool
from retriver.retriver_manager import  RetriverManager
from rerank.rerank_manager import RerankManager
from slot_parser.slot_parser import SlotParser


tree_config     = resource.tree_config
rerank_config   = resource.rerank_config
retriver_config = resource.retriver_config


g_ltool = LTool(None)
g_tree = tree.Tree(tree_config)
g_retriver_m = RetriverManager(retriver_config)
g_reranker_m = RerankManager(rerank_config)
g_sp = SlotParser()

def get_tree_cache(query):
    #tree cache 
    node = g_tree.get_node(query)
    if node:
        return node

def get_retriver_node(query):
    nlu_result = g_ltool.cut(query)
    candidates = g_retriver_m.retrive(query) 
    args = {"tree": g_tree}
    args = {"sp": g_sp}
    candidates = g_retriver_m.rerank(query, candidates, args)
    return g_tree.get_final_node(candidates)

def get_slot(node, query):
    slot_dict = {}
    nlu_result = g_ltool.cut(query)
    return g_sp.parse(query, nlu_result)
    

def infer(query):
    if type(query) is str:
        query = query.decode("utf-8")
    node = None
    node = get_tree_cache(query)
    if not node:
        node = get_retriver_node(query)    
    if node:
        return get_slot(node, query), node
    return None, None

if __name__ == "__main__":
    
