import os.path

import yaml

def read_yaml(path):
    with open(path,mode='r',encoding='utf-8') as f:
       value= yaml.load(stream=f,Loader=yaml.FullLoader)
       return value


def read_config_file(node_name):
    return 1
s
def read_extract_file(node_name):
    return 2