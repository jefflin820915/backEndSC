from common import system_tab
from common import countList
from common import connectSQL
from common.connectSQL import searchDB
from time import sleep
import pytest
import logging


class TestSubSystemInformation(object):
    def test_subSystemInformation(self, driver):
        """
        @type driver: selenium.webdriver.remote.webdriver.WebDriver
        @:type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return:
        """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # 調用登入方法，進入後台
        system_tab.login(driver)
        # 後台首頁點擊子系統資訊
        system_tab.subSystemInformation(driver)
        # 取子系統資訊列表count數
        subSysList = countList.subsystemInSubsystemList(driver)

        sleep(1)
        # 取資料庫count數
        subsystemInformationSqlCount = searchDB.subsystemInformation()
        # 驗證列表、資料庫count數比對
        assert subSysList == subsystemInformationSqlCount

        sleep(1)

        # # 找name為到tr的元素，全部拿取
        # tr = driver.find_elements_by_tag_name("tr")
        # # 調用遍歷trtd方法，拿到當前頁面全部td list
        # tdList = system_tab.tr_td(tr)
        # # 處理list空字串問題，刪除全部空字串
        # tdDelNoneList = list(filter(None, tdList))
        # # 刪除更新時間
        # del tdDelNoneList[4:len(tdDelNoneList):5]
        # assert tdDelNoneList == ['1', '電力系統', '電力系統', 'OPCUA',
        #                  '2', '儲能系統', '能源管理系統', 'ModbusTCP',
        #                  '3', '能源管理系統', '能源管理系統', 'EntryGuard_Chiyu',
        #                  '4', '給排水系統', '衛生給排水系統', 'ModbusTCP',
        #                  '5', '監視系統', '監視系統', 'MQTTBox',
        #                  '6', '空調系統-冰水主機', '冰水主機系統', 'OPCUA',
        #                  '7', '空調系統', '空調系統', 'ModbusTCP',
        #                  '8', '照明系統', '照明系統', 'ModbusTCP',
        #                  '9', '門禁系統', '門禁系統', 'EntryGuard_Chiyu',
        #                  '10', '消防系統', '消防系統', 'OPCUA']
