__author__ = "Tibbers"

from tool import *
from airtest.report.report import simple_report
import logging

file = '\Page_case\Home_search.yaml'

poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
class TestPage():
    auto_setup(__file__, logdir=True, devices=["Android:///", ])
    # poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    logger = logging.getLogger('airtest')
    logger.setLevel(logging.WARN )

    # simple_report(__file__)



    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>"*5,"start>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def case01(self):
        start_app('com.ak.zanjiadoctor')  # 启动app
        drivec = Driver()
        file = '\Page_case\Home_search.yaml'
        kw = 'case01'
        data = Yaml().get_yaml(file, kw)


        for item in data :
            print('定位到的元素：',data[item]['element_info'],'页面操作：',data[item]['operate_type'])
            print("<><><><><><><><><><><><><><><><><><><><><>"*5)
            if data[item]['operate_type'] == 'click' :
                drivec.wait(data[item]['element_info'])
                drivec.click(data[item]['element_info'])

            elif data[item]['operate_type'] == 'input' :
                drivec.wait(data[item]['element_info'])
                drivec.input((data[item]['element_info']), (data[item]['text']))

            elif data[item]['operate_type'] == 'swip' :
                drivec.scroll_down(1)

            elif  data[item]['operate_type'] == 'text':
                drivec.text_wait(data[item]['element_info'])
                sleep(2.0)
                drivec.text_chick(data[item]['element_info'])

            elif data[item]['operate_type'] == 'key':
                drivec.press_key()
                sleep(2.0)


            elif data[item]['operate_type'] == 'poco':
                # print((data[item]['element_info']), (data[item]['text']))
                # drivec.offspring((data[item]['element_info']), (data[item]['text']))
                key =data[item]['element_info']
                keys=eval(key)
                # print(type(keys))
                # print(keys)
                # keys=(keys.replace("'",""))
                vale = (data[item]['text'])
                drivec.offspring_wait(keys)
                drivec.offspring(keys,vale)
                # sleep(2.0)


if __name__ == '__main__':
    TestPage.case01('')
    simple_report(__file__, logpath=True, logfile=r"D:\pytest\air_selenium\case\log\log.txt",
                  output=r"D:\pytest\air_selenium\case\log\log1234.html")

