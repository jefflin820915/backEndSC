import pytest
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestInteractionSchedule(object):
    def test_interactionSchedule(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # ----------------------------------- 連動時間排程設定 ---------------------------------------
        # 登入
        system_tab.login(driver)
        # 後台首頁點擊連動時間排程設定
        system_tab.interactionSchedule(driver)

        sleep(1)

        # --------------- 新增連動時間排程 -----------------
        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateScheduleModal()']").click()
        # 輸入時間排程名稱
        driver.find_element(By.CSS_SELECTOR, "[ng-model='scheduleModel.name']").send_keys(
            load_yaml['InteractionSchedule']['name'])
        # 點擊觸發動作,展開動作列表
        driver.find_element(By.CSS_SELECTOR, "[ng-click='changeEditActionGroupArea()']").click()
        # 點擊動作列表第一項
        driver.find_element_by_xpath("//*[@id='ActionGroupListTable']/div[2]/table/tbody/tr[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)
        # 取連動時間排程列表count數
        scheduleList = countList.scheduleInScheduleList(driver)

        sleep(1)
        # 取資料庫count數
        scheduleSqlCount = searchDB.interactionSchedule()
        # 驗證列表、資料庫count數比對
        assert scheduleList == scheduleSqlCount

        # --------------- 搜尋連動時間排程 -----------------
        # 文字搜尋框輸入關鍵字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").send_keys("InteractionScheduleAdd")

        sleep(1)

        # 拿取搜尋後連動時間排程count數驗證
        scheduleList = countList.scheduleInScheduleList(driver)
        assert scheduleList == 1

        # 清除搜尋框文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='pageModel.searchString']").clear()

        sleep(1)

        # --------------- 編輯連動時間排程 -----------------
        # 點擊功能區編輯按鈕
        driver.find_element_by_xpath("//*[@id='ScheduleTable']/div[2]/table/tbody/tr[2]/td[6]/button[1]").click()

        sleep(1)

        # 更改名稱欄位
        driver.find_element(By.CSS_SELECTOR, "[ng-model='scheduleModel.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='scheduleModel.name']").send_keys(
            load_yaml['InteractionSchedule']['new_name'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)
        # 取編輯後連動時間排程列表名稱文字
        scheduleOneName = driver.find_element_by_xpath("//*[@id='ScheduleTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        # 驗證是否為修改後文字
        assert scheduleOneName.text == load_yaml['InteractionSchedule']['new_name']

        # --------------- 刪除連動時間排程 -----------------
        # 點擊功能區刪除按鈕
        driver.find_element_by_xpath("//*[@id='ScheduleTable']/div[2]/table/tbody/tr[2]/td[6]/button[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)
        # 取連動時間排程列表count數
        scheduleList = countList.scheduleInScheduleList(driver)

        sleep(1)
        # 取資料庫count數
        scheduleSqlCount = searchDB.interactionSchedule()
        # 驗證列表、資料庫count數比對
        assert scheduleList == scheduleSqlCount

        sleep(1)
