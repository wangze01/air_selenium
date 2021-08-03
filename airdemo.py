from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import sys

auto_setup(__file__, logdir=True, devices=["Android:///", ])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=False, screenshot_each_action=False)
print("start>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def offspring(key,text) :
    keys = key
    keys.click()
    keys.set_text(text)

# start_app('com.ak.zanjiadoctor')  # 启动app
# poco(text="居民").click()

# key=poco(text='体温').parent().offspring(text="请输入")
# key.click()
offspring(poco(text='体温').parent().offspring(text="请输入"),36)

