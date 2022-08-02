import pytest
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestEventNotify(object):
    def test_eventNotify(self, driver):
        """
           @type driver: selenium.webdriver.remote.webdriver.WebDriver
           @:type driver: selenium.webdriver.remote.webdriver.WebDriver
           :return:
           """
        # @:type driver: selenium.webdriver.remote.webdriver
        # @type driver: selenium.webdriver.remote.webdriver.WebDriver
        # @:type driver: selenium.webdriver.remote.webdriver.WebDriver

        # ----------------------------------- 設備事件通知 ---------------------------------------

        # ------------------ 新增設備事件通知 ----------------------
        # 登入
        system_tab.login(driver)
        # 後台首頁點擊設備事件通知
        system_tab.deviceNotifyEvent(driver)

        # 點擊新增設備事件通知
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openEventNotificationModal(0)']").click()

        sleep(1)

        # 勾選notificationEvent_29
        driver.find_element_by_id("notificationEvent_29").click()
        # 勾選notificationEvent_34
        driver.find_element_by_id("notificationEvent_34").click()
        # 勾選notificationEvent_11
        driver.find_element_by_id("notificationEvent_1").click()
        # 輸入文字add至附加訊息
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['DeviceNotifyEvent']['message'])
        # 勾選群組通知 測試部 telegram checkbox
        driver.find_element_by_xpath("//*[@id='contactPersonGroupTable']/div/table/tbody/tr[1]/td[7]/input").click()
        # 勾選群組通知 測試部 App推播 checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[9]/input").click()
        # 勾選個人通知 Line checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[7]/input").click()
        # 點擊新增設備事件通知視窗確定按鈕
        driver.find_element_by_xpath("//*[@id='eventNotificationModal']/div/div/div[3]/button[2]").click()

        sleep(1)

        deviceNotifyList = countList.notifyEvent(driver)

        sleep(1)

        deviceEventNotifySqlCount = searchDB.deviceEventNotify()
        assert deviceNotifyList == deviceEventNotifySqlCount

        # ------------------ 編輯設備事件通知 ----------------------
        # 點擊設備通知列表第一項 編輯按鈕
        deviceListEditOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[1]")
        deviceListEditOne.click()

        sleep(1)
        # 點擊notificationEvent_37  checkbox
        driver.find_element_by_id("notificationEvent_37").click()

        sleep(1)

        # 點擊notificationEvent_50 checkbox
        driver.find_element_by_id("notificationEvent_50").click()

        sleep(1)

        # 修改附加訊息
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['DeviceNotifyEvent']['new_message'])
        # 點擊編輯設備事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventNotifaication()']").click()

        sleep(1)

        deviceListTextOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[5]/span")
        assert deviceListTextOne.text == load_yaml['DeviceNotifyEvent']['new_message']

        sleep(1)

        # ------------------ 刪除設備事件通知 ----------------------
        # 點擊通知列表第一項 刪除按鈕
        deviceListDelOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]")
        deviceListDelOne.click()
        # 刪除事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        deviceNotifyList = countList.notifyEvent(driver)

        sleep(1)

        deviceEventNotifySqlCount = searchDB.deviceEventNotify()
        assert deviceNotifyList == deviceEventNotifySqlCount

        # ----------------------------------- 數值事件通知 ---------------------------------------

        # ------------------ 新增數值事件通知 ----------------------
        # 點擊數值事件通知頁面
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification/EventNotification?type=1']").click()

        sleep(1)

        # 點擊新增數值事件通知
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openEventNotificationModal(0)']").click()

        sleep(1)

        # 勾選notificationEvent_94 checkbox
        driver.find_element_by_id("notificationEvent_94").click()

        sleep(1)

        # 勾選notificationEvent_10093 checkbox
        driver.find_element_by_id("notificationEvent_10093").click()

        sleep(1)

        # 在附加訊息填入文字 test
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['ValueNotifyEvent']['message'])
        # 勾選群組通知 測試部 telegram checkbox
        driver.find_element_by_xpath("//*[@id='contactPersonGroupTable']/div/table/tbody/tr[1]/td[7]/input").click()
        # 勾選群組通知 測試部 App推播 checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[9]/input").click()
        # 勾選個人通知 Line checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[7]/input").click()
        # 點擊新增數值事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventNotifaication()']").click()

        sleep(1)

        ValueNotifyList = countList.notifyEvent(driver)

        sleep(1)

        valueEventNotifySqlCount = searchDB.valueEventNotify()
        assert ValueNotifyList == valueEventNotifySqlCount

        # ------------------ 編輯數值事件通知 ----------------------
        # 點擊數值通知列表第一項 編輯按鈕
        valueListEditOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[1]")
        valueListEditOne.click()

        sleep(1)

        # 勾選notificationEvent_10094 checkbox
        driver.find_element_by_id("notificationEvent_10094").click()

        sleep(1)

        # 勾選 notificationEvent_10097 checkbox
        driver.find_element_by_id("notificationEvent_10097").click()

        sleep(1)

        # 在附加訊息填入文字 test
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['ValueNotifyEvent']['new_message'])
        # 點擊編輯數值事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventNotifaication()']").click()

        sleep(1)

        # 第一項數值事件名稱
        valueListTextOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[5]/span")
        assert valueListTextOne.text == load_yaml['ValueNotifyEvent']['new_message']

        sleep(1)

        # ------------------ 刪除數值事件通知 ----------------------
        # 點擊數值通知列表第一項 刪除按鈕
        valueListDelOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]")
        valueListDelOne.click()
        # 刪除數值事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        valueNotifyList = countList.notifyEvent(driver)

        sleep(1)

        valueEventNotifySqlCount = searchDB.valueEventNotify()
        assert valueNotifyList == valueEventNotifySqlCount

        # ----------------------------------- 複合式條件事件通知 ---------------------------------------
        # ------------------ 新增複合式條件事件通知 ----------------------
        # 點擊複合式條件事件通知頁面
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification/EventNotification?type=2']").click()

        sleep(1)

        # 新增
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openEventNotificationModal(0)']").click()

        sleep(1)

        # 勾選 notificationEvent_81 checkbox
        driver.find_element(By.ID, "notificationEvent_81").click()

        sleep(1)

        # 勾選 notificationEvent_88 checkbox
        driver.find_element(By.ID, "notificationEvent_10095").click()

        sleep(1)

        # 在附加訊息填入文字 test
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['CustomNotifyEvent']['message'])
        # 勾選群組通知 測試部 telegram checkbox
        driver.find_element_by_xpath("//*[@id='contactPersonGroupTable']/div/table/tbody/tr[1]/td[7]/input").click()
        # 勾選群組通知 測試部 App推播 checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[9]/input").click()
        # 勾選個人通知 Line checkbox
        driver.find_element_by_xpath("//*[@id='alreadyAddTable']/div/table/tbody/tr[5]/td[7]/input").click()
        # 點擊新增數值事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventNotifaication()']").click()

        sleep(1)

        customMultipleNotifyList = countList.notifyEvent(driver)

        sleep(1)

        customMultipleEventNotifySqlCount = searchDB.customMultipleEventNotify()
        assert customMultipleNotifyList == customMultipleEventNotifySqlCount

        # ------------------ 編輯複合式條件事件通知 ----------------------
        # 點擊數值通知列表第一項 編輯按鈕
        customMultipleListEditOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[1]")
        customMultipleListEditOne.click()

        sleep(1)

        # 勾選 notificationEvent_68 checkbox
        driver.find_element_by_id("notificationEvent_68").click()

        sleep(1)

        # 勾選 notificationEvent_73 checkbox
        driver.find_element_by_id("notificationEvent_73").click()

        sleep(1)

        # 在附加訊息填入文字 test
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='additionalMessage']").send_keys(
            load_yaml['CustomNotifyEvent']['new_message'])
        # 點擊新增數值事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='addEditEventNotifaication()']").click()

        sleep(1)

        # 第一項複合事件名稱
        customMultipleListTextOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[5]/span")
        assert customMultipleListTextOne.text == load_yaml['CustomNotifyEvent']['new_message']

        sleep(1)

        # ------------------ 刪除複合式條件事件通知 ----------------------
        # 點擊複合式條件通知列表第一項 刪除按鈕
        customMultipleListDelOne = driver.find_element_by_xpath(
            "//*[@id='notificationDataTable']/div[2]/table/tbody/tr[2]/td[8]/button[2]")
        customMultipleListDelOne.click()
        # 刪除複合式條件事件通知視窗確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        customMultipleNotifyList = countList.notifyEvent(driver)

        sleep(1)

        customMultipleEventNotifySqlCount = searchDB.customMultipleEventNotify()
        assert customMultipleNotifyList == customMultipleEventNotifySqlCount

        sleep(1)
