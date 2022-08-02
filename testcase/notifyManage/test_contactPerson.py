import pytest
from time import sleep
from common import system_tab
from common import countList
from common import connectSQL
from common.connectSQL import searchDB
from common import loadYaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_yaml = loadYaml.loadYaml()


class TestContactPerson(object):
    def test_contactPerson(self, driver):
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
        # 後台首頁點擊通訊錄設定
        system_tab.contactSet(driver)

        # ----------------------- 新增聯絡人 ---------------------------
        # 點擊新增聯絡人
        addContactPersonBtn = driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateContactPersonModal()']")
        addContactPersonBtn.click()

        sleep(1)

        # 新增聯絡人視窗輸入名字
        addContactPersonName = driver.find_element(By.CSS_SELECTOR, "[ng-model='contactPersonModel.name']")
        addContactPersonName.send_keys(load_yaml['ContactPerson']['name'])
        # 新增聯絡人視窗輸入電話
        addContactPersonTel = driver.find_element(By.CSS_SELECTOR, "[ng-model='contactPersonModel.phone']")
        addContactPersonTel.send_keys(load_yaml['ContactPerson']['phone'])
        # 新增聯絡人視窗輸入信箱
        addContactPersonMail = driver.find_element(By.CSS_SELECTOR, "[ng-model='contactPersonModel.email']")
        addContactPersonMail.send_keys(load_yaml['ContactPerson']['email'])
        # 新增聯絡人視窗輸入備註
        addContactPersonNote = driver.find_element(By.CSS_SELECTOR, "[ng-model='contactPersonModel.description']")
        addContactPersonNote.send_keys(load_yaml['ContactPerson']['note'])
        # 新增聯絡人視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 新增後取得當前聯絡人列表count
        contactPersonList = countList.contactPersonInList(driver)

        sleep(1)

        contactPersonSqlCount = searchDB.contactPerson()
        assert contactPersonList == contactPersonSqlCount

        # ----------------------- 新增群組 ---------------------------
        # 點擊新增群組
        addContactGroupBtn = driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateContactPersonGroupModal()']")
        addContactGroupBtn.click()

        sleep(1)

        # 新增群組視窗輸入群組名字
        addContactGroupName = driver.find_element(By.CSS_SELECTOR, "[ng-model='contactPersonGroupModel.name']")
        addContactGroupName.send_keys(load_yaml['ContactGroup']['name'])

        sleep(1)

        # 新增聯絡人群組視窗確定按鈕
        addContactConfirm = driver.find_element(By.XPATH,
                                                "//*[@id='CreateEditContactPersonGroupModal']/div/div/div[3]/button[2]")
        addContactConfirm.click()

        sleep(1)

        # 新增後取得當前群組列表count
        contactPersonGroupList = countList.contactPersonGroupInGroupList(driver)

        sleep(1)

        contactPersonGroupSqlCount = searchDB.contactPersonGroup()
        assert contactPersonGroupList == contactPersonGroupSqlCount

        # ----------------------- 編輯群組 ---------------------------
        # 點擊群組列表第一項編輯群組
        driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[1]/div/div[2]/ul/li[2]/button[2]").click()

        sleep(1)

        # 清除文字
        addContactGroupName.clear()
        # 編輯群組視窗輸入群組名字
        addContactGroupName.send_keys(load_yaml['ContactGroup']['new_name'])
        # 新增群組群組視窗確定按鈕
        addContactConfirm.click()

        sleep(1)

        # 編輯群組後 驗證群組列表第一項項目名字
        addGroupNameOne = driver.find_element_by_xpath(
            "//*[@id='PageContainer']/div[2]/div[1]/div/div[2]/ul/li[2]/a/span")
        assert addGroupNameOne.text == load_yaml['ContactGroup']['new_name']

        # ----------------------- 群組加入聯絡人 ---------------------------
        # 點擊群組列表第一項聯絡人
        driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[1]/div/div[2]/ul/li[2]/button[3]").click()

        sleep(1)

        # 點擊聯絡人 加入群組
        for i in range(3):
            sleep(1)
            driver.find_element_by_xpath("//*[@id='EditPersonsInGroupTable']/div[2]/table/tbody/tr[2]").click()

        # 點擊X關閉修改群組聯絡人視窗
        driver.find_element(By.XPATH, "//*[@id='EditPersonsInContactPersonGroupModal']/div/div/div[1]/button").click()

        sleep(1)

        # 獲取聯絡人群組之聯絡人列表count數進行count數驗證
        groupPersonList = countList.contactPersonInList(driver)
        assert groupPersonList == 3

        # ----------------------- 搜尋群組 ---------------------------
        # 搜尋群組名稱
        groupSearch = driver.find_element(By.CSS_SELECTOR, "[ng-change='searchContactPersonGroupList()']")
        # 輸入"contactGroupEdit"
        groupSearch.send_keys(load_yaml['ContactGroup']['new_name'])

        sleep(1)

        # 輸入的關鍵字搜尋後返回列表count驗證count數
        groupList = countList.contactPersonGroupInGroupList(driver)
        assert groupList == 1

        # 刪除搜尋文字
        groupSearch.clear()

        # ----------------------- 刪除群組 ---------------------------
        # 刪除群組
        # 點擊群組右邊功能"X"刪除按鈕
        driver.find_element(By.XPATH, "//*[@id='PageContainer']/div[2]/div[1]/div/div[2]/ul/li[2]/button[1]").click()

        sleep(1)

        # 點擊刪除群組視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # ----------------------- 編輯聯絡人 ---------------------------
        # 點擊編輯按鈕
        driver.find_element(By.XPATH, "//*[@id='contactPersonTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]").click()

        sleep(1)
        # 修改姓名欄位
        addContactPersonName.clear()
        addContactPersonName.send_keys(load_yaml['ContactPerson']['new_name'])

        # 新增聯絡人視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        contactPersonNameOne = driver.find_element(By.XPATH,
                                                   "//*[@id='contactPersonTable']/div[2]/table/tbody/tr[2]/td[2]")
        assert contactPersonNameOne.text == load_yaml['ContactPerson']['new_name']

        # ----------------------- 刪除聯絡人 ---------------------------
        # 點擊創建之聯絡人刪除按鈕
        contactPersonDel = driver.find_element_by_xpath(
            "//*[@id='contactPersonTable']/div[2]/table/tbody/tr[2]/td[8]/button[3]")
        contactPersonDel.click()

        sleep(1)

        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 獲取通訊錄設定聯絡人列表count數進行count數驗證
        contactPersonList = countList.contactPersonInList(driver)

        sleep(1)

        contactPersonSqlCount = searchDB.contactPerson()
        assert contactPersonList == contactPersonSqlCount

        sleep(1)
