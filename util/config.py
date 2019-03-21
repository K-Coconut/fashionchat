#coding=utf-8

def _replace_args(str_var, replace_dict):
    if replace_dict is None:
        return str_var 
    for src_str in replace_dict:
        dest_str = replace_dict[src_str]
        str_var = str_var.replace(src_str, dest_str)
    return str_var

def loadconfig(config_file, replace_dict=None):
    config_file = _replace_args(config_file, replace_dict)
    file_content = None
    with open(config_file) as fr:
        file_content = fr.read()
    if file_content:
        _t = {}

        # exec 函数为执行文本内容,_t['..']=.. ; _t包含系统变量__builtins__
        exec(file_content, _t)

        # 只有前缀为_conf的配置有效
        prefix = "_conf"
        if "prefix" in _t:
            prefix = _t["prefix"]
        
        config_dict = {}
        for name in _t:
            if name.startswith(prefix): 
                value = _replace_args(_t[name], replace_dict)
                config_dict[name] = value
        return config_dict
    return {}
