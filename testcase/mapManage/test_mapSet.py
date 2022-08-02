import pytest
import os
from common import system_tab
from common import countList
from common import connectSQL
from common.connectSQL import searchDB
from common import getDownLoadedFileName
from common import loadYaml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestMapSet(object):
    def test_mapSet(self, driver):
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
        # 後台首頁平面圖設定
        system_tab.mapSet(driver)

        # ----------------------- 新增圖層 ---------------------------
        # 點擊編輯圖層
        driver.find_element(By.CSS_SELECTOR, "[ng-click='showEditMapFolderModal()']").click()

        sleep(1)

        # 點擊新增圖層
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addMapFolder()']").click()

        # 點擊新圖層名稱欄位
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/input").send_keys(
            load_yaml['NewMap']['name'])
        # 點擊新增圖層完成按鈕
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/button").click()

        sleep(1)

        # 點擊編輯圖層頁確定按鈕
        driver.find_element(By.XPATH, "//*[@id='editMapFolderModal']/div/div/div[3]/button[2]").click()

        sleep(2)

        # 點擊編輯圖層
        driver.find_element(By.CSS_SELECTOR, "[ng-click='showEditMapFolderModal()']").click()

        sleep(1)

        # 取當前編輯圖層頁面圖層count數
        mapFolderList = countList.mapInMapFolderList(driver)

        sleep(1)
        # 取資料庫count數
        mapFolderSqlCount = searchDB.mapFolder()
        # 驗證列表、資料庫count數比對
        assert mapFolderList == mapFolderSqlCount

        sleep(1)

        # ----------------------- 編輯圖層 ---------------------------
        # 點擊圖層編輯按鈕
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[2]/button[1]").click()

        sleep(1)

        # 點擊新圖層名稱欄位 編輯名稱
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/input").send_keys(
            load_yaml['NewMap']['new_name'])
        # 點擊新增圖層完成按鈕
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[3]/div/button").click()

        sleep(1)

        # 驗證修改後圖層名稱
        assert driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[1]").text == load_yaml['NewMap'][
                   'new_name']

        # ----------------------- 新增圖層 - 內圖層 ---------------------------
        # 點擊圖層"+"按鈕 新增內圖層
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[2]/button[2]").click()
        # 修改內圖層名稱
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[2]/li/div[3]/div/input").clear()
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[2]/li/div[3]/div/input").send_keys(
            load_yaml['NewMapInMap']['name'])
        # 點擊內圖層完成按鈕
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[2]/li/div[3]/div/button").click()
        # 驗證內圖層名稱 確認內圖層有新增
        assert driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[2]/li/div[1]").text == load_yaml['NewMapInMap']['name']
        # 點擊編輯圖層 確定按鈕
        driver.find_element_by_xpath("//*[@id='editMapFolderModal']/div/div/div[3]/button[2]").click()

        sleep(2)

        # ----------------------- 新增圖面 ---------------------------
        # 點擊新增圖面
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateMapModal()']").click()

        sleep(1)

        # 點擊第一層圖層選項
        driver.find_element(By.CSS_SELECTOR, "[data-id='firstMapFolder-select']").click()

        sleep(1)

        # 點擊 newMapEditTest 圖層
        driver.find_element_by_id("bs-select-1-8").click()
        # 平面圖名稱輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='modalMap.description']").send_keys(
            load_yaml['MapModal']['name'])

        # 選擇檔案上傳
        # 選取特定目錄下特定檔案
        # todo: 檔案路徑,以解決,剩把路徑設成變數或常數
        uploadMapFile = driver.find_element(By.ID, "uploadMapFile")
        uploadMapFile.send_keys(
            os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, 'file', load_yaml['MapModal']['uploadFile'])))
        sleep(1)

        # 點擊確定
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(2)

        # 進入newMapEditTest圖層
        driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[1]/div/div[2]/ul/li[9]/a").click()

        sleep(2)

        # 取當前圖面列表count數,驗證count
        mapList = countList.mapInMapList(driver)

        sleep(1)
        # 取資料庫count數
        mapsSqlCount = searchDB.maps()
        # 驗證列表、資料庫count數比對
        # 因mapList count在CSS多一個,這裡資料庫撈出來count + 1來驗證
        assert mapList == mapsSqlCount + 1

        # ----------------------- 編輯圖面 ---------------------------
        # 點擊圖面編輯按鈕
        driver.find_element_by_xpath("//*[@id='mapDataTable']/div[2]/table/tbody/tr[2]/td[5]/button[2]").click()

        sleep(1)

        # 抓取上傳檔案欄位文字
        uploadFileTxt = driver.find_element(By.XPATH,
                                            "//*[@id='createEditMapModal']/div/div/div[2]/div/div[7]/div[2]/div/div[1]/div/label")
        # 抓取ng-src的值
        mapPicturePreview = driver.find_element(By.XPATH,
                                                "//*[@id='createEditMapModal']/div/div/div[2]/div/div[7]/div[2]/div/div[3]/div/img")
        mapPicturePreviewSrc = mapPicturePreview.get_attribute("ng-src")
        # 文字互相做比對是否存在文字,驗證圖片預覽圖是否顯示
        assert uploadFileTxt.text in mapPicturePreviewSrc

        sleep(1)

        # 平面圖名稱編輯
        driver.find_element_by_xpath("//*[@id='createEditMapModal']/div/div/div[2]/div/div[5]/div[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='createEditMapModal']/div/div/div[2]/div/div[5]/div[2]/input").send_keys(
            load_yaml['MapModal']['new_name'])
        # 修改頁面確認按鈕
        driver.find_element_by_xpath("//*[@id='createEditMapModal']/div/div/div[3]/button[2]").click()

        sleep(1)

        # 驗證修改後圖面名稱
        assert driver.find_element_by_xpath("//*[@id='mapDataTable']/div[2]/table/tbody/tr[2]/td[2]/span").text == load_yaml['MapModal']['new_name']

        # ----------------------- 刪除圖面 ---------------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='mapDataTable']/div[2]/table/tbody/tr[2]/td[5]/button[3]").click()

        sleep(1)

        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 刪除後取當前圖面列表count數,驗證count
        mapList = countList.mapInMapList(driver)

        sleep(1)
        # 取資料庫count數
        mapsSqlCount = searchDB.maps()
        # 驗證列表、資料庫count數比對
        # 因mapList count在CSS多一個,這裡資料庫撈出來count + 1來驗證
        assert mapList == mapsSqlCount + 1

        # ----------------------- 刪除圖層 ---------------------------
        # 點擊編輯圖層按鈕
        driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[1]/div/div[1]/button").click()

        sleep(1)

        # 點擊刪除圖層按鈕
        driver.find_element_by_xpath(
            "//*[@id='editMapFolderModal']/div/div/div[2]/div[2]/ul/li[8]/ul[1]/li/div[2]/button[3]").click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element_by_xpath("//*[@id='editMapFolderModal']/div/div/div[3]/button[2]").click()

        sleep(2)

        # 點擊編輯圖層按鈕
        driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[1]/div/div[1]/button").click()

        sleep(1)

        # 刪除後取當前編輯圖層頁面圖層count數,驗證count
        mapFolderList = countList.mapInMapFolderList(driver)

        sleep(1)
        # 取資料庫count數
        mapFolderSqlCount = searchDB.mapFolder()
        # 驗證列表、資料庫count數比對
        assert mapFolderList == mapFolderSqlCount

        sleep(1)

        # 點擊編輯圖層 確定按鈕
        driver.find_element_by_xpath("//*[@id='editMapFolderModal']/div/div/div[3]/button[2]").click()

        sleep(2)

        # ----------------------- 匯出圖面 ---------------------------
        # 點擊匯出圖面按鈕
        driver.find_element(By.CSS_SELECTOR, "[class='fas fa-download']").click()

        sleep(1)

        # 點擊下載
        driver.find_element(By.CSS_SELECTOR, "[class='fa fa-cloud-download-alt']").click()

        sleep(2)

        # todo:位置解決, 把路徑設成變數或常數
        # 取得瀏覽器下載頁面下載之檔案名稱
        file_name = getDownLoadedFileName.getDownLoadedFileName(driver, 5)
        # 取得下載目錄的下載檔案名稱
        folderDataName = os.path.basename(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                         load_yaml['ExcelDownload']['mapSet'])))
        # 驗證瀏覽器下載頁面檔案名稱、下載檔案名稱比對
        assert file_name == folderDataName

        sleep(1)

        # 刪除下載檔案
        os.remove(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'],
                                               load_yaml['ExcelDownload']['mapSet'])))

        sleep(1)

        # 切回原本分頁
        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        # ----------------------- 匯入圖面 ---------------------------
        # 點擊匯入按鈕
        driver.find_element(By.CSS_SELECTOR, "[class='fas fa-upload']").click()

        sleep(1)

        # 匯入圖面檔案
        driver.find_element_by_id("importFile").send_keys(os.path.abspath(
            os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['file'],
                         load_yaml['uploadFile']['mapSet'])))
        # 點擊確定按鈕
        driver.find_element(By.XPATH, "//*[@id='ImportDbModal']/div/div/div[3]/button[2]").click()

        sleep(5)

        # 驗證匯入成功訊息
        assert driver.find_element_by_xpath("/html/body/div[9]/div/div").text == '匯入成功。'
