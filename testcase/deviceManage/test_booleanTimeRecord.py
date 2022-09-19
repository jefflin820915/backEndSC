import pytest
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common import loadYaml
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import getDownLoadedFileName

load_yaml = loadYaml.loadYaml()


class TestBooleanTimeRecord(object):
    def test_booleanTimeRecord(self, driver):
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
        system_tab.booleanTimeRecord(driver)

        sleep(1)

        # ------------------------------ 運轉紀錄 搜尋 --------------------------------- #
        # 點擊起始日
        driver.find_element(By.XPATH,
                            "//*[@id='PageContainer']/div[3]/div[1]/div/div[2]/div/div[1]/div[2]/input").click()

        sleep(1)
        # 點擊選月份
        driver.find_element(By.CSS_SELECTOR, "[data-view='month current']").click()

        sleep(1)
        # 點擊選年分
        driver.find_element(By.CSS_SELECTOR, "[data-view='year current']").click()

        sleep(1)

        # 選擇2022
        driver.find_element(By.XPATH, "//li[contains(.,'2022')]").click()

        sleep(1)

        # 選擇1月
        driver.find_element(By.XPATH, "//li[contains(.,'1月')]").click()

        sleep(1)

        # 選擇1
        driver.find_element(By.XPATH, "//li[text()='1']").click()

        sleep(1)

        # 點擊設備屬性
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openSearchModel()']").click()

        sleep(1)

        # 點擊屬性點位分頁
        driver.find_element(By.CSS_SELECTOR, "[onclick='changeTab(1)']").click()
        # 點擊屬性點位第一項
        driver.find_element(By.ID, "deviceAttribute0").click()

        sleep(1)

        # 點擊屬性點位 關閉按鈕
        driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()

        sleep(1)

        # 點擊送出按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='getOperationRecords()']").click()

        sleep(2)

        # ------------------------------- 搜尋結果頁面 -----------------------------#
        # 點擊查看搜尋結果
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openOperationResult()']").click()

        sleep(1)

        # 驗證查看搜尋結果列表 結果欄位
        searchResult = driver.find_element(By.XPATH, "//*[@id='OperationResultTable']/div/table/tbody/tr[2]/td[2]")
        assert searchResult.text == '查詢成功'

        sleep(1)

        # 點擊查詢結果 關閉按鈕
        driver.find_element(By.XPATH, "//*[@id='OperationResultModel']/div/div/div[1]/button").click()

        sleep(1)

        # ------------------------------- 匯出Excel -------------------------------#
        # 點擊下載
        driver.find_element(By.CSS_SELECTOR, "[class='far fa-file-excel']").click()

        sleep(10)

        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(
            os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                         load_yaml['ExcelDownload']['booleanTimeRecord'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['booleanTimeRecord'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ------------------------------- 匯出ods -------------------------------#
        # 點擊下載
        driver.find_element(By.CSS_SELECTOR, "[class='fa fa-download']").click()

        sleep(10)

        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['OdsDownload']['booleanTimeRecord'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['OdsDownload']['booleanTimeRecord'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)
