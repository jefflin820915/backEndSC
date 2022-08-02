import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import loadYaml

load_yaml = loadYaml.loadYaml()


class TestActionGroup(object):
    def test_actionGroup(self, driver):
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
        # 後台首頁點擊動作群組
        system_tab.actionGroup(driver)

        # ----------------------- 新增動作群組 ---------------------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateActionGroupModal()']").click()

        sleep(1)

        # 動作群組名稱 輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='actionGroupModel.name']").send_keys(
            load_yaml['ActionGroup']['name'])
        # 選擇動作設備,點擊選地圖,彈出搜尋圖面視窗
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchMap()']").click()

        sleep(1)

        # 點擊篩選第一圖層下拉式選單
        driver.find_element(By.CSS_SELECTOR, "[ng-model='firstMapFolderId']").click()
        # 第一圖層選擇平面圖
        driver.find_element(By.XPATH, "//li[contains(.,'平面圖')]").click()
        # 選擇平面圖10F
        driver.find_element(By.CSS_SELECTOR, "[title='平面圖-10F']").click()

        sleep(1)
        # 選擇平面圖球型攝影機鏡頭(10F東北電梯口(球型攝影機))
        driver.find_element_by_id("actionMapDevice_33076").click()

        sleep(1)

        # 選擇平面圖球型攝影機鏡頭(10F東南電梯口(球型攝影機))
        driver.find_element_by_id("actionMapDevice_33077").click()

        sleep(1)

        # 點擊屬性點位Tab
        driver.find_element(By.CSS_SELECTOR, "[onclick='changeTab(1)']").click()

        sleep(1)

        # 點擊屬性點位第一項
        driver.find_element(By.ID, "deviceAttribute0").click()

        sleep(1)

        # 點擊新增動作群組確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 新增後取得當前動作群組列表count
        actionGroupList = countList.actionGroup(driver)

        sleep(1)
        # 取資料庫count數
        actionGroupSqlCount = searchDB.actionGroup()
        assert actionGroupList == actionGroupSqlCount

        # ----------------------- 篩選動作群組 ---------------------------
        # 動作群組篩選關鍵字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").send_keys(
            load_yaml['ActionGroup']['name'])
        sleep(1)

        # 篩選後取得當前動作群組列表count
        actionGroupList = countList.actionGroup(driver)

        sleep(1)

        assert actionGroupList == 1

        # 清除篩選關鍵字欄位
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").clear()

        sleep(1)

        # ----------------------- 編輯動作群組 ---------------------------
        # 點擊動作群組列表第一項編輯按鈕
        driver.find_element_by_xpath("//*[@id='ActionGroupTable']/div[2]/table/tbody/tr[2]/td[3]/button[1]").click()
        # 修改動作群組 動作群組名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='actionGroupModel.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='actionGroupModel.name']").send_keys(
            load_yaml['ActionGroup']['new_name'])

        # 點擊新增動作群組確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()
        # 動作群組列表第一項名稱
        actionGroupListOneName = driver.find_element_by_xpath(
            "//*[@id='ActionGroupTable']/div[2]/table/tbody/tr[2]/td[2]")
        # 驗證是否為修改後名稱
        assert actionGroupListOneName.text == load_yaml['ActionGroup']['new_name']

        sleep(1)

        # ----------------------- 刪除動作群組 ---------------------------
        # 點擊動作群組列表第一項刪除按鈕
        driver.find_element_by_xpath("//*[@id='ActionGroupTable']/div[2]/table/tbody/tr[2]/td[3]/button[2]").click()

        sleep(1)

        # 刪除動作群組確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除後取得當前動作群組列表count
        actionGroupList = countList.actionGroup(driver)

        sleep(1)
        # 取資料庫count數
        actionGroupSqlCount = searchDB.actionGroup()
        # 驗證列表、資料庫count數比對
        assert actionGroupList == actionGroupSqlCount
