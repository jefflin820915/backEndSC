import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from common import system_tab
from common import loadYaml
from common import countList
from common import getDownLoadedFileName
from common.connectSQL import searchDB
from common import connectSQL
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestUseLog(object):
    def test_userLog(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # 登入
        system_tab.login(driver)
        # 後台首頁點擊事件設定 - 設備事件
        system_tab.userLog(driver)

        sleep(1)

        # ------------------------- 匯出使用者日誌 excel -------------------------
        # 點擊匯出Excel按鈕
        driver.find_element(By.CSS_SELECTOR, "[class='fas fa-file-excel']").click()

        sleep(1)

        # todo:位置解決, 把路徑設成變數或常數
        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['ExcelDownload']['userLog'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['userLog'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ------------------------------- 使用者日誌 ods -------------------------------#
        # 點擊匯出ods按鈕
        driver.find_element(By.CSS_SELECTOR, "[class='fa fa-download']").click()

        sleep(8)

        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(
            os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                         load_yaml['OdsDownload']['userLog'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['OdsDownload']['userLog'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)
