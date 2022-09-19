import pytest
import os
from selenium.webdriver.common.by import By
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import getDownLoadedFileName
from common import connectSQL
from time import sleep


class TestDevicesInformation(object):
    def test_devicesInformation(self, driver):
        """
        @type driver: selenium.webdriver.remote.webdriver.WebDriver
        @:type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return:
        """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # 調用登入方法，進入後台
        system_tab.login(driver)
        # 後台首頁點擊設備資訊
        system_tab.devicesInformation(driver)

        # ------------------------- 只篩選子系統 -------------------------
        # 點擊子系統篩選
        driver.find_element(By.CSS_SELECTOR, "[data-id='subsystemList']").click()

        sleep(1)

        # ------------------- 電力系統 -------------------
        # 點擊第二個選項, 電力系統
        driver.find_element(By.XPATH, "//li[contains(.,'電力系統')]").click()

        sleep(1)

        # 拿取設備列表頁的count數
        deviceList = countList.deviceInDeviceList(driver)

        sleep(1)
        # 取資料庫count數
        onlySubsystemSqlCount = searchDB.deviceInformationOnlySub()
        # 驗證列表、資料庫count數比對
        assert deviceList == onlySubsystemSqlCount

        sleep(1)

        # 點擊子系統篩選
        driver.find_element(By.CSS_SELECTOR, "[data-id='subsystemList']").click()

        sleep(1)

        # 選擇全部
        driver.find_element(By.XPATH, "//li[contains(.,'全部')]").click()

        sleep(1)

        # ------------------------- 只篩選設備類別 -------------------------

        # 點擊設備類別篩選
        driver.find_element(By.CSS_SELECTOR, "[data-id='deviceTypeList']").click()
        # 點擊第二個選項, PTZ攝影機
        driver.find_element(By.XPATH, "//li[contains(.,'PTZ攝影機')]").click()

        sleep(1)

        # 拿取設備列表頁的count
        deviceList = countList.deviceInDeviceList(driver)

        sleep(1)
        # 取資料庫count數
        onlyCategorySqlCount = searchDB.deviceInformationOnlyCategory()
        # 驗證列表、資料庫count數比對
        assert deviceList == onlyCategorySqlCount

        sleep(1)
        # ------------------------- 子系統以及設備類別都篩選一種和輸入關鍵字搜尋 -------------------------

        # 點擊子系統篩選
        driver.find_element(By.CSS_SELECTOR, "[data-id='subsystemList']").click()
        # 點擊第三個選項, 監視系統
        driver.find_element(By.XPATH, "//li[contains(.,'監視系統')]").click()
        sleep(2)
        # 點擊設備類別篩選
        driver.find_element(By.CSS_SELECTOR, "[data-id='deviceTypeList']").click()
        # 點擊第二個選項, 球型攝影機
        driver.find_element(By.XPATH, "//li[contains(.,'球型攝影機')]").click()

        sleep(2)

        # 輸入VIP到搜尋關鍵字欄位
        keyWords = driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']")
        keyWords.send_keys('SC')

        sleep(2)

        # 拿取設備列表頁的count
        deviceList = countList.deviceInDeviceList(driver)

        sleep(1)
        # 拿取資料庫count數
        allSearchSqlCount = searchDB.deviceInformationAll()
        # 驗證列表、資料庫count數比對
        assert deviceList == allSearchSqlCount

        sleep(1)

        # ------------------------- 匯出設備資訊excel -------------------------
        # 點擊匯出Excel按鈕
        driver.find_element(By.CSS_SELECTOR, "[class='far fa-file-excel']").click()

        sleep(5)

        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['ExcelDownload']['devicesInformation'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['devicesInformation'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ------------------------------- 匯出ods -------------------------------#
        # 點擊下載
        driver.find_element(By.CSS_SELECTOR, "[class='fa fa-download']").click()

        sleep(5)

        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['OdsDownload']['devicesInformation'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['OdsDownload']['devicesInformation'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)
