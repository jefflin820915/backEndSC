import pytest
import os
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestRegularWork(object):
    def test_regularWork(self, driver):
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
        # 後台首頁 定期工作 定期工作設定
        system_tab.regularWorkSet(driver)

        # ----------------------- 新增定期工作設定 ---------------------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateRegularWorkModal()']").click()

        sleep(1)

        # 標題 輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='regularWorkModel.title']").send_keys(
            load_yaml['RegularWork']['name'])
        # 工作內容 輸入文字
        driver.find_element(By.CLASS_NAME, "ke-edit-iframe").send_keys(load_yaml['RegularWork']['workcontent'])

        # 時間列表 新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddRegularWorkTimeArea()']").click()

        sleep(1)

        # 預設每日 確定後 將每日創建於時間列表
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='saveRegularWorkTime()']").click()

        sleep(1)

        # 時間列表 時間列表 新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddRegularWorkTimeArea()']").click()

        sleep(1)

        # 點擊 每週
        driver.find_element_by_xpath(
            "//*[@id='CreateEditRegularWorkModal']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div/label[2]/input").click()
        # 選擇 禮拜三
        driver.find_element_by_xpath(
            "//*[@id='CreateEditRegularWorkModal']/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/label[3]/input").click()
        # 點擊時間列表確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='saveRegularWorkTime()']").click()
        # 時間列表 新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openAddRegularWorkTimeArea()']").click()

        sleep(1)

        # 點擊 每月
        driver.find_element_by_xpath(
            "//*[@id='CreateEditRegularWorkModal']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div/label[3]/input").click()
        # 選擇 01
        driver.find_element_by_xpath(
            "//*[@id='CreateEditRegularWorkModal']/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div/label[1]/input").click()
        # 點擊時間列表確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='saveRegularWorkTime()']").click()
        # 點擊 新增定期工作 確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        regularWorkList = countList.regularWorkSet(driver)

        sleep(1)

        regularWorkSqlCount = searchDB.regularWorkSet()
        # 驗證count
        assert regularWorkList == regularWorkSqlCount

        # ----------------------- 編輯定期工作設定 ---------------------------

        # 點擊 編輯按鈕
        driver.find_element_by_xpath("//*[@id='RegularWorkTable']/div[2]/table/tbody/tr[2]/td[4]/button[2]").click()

        sleep(1)

        driver.find_element(By.CSS_SELECTOR, "[ng-model='regularWorkModel.title']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='regularWorkModel.title']").send_keys(
            load_yaml['RegularWork']['new_name'])

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 第一項定期工作名稱
        regularWorkOneName = driver.find_element_by_xpath("//*[@id='RegularWorkTable']/div[2]/table/tbody/tr[2]/td[2]")
        assert regularWorkOneName.text == load_yaml['RegularWork']['new_name']

        # ----------------------- 定期工作設定  內容 ---------------------------
        # 點擊 內容按鈕
        driver.find_element_by_xpath("//*[@id='RegularWorkTable']/div[2]/table/tbody/tr[2]/td[4]/button[1]").click()

        sleep(1)

        regularWorkOneContent = driver.find_element(By.CLASS_NAME, "content")
        assert regularWorkOneContent.text == load_yaml['RegularWork']['workcontent']

        # 點擊 內容彈窗取消按鈕
        driver.find_element_by_xpath("//*[@id='RegularWorkContentDetailModal']/div/div/div[3]/button").click()

        # ----------------------- 刪除定期工作設定 ---------------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='RegularWorkTable']/div[2]/table/tbody/tr[2]/td[4]/button[3]").click()

        sleep(1)

        # 點擊 刪除彈窗 確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        regularWorkList = countList.regularWorkSet(driver)

        sleep(1)

        regularWorkSqlCount = searchDB.regularWorkSet()
        # 驗證count
        assert regularWorkList == regularWorkSqlCount

        sleep(1)
