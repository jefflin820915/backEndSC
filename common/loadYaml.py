import os
import yaml


def loadYaml():
    with open('../data/data.yaml', 'r', encoding='utf-8')as yaml_data:
        data = yaml.load(stream=yaml_data, Loader=yaml.FullLoader)
        print(data)
    return data
