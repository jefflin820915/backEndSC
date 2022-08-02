import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestEventCategory(object):
    def test_eventCategory(self, driver):
        """
            @type driver: selenium.webdriver.remote.webdriver.WebDriver
            @:type driver: selenium.webdriver.remote.webdriver.WebDriver
            :return:
            """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # 調用登入方法,登入後台
        system_tab.login(driver)
        # 後台首頁點擊事件類別
        system_tab.eventCategory(driver)

        sleep(1)

        # --------------------------  新增 -----------------------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddEditEventTypeModal(null)']").click()

        sleep(1)

        # 新增1 輸入新增視窗類別名稱
        addEditCateGoryName = driver.find_element(By.CSS_SELECTOR, "[ng-model='modalEventType.chineseName']")
        addEditCateGoryName.send_keys(load_yaml['EventCategory']['name'])
        # 點擊確定按鈕,創建事件類別
        addEditConfirmButton = driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventType()']")
        addEditConfirmButton.click()

        sleep(1)
        # 取事件類別列表count數
        eventCategoryList = countList.eventCategoryList(driver)

        sleep(1)
        # 取資料庫count數
        eventCategorySqlCount = searchDB.eventCategory()
        # 驗證列表、資料庫count數比對
        assert eventCategoryList == eventCategorySqlCount

        sleep(1)

        # --------------------------  編輯 -----------------------------
        # 點擊新增1事件類別編輯圖示
        driver.find_element_by_xpath("//*[@id='eventTypeTable']/div[2]/table/tbody/tr[20]/td[3]/button[1]").click()

        sleep(1)

        # 輸入修改視窗類別名稱
        addEditCateGoryName.clear()
        addEditCateGoryName.send_keys(load_yaml['EventCategory']['new_name'])
        # 點擊確定按鈕,修改事件類別
        addEditConfirmButton.click()

        sleep(1)

        # 驗證新增1事件類別名稱是否修改成功
        addEventCategoryName = driver.find_element_by_xpath("//*[@id='eventTypeTable']/div[2]/table/tbody/tr[20]/td[2]")
        # 驗證是否為修改後名稱
        assert addEventCategoryName.text == load_yaml['EventCategory']['new_name']

        # --------------------------  刪除 -----------------------------
        # 點擊刪除
        driver.find_element_by_xpath("//*[@id='eventTypeTable']/div[2]/table/tbody/tr[20]/td[3]/button[2]").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)
        # 取事件類別列表count數
        eventCategoryList = countList.eventCategoryList(driver)

        sleep(1)
        # 取資料庫count數
        eventCategorySqlCount = searchDB.eventCategory()
        # 驗證列表、資料庫count數比對
        assert eventCategoryList == eventCategorySqlCount

        sleep(1)
