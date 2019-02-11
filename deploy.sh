current_dir=`pwd`
project_dir=$(dirname $(readlink -f $0))
cd $project_dir
cd configs/dict/
bash create_entity_list.sh 
bash create_jieba_dict.sh
cd $project_dir
config_root=`readlink -f configs`
cat >global_config.py <<EOF
#coding=utf-8
root_path = "$config_root"
EOF
