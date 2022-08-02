import pytest
import os
import datetime
from common import system_tab
from common import countList
from common.connectSQL import searchDB
from common import connectSQL
from common import loadYaml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_yaml = loadYaml.loadYaml()


class TestHolidayManage(object):
    def test_holidayManage(self, driver):
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
        # 後台首頁假日管理
        system_tab.holidayManage(driver)

        # ----------------------- 假日管理日曆 新增標題內容 ---------------------------

        # 點擊日曆
        driver.find_element(By.CSS_SELECTOR,
                            "[class='fc-bg-event fc-event fc-event-start fc-event-end fc-event-today']").click()

        sleep(1)

        # 日曆原因 輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='holidayModel.reason']").send_keys(
            load_yaml['HolidayCalendarContent']['name'])
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='editHoliday()']").click()

        sleep(1)

        # 該日曆內容標題
        holidayCalendarTitle = driver.find_element(By.CSS_SELECTOR,
                                                   "[class='fc-bg-event fc-event fc-event-start fc-event-end fc-event-today']")
        # 驗證內容標題是否為輸入文字
        assert holidayCalendarTitle.text.replace('\n', "") == load_yaml['HolidayCalendarContent']['name']

        sleep(1)

        # ----------------------- 假日管理日曆 清除標題內容 --------------------------- #
        # 點擊日曆
        driver.find_element(By.CSS_SELECTOR,
                            "[class='fc-bg-event fc-event fc-event-start fc-event-end fc-event-today']").click()

        sleep(1)

        # 日曆原因 清除文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='holidayModel.reason']").clear()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='editHoliday()']").click()

        sleep(1)

        # ----------------------- 假日管理 新增國定假日 ---------------------------
        # 點擊國定假日頁面
        driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/NationalHoliday']").click()

        sleep(1)

        # 點擊新增按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='openCreateNationalHolidayModal()']").click()

        sleep(1)

        # 名稱欄位輸入文字
        driver.find_element(By.CSS_SELECTOR, "[ng-model='nationalHolidayModel.name']").send_keys(
            load_yaml['NationalHoliday']['name'])
        # 確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()

        sleep(1)

        # 取列表、資料庫 count數驗證比對
        nationalHolidayList = countList.nationalInHolidayList(driver)

        sleep(1)

        nationalHolidaySqlCount = searchDB.nationalHoliday()
        assert nationalHolidayList == nationalHolidaySqlCount

        sleep(1)

        # ----------------------- 假日管理 修改國定假日 ---------------------------
        # 點擊修改
        driver.find_element_by_xpath("//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[5]/button[1]").click()

        sleep(1)

        # 修改名稱欄位
        driver.find_element(By.CSS_SELECTOR, "[ng-model='nationalHolidayModel.name']").clear()
        driver.find_element(By.CSS_SELECTOR, "[ng-model='nationalHolidayModel.name']").send_keys(
            load_yaml['NationalHoliday']['new_name'])

        # 點擊確定按鈕
        driver.find_element_by_xpath("//*[@id='CreateEditNationalHolidayModal']/div/div/div[3]/button[2]").click()

        sleep(1)

        nationHolidayNameOne = driver.find_element_by_xpath(
            "//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[2]/span")
        assert nationHolidayNameOne.text == load_yaml['NationalHoliday']['new_name']

        sleep(1)

        # ----------------------- 假日管理 刪除國定假日 ---------------------------

        # 點擊刪除按鈕
        driver.find_element_by_xpath("//*[@id='manageTable']/div[2]/table/tbody/tr[2]/td[5]/button[2]").click()
        # 點擊確定按鈕
        driver.find_element(By.CSS_SELECTOR, "[ng-click='makeSure()']").click()

        sleep(1)

        # 取列表、資料庫 count數驗證比對
        nationalHolidayList = countList.nationalInHolidayList(driver)

        sleep(1)

        nationalHolidaySqlCount = searchDB.nationalHoliday()
        assert nationalHolidayList == nationalHolidaySqlCount

        sleep(1)
