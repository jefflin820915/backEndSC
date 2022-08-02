import pytest
from time import sleep
from selenium.webdriver.common.by import By
from common import loadYaml

LOAD_YAML = loadYaml.loadYaml()

def login(driver):
    # 登入
    # 帳號
    driver.find_element_by_id("loginUserName").send_keys(LOAD_YAML['Login']['account'])
    # 密碼
    driver.find_element_by_id("Password").send_keys(LOAD_YAML['Login']['password'])
    # 登入按鈕
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

def backendLogout(driver):
    # 後台登出
    driver.find_element_by_css_selector("[class='dropdown']").click()
    driver.find_element_by_css_selector("[onclick='logout()']").click()

def accountManage(driver):
    # 首頁菜單 帳號管理
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Account']").click()
    sleep(2)

def userLog(driver):
    # 首頁菜單 使用者日誌
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Account/UserLog']").click()
    sleep(2)

def subSystemInformation(driver):
    # 首頁菜單 子系統資訊
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Device/Subsystem']").click()
    sleep(2)

def devicesInformation(driver):
    # 首頁菜單 設備資訊
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Device']").click()
    sleep(2)

def eventCategory(driver):
    # 首頁菜單 事件類別
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/EventType']").click()
    sleep(2)

def eventRecord(driver):
    # 首頁菜單 事件紀錄
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/EventRecord']").click()
    sleep(2)

def contactSet(driver):
    # 首頁菜單 通訊錄設定
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification']").click()
    sleep(2)

def actionGroup(driver):
    # 首頁菜單 動作群組
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Interaction/ActionGroup']").click()
    sleep(2)

def deviceNotifyEvent(driver):
    # 首頁菜單 通知事件設定 - 設備事件通知
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[3]/div/div/li[2]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification/EventNotification?type=0']").click()
    sleep(1)

def valueNotifyEvent(driver):
    # 首頁菜單 通知事件設定 - 數值事件通知
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[3]/div/div/li[2]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification/EventNotification?type=1']").click()
    sleep(1)

def customMultipleEvent(driver):
    # 首頁菜單 通知事件設定 - 複合式條件事件通知
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[3]/div/div/li[2]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Notification/EventNotification?type=2']").click()
    sleep(1)

def deviceEvent(driver):
    # 首頁菜單 事件設定 - 設備事件
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[4]/div/div/li[1]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/DeviceEvent']").click()
    sleep(1)

def valueEvent(driver):
    # 首頁菜單 事件設定 - 數值事件
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[4]/div/div/li[1]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/CustomEvent']").click()
    sleep(1)

def customMultipleEvent(driver):
    # 首頁菜單 事件設定 - 複合式條件事件
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[4]/div/div/li[1]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Event/CustomMultipleEvent']").click()
    sleep(1)

def interaction(driver):
    # 首頁菜單 連動設定
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Interaction']").click()
    sleep(1)

def booleanTime(driver):
    # 首頁菜單 運轉時數設定
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Device/BooleanTime']").click()
    sleep(1)

def booleanTimeRecord(driver):
    # 首頁菜單 運轉紀錄
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Device/OperationRecord']").click()
    sleep(1)

def mapSet(driver):
    # 首頁菜單 平面圖設定
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Map']").click()
    sleep(1)

def interactionSchedule(driver):
    # 首頁菜單 連動時間排程
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Interaction/Schedule']").click()
    sleep(1)

def mapDevice(driver):
    # 首頁菜單 平面圖設備設定
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Map/DevicePosition']").click()
    sleep(1)

def regularWorkSet(driver):
    # 首頁菜單 定期工作 定期工作設定
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[7]/div[1]/div[1]/li[2]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/RegularWorkSetting']").click()
    sleep(1)

def holidayManage(driver):
    # 假日管理 假日管理
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul[7]/div[1]/div[1]/li[3]/a").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/Holiday']").click()
    sleep(1)

def relevantFile(driver):
    # 平台管理 相關檔案
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/DownloadFile']").click()
    sleep(1)

def relevantLink(driver):
    # 平台管理 相關連結
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/DownloadFile']").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[href='/Manage/Platform/OtherLink']").click()
    sleep(1)


def tr_td(tr):
    list1 = []
    for i in tr:
        # 定位td整個元素
        td = i.find_elements_by_tag_name("td")
        # 遍歷td元素list,拿取td里全部資料, 放進空list裡
        for item in td:
            text = item.text
            list1.append(text)
    return list1