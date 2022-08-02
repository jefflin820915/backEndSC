import pytest
import os
from common import system_tab
from common import countList
from common import getDownLoadedFileName
from common.connectSQL import searchDB
from common import connectSQL
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class TestRelevantFile(object):
    def test_relevantFile(self, driver):
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
        # 後台首頁相關檔案
        system_tab.relevantFile(driver)

        sleep(1)

        relevantFileList = countList.downloadFileInSubDownloadFileList(driver)

        sleep(1)

        # ----------------------- 相關檔案 上傳檔案 ---------------------------

        # 點擊 新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openUploadModal()']").click()

        sleep(1)

        # 選擇檔案上傳
        # 選取特定目錄下特定檔案
        # todo: 檔案路徑,以解決,剩把路徑設成變數或常數
        driver.find_element_by_id("uploadFile").send_keys(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['file'],
                         load_yaml['uploadFile']['relevantFile'])))

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='uploadFile()']").click()

        sleep(1)

        relevantFileAddList = countList.downloadFileInSubDownloadFileList(driver)

        sleep(1)

        assert relevantFileAddList == relevantFileList + 1

        # ----------------------- 相關檔案 下載檔案 ---------------------------

        # 點擊 下載按鈕
        driver.find_element_by_xpath("//*[@id='DownloadFileTable']/div[2]/table/tbody/tr[2]/td[3]/button[1]").click()

        sleep(2)

        # todo:位置解決, 把路徑設成變數或常數
        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['ExcelDownload']['relevantFile'])))
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['relevantFile'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ----------------------- 相關檔案 刪除檔案 ---------------------------

        #  點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='DownloadFileTable']/div[2]/table/tbody/tr[2]/td[3]/button[2]").click()

        sleep(1)

        # 點擊確定
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        relevantFileDelList = countList.downloadFileInSubDownloadFileList(driver)

        sleep(1)

        assert relevantFileDelList == relevantFileList
