import os
import yaml


class ReadYAML():
    def __init__(self,filename):
        # 动态组装文件路径及文件名
        self.file_path = os.getcwd()+os.sep+"Data"+os.sep+filename
    # 通过pytest命令执行时
    def read_yaml(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            return yaml.load(f)