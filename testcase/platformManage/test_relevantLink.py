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


class TestRelevantLink(object):
    def test_relevantLink(self, driver):
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
        # 後台首頁 相關檔案
        system_tab.relevantLink(driver)
        # 點擊相關連結
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/OtherLink']").click()

        # ----------------------- 新增 相關連結  ---------------------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateOtherLinkModal()']").click()

        sleep(1)

        # 填入名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='otherLinkModel.name']").send_keys(
            load_yaml['RelevantLinkAdd']['name'])
        # 填入網址
        driver.find_element(By.CSS_SELECTOR, "[ng-model='otherLinkModel.url']").send_keys(
            load_yaml['WebsiteURL']['google'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 取列表、資料庫 count數驗證比對
        relevantLinkList = countList.otherLinkInOtherLinkList(driver)

        sleep(1)

        relevantLinkSqlCount = searchDB.relevantLink()
        assert relevantLinkList == relevantLinkSqlCount

        # ----------------------- 編輯 相關連結  ---------------------------
        # 點擊修改按鈕
        driver.find_element_by_xpath("//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[4]/button[1]").click()

        sleep(1)

        # 修改名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='otherLinkModel.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='otherLinkModel.name']").send_keys(
            load_yaml['RelevantLinkAdd']['new_name'])

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 驗證修改後名稱
        relevantLinkNameOne = driver.find_element_by_xpath("//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        assert relevantLinkNameOne.text == load_yaml['RelevantLinkAdd']['new_name']

        # ----------------------- 刪除 相關連結  ---------------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[4]/button[2]").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 取列表、資料庫 count數驗證比對
        relevantLinkList = countList.otherLinkInOtherLinkList(driver)

        sleep(1)

        relevantLinkSqlCount = searchDB.relevantLink()
        assert relevantLinkList == relevantLinkSqlCount

        sleep(1)

        connectSQL.sqlClose()
        sleep(1)
