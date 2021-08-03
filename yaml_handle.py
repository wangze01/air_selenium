# -*-coding:utf-8 -*-
# @Author: Tibbers
# Created on: 2021-07-29

import yaml
from Config.project_var import project_var



class Yaml:
    def get_yaml(self, file_name, keyword):
        file_path = project_var + file_name
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                cont = f.read()
                yaml_obj = yaml.load(cont, Loader=yaml.FullLoader)
                return yaml_obj[keyword]
        except Exception as e:
            ('读取设备配置信息文件失败：{}'.format(e))


if __name__ == '__main__':
    file = '\Page_case\Home_search.yaml'
    kw = 'case01'
    # data = Yaml().get_yaml(file, kw)
    # print(len(data))
    # for key, item in data.items():

    data = Yaml().get_yaml('\\Page_case\\Home_search.yaml',kw)
    print(data)

    # print(type(data['element_info']))
