import pytest
from time import sleep
from common import system_tab
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common import countList
from common.connectSQL import searchDB
from common import connectSQL


class TestBooleanTime(object):
    def test_booleanTime(self, driver):
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
        # 後台首頁點擊運轉時數設定
        system_tab.booleanTime(driver)

        # ----------------------- 新增運轉時數 ---------------------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateBooleanTimeModal()']").click()

        sleep(1)

        # 點擊選擇地圖
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchMap()']").click()

        sleep(1)

        # 點擊CE區電力系統1
        driver.find_element_by_css_selector("[title='CE區電力系統1']").click()

        sleep(1)

        # 點擊 PM_TR2 UPS P-A4_跳脫 () 警報點
        driver.find_element_by_id("booleanMapDevice_37983").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 新增後獲取當前運轉時數列表count
        booleanTimeList = countList.booleanTimeInBooleanTimeList(driver)

        sleep(1)
        # 取資料庫count數
        booleanTimeSqlCount = searchDB.booleanTime()
        # 驗證列表、資料庫count數比對
        assert booleanTimeList == booleanTimeSqlCount

        sleep(1)

        # ----------------------- 篩選運轉時數 ---------------------------
        # 篩選框輸入關鍵字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").send_keys('PM_TR2 UPS')

        sleep(1)

        # 篩選後獲取當前運轉時數列表count
        booleanTimeList = countList.booleanTimeInBooleanTimeList(driver)

        sleep(1)
        # 驗證篩選後列表count數
        assert booleanTimeList == 1

        # ----------------------- 刪除運轉時數 ---------------------------
        # 點擊運轉時數列表第一項刪除按鈕
        driver.find_element_by_xpath("//*[@id='BooleanTimeTable']/div[2]/table/tbody/tr[2]/td[5]/button").click()

        sleep(1)

        # 點擊刪除視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除搜尋框關鍵字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").clear()

        sleep(1)

        # 刪除後獲取當前運轉時數列表count
        booleanTimeList = countList.booleanTimeInBooleanTimeList(driver)

        sleep(1)

        # 取資料庫count數
        booleanTimeSqlCount = searchDB.booleanTime()
        # 驗證列表、資料庫count數比對
        assert booleanTimeList == booleanTimeSqlCount

        sleep(1)
