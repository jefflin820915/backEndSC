import pytest
import os
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import getDownLoadedFileName
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestMapDevice(object):
    def test_mapDevice(self, driver):
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
        # 後台首頁平面圖設備設定
        system_tab.mapDevice(driver)

        # ----------------------- 匯出資料庫 ---------------------------
        # 點擊匯出資料庫按鈕
        driver.find_element(By.CLASS_NAME, "fas fa-download").click()

        sleep(1)

        # 點擊下載
        driver.find_element_by_xpath("//*[@id='ExportDbModal']/div/div/div[2]/div/div/div[2]/div/button").click()

        sleep(2)

        # todo:位置解決, 把路徑設成變數或常數
        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['ExcelDownload']['mapDevice'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['mapDevice'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)
