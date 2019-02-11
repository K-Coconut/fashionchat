#coding=utf-8
import jieba
import util.load_dict 
from util import config
import global_config
root_path = global_config.root_path
config_args_dict = {"{config_root_path}": root_path}

sys_config = config.loadconfig("{config_root_path}/sys.conf", config_args_dict)

tree_config = config.loadconfig(sys_config["_conf_tree_file"], config_args_dict)
rerank_config = config.loadconfig(sys_config["_conf_rerank_file"], config_args_dict)


retriver_config = config.loadconfig(sys_config["_conf_retriver_file"], config_args_dict)

jieba.load_userdict(sys_config["_conf_cut_dict"])

em=util.load_dict.EntityManager(sys_config["_conf_entity_list"])








