#coding=utf-8


class TreeReranker(Reranker):
    def __init__(self, config)
        pass
    
    def rerank(self, query, candidates, args):
        tree = args["tree"]
        slot_parse = args["sp"]
        slot_dict = slot_parse.parse(query, nlu_result)
        q_slot_list = set(slot_dict.keys())
        result = {}
        for candi in candidates:    
            node = tree.get_node(query)
            sp_node = node.split("/")
            node_list = []
            for _l in range(len(sp_node)): 
                t_node = "/".join(sp_node[:_l+1])
                slot_list = set(tree.get_node_need_slot(t_node))
                if slot_list.issubset(q_slot_list):
                    node_list.append(t_node)

            if len(node_list) > 0:
                result[candi] = {}
                result[candi]["score"] = candidates["candi"]["score"]
                result[candi]["node"] = node_list 
        return result
