from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from yaml_handle import Yaml
from appium.webdriver.common.touch_action import TouchAction

# auto_setup(__file__, logdir=True, devices=["Android:///", ])
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
class Driver:
    #
    auto_setup(__file__, logdir=True, devices=["Android:///", ])
    poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def wait(self,key):
        try:
            self.poco(key).wait_for_appearance(timeout=30)
        except:
            ('输入内容失败：{}'.format())

    def text_wait(self,key):
        try:
            self.poco(text=key).wait_for_appearance(timeout=30)
        except:
            ('输入内容失败：{}'.format())

    def offspring_wait(self,key):
        try :
            keys = key
            keys.wait_for_appearance(timeout=30)
        except:
            print('等待超时')


    def click(self,key):
        """点击元素"""

        try:
            self.poco(key).click()
            # self.poco(text="居民").click()
        except Exception as e:
            print("未找到元素")

    def input(self, keyword, text) :
        """向文本框元素输入内容"""
        try :
            self.poco(keyword).set_text(text)

        except Exception as e :
            ('输入内容失败：{}'.format(e))

    def clear(self, type, keyword) :
        """清除文本框内的内容"""
        try :
            self.find_element(type, keyword).clear()
        except Exception as e :
            ('清除输入框内容失败：{}'.format(e))

    def text_chick(self,key):
        try:
            self.poco(text=key).click()
        except:
            print('清除输入框内容失败')

    def offspring(self,key,text):
        try:
            keys = key
            keys.click()
            keys.set_text(text)
        except:
            print('报错')



    # def get_size(self):
    #     """获取屏幕尺寸"""
    #     try :
    #         w, h = device().get_current_resolution()  # 获取手机分辨率
    #         print(w, h)
    #         for i in range(6) :
    #             touch([0.5 * w, 0.5 * h])  # 点击手机中心位置
    #             swipe((0.5 * w, 0.7 * h), vector=(0, -0.75), duration=0.2)
    #             sleep(2.0)
    #         self.poco.scroll(direction="vertical", percent=0.8, duration=3.0)
    #         print('页面下拉操作，定位xxx')
    #     except :
    #         print('操作报错了')

    def scroll_down(self, vale):
        try :
            w, h = device().get_current_resolution()  # 获取手机分辨率
            print(w, h)
            for i in range(vale) :
                touch([0.5 * w, 0.5 * h])  # 点击手机中心位置
                swipe((0.5 * w, 0.7 * h), vector=(0, -0.75), duration=0.2)
                sleep(2.0)
            self.poco.scroll(direction="vertical", percent=0.8, duration=3.0)
            print('页面下拉操作，定位xxx')
        except :
            print('操作报错了')

    def assert_string_in_pagesource(self, assertString, *args):
        """断言页面源码是否存在某关键字或关键字符串"""
        page_source = self.driver.page_source
        try:
            assert assertString in page_source, "{} not found in page source!".format(assertString)
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            ('判断页面元素失败：{}'.format(e))

    def press_key(self):
        """发送一个键码的操作"""
        """4"""
        keyevent('BACK')
        # self.driver.press_keycode(key)
        # self.drivec().pressKeyCode(key)


if __name__ == '__main__':
    start_app('com.ak.zanjiadoctor')  # 启动app
    drivec=Driver()

    # file = '\Page_case\Home_search.yaml'
    # kw = 'case01'
    # data = Yaml().get_yaml('\\Page_case\\Home_search.yaml',kw)
    # print(data)
    # print(data['输入账号']['element_info'])
    # drivec.press_key('KEYCODE_BACK')
    # drivec.press_key()
    drivec.offspring(poco(text='体温').parent().offspring(text="请输入"),36.5)

    # print((data[item]['element_info']), (data[item]['text']))
    # drivec.offspring((data[item]['element_info']), (data[item]['text']))
    key = data[item]['element_info']
    keys = eval(key)
    # print(type(keys))
    # print(keys)
    # keys=(keys.replace("'",""))
    vale = (data[item]['text'])
    # drivec.offspring_wait(key)
    # drivec.offspring(keys,vale)
    drivec.offspring(keys, vale)
    sleep(2.0)

    # drivec.text_chick('居民')

    # poco(text="居民").click()

    # for item in data:
    #     if data[item]['operate_type'] == 'click':
    #         drivec.click(data[item]['element_info'])
    #     elif data[item]['operate_type'] == 'input':
    #         drivec.input((data[item]['element_info']),(data[item]['text']))
