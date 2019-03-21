#coding=utf-8
import resource
import tree
from lt.ltools import LTool,add_dict
from retriver.retriver_manager import  RetriverManager
from rerank.rerank_manager import RerankManager
from slot_parser.slot_parser import SlotParser
import json

tree_config     = resource.tree_config
rerank_config   = resource.rerank_config
retriver_config = resource.retriver_config


g_ltool = LTool(None)
g_tree = tree.Tree(tree_config)
g_retriver_m = RetriverManager(retriver_config)
g_reranker_m = RerankManager(rerank_config)
g_sp = SlotParser()
add_dict()

def forprint(_d):
    return json.dumps(_d,encoding='utf-8',ensure_ascii=False)

def get_tree_cache(query):
    #tree cache 
    node = g_tree.get_node(query)
    if node:
        return node

def get_retriver_node(query):
    nlu_result = g_ltool.cut(query)
    candidates = g_retriver_m.retrive(query)
    print 'candidates1:',forprint(candidates)
    args = {"tree": g_tree}
    args["sp"] = g_sp
    args["nlu_result"] = nlu_result
    candidates = g_reranker_m.rerank(query, candidates, args)
    print 'candidates2:',forprint(candidates)
    return g_tree.get_final_node(candidates)

def get_slot(node, query):
    slot_dict = {}
    nlu_result = g_ltool.cut(query)
    return g_sp.parse(query, nlu_result)
    

def infer(query):
    if type(query) is str:
        query = query.decode("utf-8")
    node = None

    # 从知识树中搜索query的节点
    node = get_tree_cache(query)

    # 如果节点不存则重新召回继续找节点
    if not node:
        node = get_retriver_node(query)

    # 如果节点存在则返回节点的槽位及节点否则返回None
    if node:
        return get_slot(node, query), node
    return None, None

if __name__ == "__main__":
    while(True):
        query = raw_input("query:\n")
        get_retriver_node(query)

        slot_dict, node = infer(query)
        print "============"
        print "node"
        if node is None:
            continue
        print node.encode("utf-8")
        for key in slot_dict:
            print key.encode("utf-8"), slot_dict[key].encode("utf-8")
