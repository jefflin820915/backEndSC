import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common import system_tab
from common import creatAccountManage
from common import menu_rightSideBar
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestAccountManage(object):
    def test_normalManager(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # ------------------ 新增 一般管理員 ----------------------
        # 創建一個一般管理員帳號
        # 帳號管理
        # 登入
        system_tab.login(driver)

        # 首頁菜單 帳號管理
        system_tab.accountManage(driver)

        # 點擊新增帳號按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateAccountModal()']").click()

        # 創建一般管理員帳號
        creatAccountManage.creatNormalManager(driver)

        sleep(1)
        # 取列表count數
        accountManageList = countList.accountInAccountList(driver)
        sleep(1)
        # 取資料庫count數
        accountManageSqlCount = searchDB.accountManage()
        # 驗證比對列表、資料庫count數
        assert accountManageList == accountManageSqlCount

        sleep(1)

        # 複製驗證碼
        # 點擊開通圖示
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[5]/button").click()
        sleep(1)

        # 拿取驗證碼文字
        accountTokenTxt = driver.find_element(By.CSS_SELECTOR, "[class='formarea-content ng-binding']").text

        # 點擊關閉
        driver.find_element(By.CSS_SELECTOR, "[class='modal-close']").click()

        sleep(1)

        # 右上角使用者登出
        system_tab.backendLogout(driver)
        # 登入帳號
        driver.find_element_by_id("loginUserName").send_keys(load_yaml['NormalManager']['account'])
        # 登入密碼
        driver.find_element_by_id("Password").send_keys(load_yaml['NormalManager']['password'])
        # 登入按鈕
        driver.find_element_by_css_selector("[type='submit']").click()

        sleep(1)

        # 輸入舊密碼
        driver.find_element_by_css_selector("[name='OldPassword']").send_keys(load_yaml['NormalManager']['password'])
        # 輸入驗證碼
        driver.find_element_by_css_selector("[name='Token']").send_keys(accountTokenTxt)
        # 輸入新密碼
        driver.find_element_by_css_selector("[name='NewPassword']").send_keys(
            load_yaml['NormalManager']['new_password'])
        # 輸入確認新密碼
        driver.find_element_by_css_selector("[name='ConfirmPassword']").send_keys(
            load_yaml['NormalManager']['new_password'])
        # 點擊確定按鈕
        driver.find_element_by_css_selector("[type='submit']").click()

        sleep(1)

        # 側邊欄登出帳戶
        menu_rightSideBar.logOut(driver)

        sleep(1)

    def test_normalUser(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver
        # ------------------ 一般使用者 ----------------------
        # 創建一個一般使用者帳號，登出後登入創建的帳號查看後台有權限之版面
        # 帳號管理
        # 登入
        system_tab.login(driver)
        # 首頁菜單 帳號管理
        system_tab.accountManage(driver)
        # 點擊新增帳號按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateAccountModal()']").click()
        # 創建一般使用者帳號
        creatAccountManage.creatNormalUser(driver)

        sleep(2)

        # 複製驗證碼
        # 點擊開通圖示
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[5]/button").click()
        sleep(1)

        # 拿取驗證碼文字
        accountTokenTxt = driver.find_element(By.CSS_SELECTOR, "[class='formarea-content ng-binding']").text

        # 點擊關閉
        driver.find_element(By.CSS_SELECTOR, "[class='modal-close']").click()

        sleep(1)

        # 右上角使用者登出
        system_tab.backendLogout(driver)

        # 登入帳號
        driver.find_element_by_id("loginUserName").send_keys(load_yaml['NormalUser']['account'])
        # 登入密碼
        driver.find_element_by_id("Password").send_keys(load_yaml['NormalUser']['password'])
        # 登入按鈕
        driver.find_element_by_css_selector("[type='submit']").click()

        sleep(1)

        # 輸入舊密碼
        driver.find_element_by_css_selector("[name='OldPassword']").send_keys(load_yaml['NormalUser']['password'])
        # 輸入驗證碼
        driver.find_element_by_css_selector("[name='Token']").send_keys(accountTokenTxt)
        # 輸入新密碼
        driver.find_element_by_css_selector("[name='NewPassword']").send_keys(load_yaml['NormalUser']['new_password'])
        # 輸入確認新密碼
        driver.find_element_by_css_selector("[name='ConfirmPassword']").send_keys(
            load_yaml['NormalUser']['new_password'])
        # 點擊確定按鈕
        driver.find_element_by_xpath("//*[@id='ChangeDefaultPasswordModal']/div/div/form/div[3]/button[2]").click()

        sleep(1)

        # 側邊欄登出帳戶
        menu_rightSideBar.logOut(driver)

        sleep(1)

    def test_systemManagerEditDelAcc(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver
        # ------------------ 程式/系統管理員 ----------------------
        # 創建一個系統管理員帳號，登出後登入創建的帳號查看後台有權限之版面
        # 帳號管理
        # 登入
        system_tab.login(driver)
        # 首頁菜單 帳號管理
        system_tab.accountManage(driver)
        # 點擊新增帳號按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateAccountModal()']").click()
        # 創建系統管理員帳號
        creatAccountManage.creatSystemManager(driver)

        sleep(2)

        # 取列表、資料庫 count數驗證比對
        accountManageList = countList.accountInAccountList(driver)

        sleep(1)

        # 取資料庫count數
        accountManageSqlCount = searchDB.accountManage()
        # 驗證比對列表、資料庫count數
        assert accountManageList == accountManageSqlCount

        sleep(1)

        # 複製驗證碼
        # 點擊開通圖示
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[5]/button").click()
        sleep(1)

        # 拿取驗證碼文字
        accountTokenTxt = driver.find_element(By.CSS_SELECTOR, "[class='formarea-content ng-binding']").text

        # 點擊關閉
        driver.find_element(By.CSS_SELECTOR, "[class='modal-close']").click()

        sleep(1)

        # 右上角使用者登出
        system_tab.backendLogout(driver)

        # 登入帳號
        driver.find_element_by_id("loginUserName").send_keys(load_yaml['SystemManager']['account'])
        # 登入密碼
        driver.find_element_by_id("Password").send_keys(load_yaml['SystemManager']['password'])
        # 登入按鈕
        driver.find_element_by_css_selector("[type='submit']").click()

        sleep(1)

        # 輸入舊密碼
        driver.find_element_by_css_selector("[name='OldPassword']").send_keys(load_yaml['SystemManager']['password'])
        # 輸入驗證碼
        driver.find_element_by_css_selector("[name='Token']").send_keys(accountTokenTxt)
        # 輸入新密碼
        driver.find_element_by_css_selector("[name='NewPassword']").send_keys(
            load_yaml['SystemManager']['new_password'])
        # 輸入確認新密碼
        driver.find_element_by_css_selector("[name='ConfirmPassword']").send_keys(
            load_yaml['SystemManager']['new_password'])
        # 點擊確定按鈕
        driver.find_element_by_xpath("//*[@id='ChangeDefaultPasswordModal']/div/div/form/div[3]/button[2]").click()

        sleep(1)

        # 側邊攔 進入後台首頁
        menu_rightSideBar.backEnd(driver)

        sleep(1)

        # 首頁菜單 帳號管理
        system_tab.accountManage(driver)

        sleep(1)

        system_tab.backendLogout(driver)

        sleep(1)

        # ------------------ 編輯、刪除 ----------------------
        # ------------------ 編輯 一般管理員 ----------------------
        # 登入
        system_tab.login(driver)
        # 側邊欄後台首頁
        menu_rightSideBar.backEnd(driver)
        # 首頁 帳號管理
        system_tab.accountManage(driver)

        sleep(1)

        # 點擊編輯按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[4]/td[6]/button[1]").click()
        # 修改姓名
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").clear()
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(
            load_yaml['NormalManager']['new_name'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 姓名欄位
        accNameOne = driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[4]/td[2]")
        # 驗證修改後姓名欄位
        assert accNameOne.text == load_yaml['NormalManager']['new_name']

        # ------------------ 刪除 一般管理員 ----------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[4]/td[6]/button[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # ------------------ 編輯 一般使用者 ----------------------
        # 點擊編輯按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[3]/td[6]/button[1]").click()
        # 修改姓名
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").clear()
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(
            load_yaml['NormalUser']['new_name'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 姓名欄位
        accNameOne = driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[3]/td[2]")
        # 驗證修改後姓名欄位
        assert accNameOne.text == load_yaml['NormalUser']['new_name']

        # ------------------ 刪除 一般使用者 ----------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[3]/td[6]/button[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # ------------------ 編輯 系統管理員 ----------------------
        # 點擊編輯按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[6]/button[1]").click()

        # 修改姓名
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").clear()
        driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(
            load_yaml['SystemManager']['new_name'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 姓名欄位
        accNameOne = driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[2]")
        # 驗證修改後姓名欄位
        assert accNameOne.text == load_yaml['SystemManager']['new_name']

        # ------------------ 刪除 系統管理員 ----------------------
        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='accountDataTable']/div[2]/table/tbody/tr[2]/td[6]/button[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()
        sleep(1)

        # 取列表count數
        accountManageList = countList.accountInAccountList(driver)

        sleep(1)
        # 取資料庫 count數
        accountManageSqlCount = searchDB.accountManage()
        # 驗證列表、資料庫count數比對
        assert accountManageList == accountManageSqlCount
