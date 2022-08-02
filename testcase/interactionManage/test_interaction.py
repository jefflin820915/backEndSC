import pytest
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestInteraction(object):
    def test_interaction(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # ----------------------------------- 連動設定 ---------------------------------------
        # 登入
        system_tab.login(driver)
        # 後台首頁點擊連動設定
        system_tab.interaction(driver)

        # --------------- 新增連動列表 -----------------
        # 連動設定 新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateInteractionModal()']").click()

        sleep(1)

        # 新增連動  名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='interactionModel.name']").send_keys(
            load_yaml['Interaction']['name'])
        # 選擇事件
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeEditEventArea()']").click()

        sleep(1)

        # 輸入觸發事件篩選
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").send_keys("火警")

        sleep(1)

        # 點擊解除火警事件
        driver.find_element_by_xpath("//*[@id='EventListTable']/div[2]/table/tbody/tr[3]/td[2]").click()

        sleep(1)

        # 點擊選擇地圖
        driver.find_element(By.CSS_SELECTOR, "[data-id='eventMapList']").click()
        # 點擊平面10F
        driver.find_element_by_xpath("//li[contains(.,'平面圖-10F')]").click()

        sleep(1)

        # 點擊平面圖 id eventMapDevice_6365 點位
        driver.find_element_by_id("eventMapDevice_6365").click()
        # 點擊平面圖 id eventMapDevice_6373 點位
        driver.find_element_by_id("eventMapDevice_6373").click()

        # 點擊進度2 連動動作
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeStep(2)']").click()

        sleep(1)

        # 點擊觸發動作
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeEditActionGroupArea()']").click()

        sleep(1)

        # 點擊動作 3樓監視器
        driver.find_element_by_xpath("//*[@id='ActionGroupListTable']/div[1]/table/tbody/tr[5]/td[2]").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 新增後取得當前連動列表count
        interactionList = countList.interaction(driver)

        sleep(1)
        # 取資料庫count數
        interactionSqlCount = searchDB.interaction()
        # 列表count數與資料庫count數做對比驗證
        assert interactionList == interactionSqlCount

        # --------------- 篩選連動列表 -----------------
        # 搜尋欄位 輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").send_keys(
            load_yaml['Interaction']['name'])

        sleep(1)

        # 搜尋後取得當前連動列表count
        interactionList = countList.interaction(driver)
        # 驗證搜尋後列表count數
        assert interactionList == 1

        sleep(1)

        # 刪除搜尋框文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").clear()

        # --------------- 編輯連動列表 -----------------
        # 點擊編輯按鈕
        driver.find_element_by_xpath("//*[@id='InteractionTable']/div[2]/table/tbody/tr[2]/td[7]/button[1]").click()

        sleep(1)

        # 修改連動 修改名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='interactionModel.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='interactionModel.name']").send_keys(
            load_yaml['Interaction']['new_name'])

        sleep(1)

        # 點擊進度2 連動動作
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeStep(2)']").click()

        sleep(1)

        # 點擊自動連動開關按鈕 : 開啟
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeAuto()']").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 連動列表第一項 名稱
        interactionOneName = driver.find_element_by_xpath(
            "//*[@id='InteractionTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        # 驗證修改後名稱
        assert interactionOneName.text == load_yaml['Interaction']['new_name']
        # 連動列表第一項 觸發狀況
        interactionOneTrigger = driver.find_element_by_xpath(
            "//*[@id='InteractionTable']/div[2]/table/tbody/tr[2]/td[5]")
        # 驗證修改後觸發狀況
        assert interactionOneTrigger.text == '自動'

        sleep(1)

        # --------------- 刪除連動列表 -----------------

        # 連動列表第一項 刪除按鈕
        driver.find_element_by_xpath("//*[@id='InteractionTable']/div[2]/table/tbody/tr[2]/td[7]/button[2]").click()

        sleep(1)

        # 刪除連動視窗 確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除後取得當前連動列表count
        interactionList = countList.interaction(driver)

        sleep(1)

        # 取資料庫count數
        interactionSqlCount = searchDB.interaction()
        # 驗證列表、資料庫count數比對
        assert interactionList == interactionSqlCount
