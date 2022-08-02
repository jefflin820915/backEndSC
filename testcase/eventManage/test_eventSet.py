import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from common import system_tab
from common import countList
from common import getDownLoadedFileName
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestEventSet(object):
    def test_eventSet(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # ----------------------------------- 設備事件 ---------------------------------------

        # 登入
        system_tab.login(driver)
        # 後台首頁點擊事件設定 - 設備事件
        system_tab.deviceEvent(driver)

        sleep(1)

        # --------------- 輸入搜尋關鍵字搜尋設備事件 -----------------
        driver.find_element(By.CSS_SELECTOR, "[ng-change='searchSubsystemEvents()']").send_keys("火")

        sleep(1)

        # 取得搜尋後當前設備事件列表count
        # 取得當前設備事件列表count
        deviceEventList = countList.eventInSubsystemEvents(driver)

        sleep(1)

        deviceEventSqlCount = searchDB.deviceEventSearch()
        assert deviceEventList == deviceEventSqlCount

        sleep(1)

        # ----------------------- 編輯設備事件 ---------------------
        # 點擊第一項設備事件列表修改圖示
        driver.find_element_by_xpath("//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[5]/button").click()

        sleep(1)

        # 點擊事件類別下拉式選項
        driver.find_element(By.CSS_SELECTOR, "[ng-model='eventModel.eventTypeName']").click()

        sleep(1)

        # 選擇"火警警報" 類別
        driver.find_element_by_xpath("//li[contains(.,'火警警報')]").click()

        sleep(1)

        # 點擊事件層級下拉式選項
        driver.find_element(By.CSS_SELECTOR, "[ng-model='eventModel.level']").click()

        sleep(1)

        # 選擇緊急
        driver.find_element(By.XPATH,
                            "//*[@id='editDeviceEventModal']/div/div/div[2]/div/div[1]/div[3]/div[2]/select/option[2]").click()

        sleep(1)

        # 點擊修改設備事件視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='editDeviceEvent()']").click()

        sleep(1)

        # 事件列表第一項事件類別,驗證結果
        eventClassOne = driver.find_element_by_xpath(
            "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[3]/select")
        # 獲取當前選取的select選項
        eventClassOneSelect = Select(eventClassOne).first_selected_option
        assert eventClassOneSelect.text == "火警警報"

        sleep(1)

        # 事件列表第一項事件層級,驗證結果
        eventLevelOne = driver.find_element_by_xpath(
            "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[4]/select")
        # 獲取當前選取的select選項
        eventLevelOneSelect = Select(eventLevelOne).first_selected_option
        assert eventLevelOneSelect.text == "緊急"

        # ----------------------- 匯出設備事件 ---------------------
        # 點擊設備事件匯出按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='exportDeviceEvent()']").click()

        sleep(2)

        # todo:位置解決, 把路徑設成變數或常數
        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(
            os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, 'download', 'Event.csv')))
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, 'download', 'Event.csv')))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ----------------------------------- 數值事件 ---------------------------------------

        # ----------------------- 新增數值事件 ---------------------
        # 點擊數值事件頁面
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/CustomEvent']").click()

        sleep(1)

        # 點擊新增
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddEditCustomEventModal(null)']").click()
        # 事件名稱輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").send_keys(load_yaml['ValueEvent']['name'])
        # 事件描述輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").send_keys(
            load_yaml['ValueEvent']['Describe'])
        # 觸發規則設定輸入數值
        driver.find_element(By.CSS_SELECTOR, "[ng-model='eventRuleTypeList[0].ruleValues[0]']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='eventRuleTypeList[0].ruleValues[0]']").send_keys("50")
        # 點擊選擇地圖
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchMap()']").click()

        sleep(1)

        # 點擊電力-配電盤-2地圖
        driver.find_element_by_css_selector("[title='電力-配電盤-2']").click()

        sleep(1)

        # 點擊GIS1 相電流Ia
        driver.find_element_by_id("mapDevice_37848").click()

        sleep(1)

        # 點擊UPS消防排煙In(A)
        driver.find_element_by_id("mapDevice_37757").click()

        sleep(1)

        # 點擊確定
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditCustomEvent(modalEvent)']").click()

        sleep(1)

        # 新增後取得當前數值事件列表count
        valueEventList = countList.eventInCustomEvents(driver)

        sleep(1)

        valueEventSqlCount = searchDB.valueEvent()
        assert valueEventList == valueEventSqlCount

        # ----------------------- 篩選數值事件 ---------------------
        # 點擊搜尋事件編輯框,輸入文字"valueEventAdd"
        driver.find_element(By.CSS_SELECTOR, "[ng-change='searchCustomEvents()']").send_keys(
            load_yaml['ValueEvent']['name'])

        sleep(1)

        # 篩選後取得當前數值事件列表count
        valueEventList = countList.eventInCustomEvents(driver)
        assert valueEventList == 1

        sleep(1)

        # 清空搜尋欄位
        driver.find_element(By.CSS_SELECTOR, "[ng-change='searchCustomEvents()']").clear()

        sleep(1)

        # ----------------------- 編輯數值事件 ---------------------
        # 點擊編輯按鈕
        driver.find_element_by_xpath("//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[8]/button[1]").click()

        sleep(1)

        # 修改事件名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").send_keys(
            load_yaml['ValueEvent']['new_name'])

        # 修改事件描述
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").send_keys(
            load_yaml['ValueEvent']['new_describe'])

        # 點擊確定
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditCustomMultipleEvent()']").click()

        sleep(1)

        valueEventNameOne = driver.find_element_by_xpath(
            "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        valueEventDescribeOne = driver.find_element(By.XPATH,
                                                    "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[5]/span")
        assert valueEventNameOne.text == load_yaml['ValueEvent']['new_name'] and valueEventDescribeOne.text == \
               load_yaml['ValueEvent']['new_describe']

        sleep(1)

        # ----------------------- 刪除數值事件 ---------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除後取得當前數值事件列表count
        valueEventList = countList.eventInCustomEvents(driver)

        sleep(1)

        valueEventSqlCount = searchDB.valueEvent()
        assert valueEventList == valueEventSqlCount

        # ----------------------------------- 複合式條件事件 ---------------------------------------
        # ----------------------- 新增複合式條件事件 ---------------------
        # 點擊複合式條件事件頁面
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/CustomMultipleEvent']").click()

        sleep(1)

        # 點擊新增
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddEditEventModal(null)']").click()

        sleep(1)

        # 事件名稱輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").send_keys(load_yaml['CustomEvent']['name'])
        # 點擊事件類別,開啟下拉式選單
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.eventTypeName']").click()
        # 點擊卡機離線
        driver.find_element_by_xpath("//li[contains(.,'卡機離線')]").click()
        # 事件描述輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").send_keys(
            load_yaml['CustomEvent']['Describe'])

        # 點擊點位一選擇平面圖圖示
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openDeviceAttributeModal(0)']").click()

        sleep(1)

        # 點擊選擇地圖
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchMap()']").click()

        sleep(1)

        # 點擊電力-配電盤-2
        driver.find_element_by_css_selector("[title='電力-配電盤-2']").click()
        # 點擊TR_01 Ia
        driver.find_element_by_id("mapDevice_37748").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='saveChooseDeviceAttribute()']").click()

        sleep(1)

        # 輸入點位一觸發規則數值
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pRules[0].eventRuleTypeList[0].ruleValues[0]']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pRules[0].eventRuleTypeList[0].ruleValues[0]']").send_keys(
            "50")

        sleep(1)

        # 點擊點位二平面圖圖示
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openDeviceAttributeModal(1)']").click()

        sleep(1)

        # 點擊選擇地圖
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchMap()']").click()

        sleep(1)

        # 點擊電力-配電盤-1
        driver.find_element_by_css_selector("[title='電力-配電盤-1']").click()

        sleep(1)

        # 點擊TR_01 用電量(KW)
        driver.find_element_by_id("mapDevice_37867").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='saveChooseDeviceAttribute()']").click()

        sleep(1)

        # 輸入點位二觸發規則數值
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pRules[1].eventRuleTypeList[0].ruleValues[0]']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pRules[1].eventRuleTypeList[0].ruleValues[0]']").send_keys(
            "100")
        # 新增複合式條件事件頁面確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditCustomMultipleEvent()']").click()

        sleep(1)

        # 新增後取得當前複合式條件事件列表count
        customMultipleEventList = countList.customMultipleEvents(driver)

        sleep(1)

        customMultipleEventSqlCount = searchDB.customMultipleEvent()
        assert customMultipleEventList == customMultipleEventSqlCount

        sleep(1)

        # ----------------------- 編輯複合式條件事件 ---------------------

        # 點擊列表第一項編輯按鈕
        driver.find_element_by_xpath("//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[8]/button[1]").click()

        sleep(1)

        # 修改複合式條件事件名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.name']").send_keys(
            load_yaml['CustomEvent']['new_name'])

        sleep(1)

        # 修改事件描述輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEvent.detail']").send_keys(
            load_yaml['CustomEvent']['new_describe'])

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditCustomMultipleEvent()']").click()

        sleep(1)

        # 列表第一項事件名稱
        customEventNameOne = driver.find_element_by_xpath(
            "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        # 列表第一項事件描述
        customEventDescribeOne = driver.find_element_by_xpath(
            "//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[5]/span")

        sleep(1)

        assert customEventNameOne.text == load_yaml['CustomEvent']['new_name'] and customEventDescribeOne.text == \
               load_yaml['CustomEvent']['new_describe']

        # ----------------------- 刪除複合式條件事件 ---------------------

        # 點擊列表第一項刪除按鈕
        driver.find_element_by_xpath("//*[@id='deviceEventTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]").click()

        sleep(1)

        # 刪除視窗 確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除後取得當前複合式條件事件列表count
        customMultipleEventList = countList.customMultipleEvents(driver)

        sleep(1)

        customMultipleEventSqlCount = searchDB.customMultipleEvent()
        assert customMultipleEventList == customMultipleEventSqlCount

        sleep(1)
