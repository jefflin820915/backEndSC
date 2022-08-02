from time import sleep
from selenium.webdriver.common.by import By
import pytest

# 子系統資訊 子系統列表
def subsystemInSubsystemList(driver):
    subSysList = driver.find_elements_by_css_selector("[ng-repeat='subsystem in subsystemList']")
    subSysListLen = len(subSysList)
    return subSysListLen

# 設備資訊 設備列表
def deviceInDeviceList(driver):
    deviceList = driver.find_elements_by_css_selector("[ng-repeat='device in deviceList']")
    deviceListLen = len(deviceList)
    return deviceListLen

# 通訊錄設定 聯絡人列表
def contactPersonInList(driver):
    contactList = driver.find_elements_by_css_selector("[ng-repeat='contactPerson in contactPersonList']")
    contactPersonListLen = len(contactList)
    return contactPersonListLen

# 通訊錄設定 群組列表
def contactPersonGroupInGroupList(driver):
    groupList = driver.find_elements_by_css_selector("[ng-repeat='contactPersonGroup in contactPersonGroupList']")
    groupListLen = len(groupList)
    return groupListLen

# 通知事件設定 通知事件列表
def notifyEvent(driver):
    notificationList = driver.find_elements_by_css_selector("[ng-repeat='notification in notificationList']")
    notificationListLen = len(notificationList)
    return notificationListLen

# 事件設定 設備事件列表
def eventInSubsystemEvents(driver):
    deviceEventList = driver.find_elements_by_css_selector("[ng-repeat='event in subsystemEvents']")
    deviceEventListLen = len(deviceEventList)
    return deviceEventListLen

# 事件設定 數值事件列表
def eventInCustomEvents(driver):
    valueEventList = driver.find_elements_by_css_selector("[ng-repeat='event in customEvents']")
    valueEventListLen = len(valueEventList)
    return valueEventListLen

# 事件設定 複合式條件事件列表
def customMultipleEvents(driver):
    customMultipleEventList = driver.find_elements_by_css_selector("[ng-repeat='event in customMultipleEvents']")
    customMultipleEventListLen = len(customMultipleEventList)
    return customMultipleEventListLen

# 連動設定 連動列表
def interaction(driver):
    interactionList = driver.find_elements_by_css_selector("[ng-repeat='interaction in interactionList']")
    interactionListLen = len(interactionList)
    return interactionListLen

# 動作群組 動作群組列表
def actionGroup(driver):
    actionGroupList = driver.find_elements_by_css_selector("[ng-repeat='actionGroup in actionGroupList']")
    actionGroupListLen = len(actionGroupList)
    return actionGroupListLen

# 設備管理 運轉時數列表
def booleanTimeInBooleanTimeList(driver):
    booleanTimeList = driver.find_elements_by_css_selector("[ng-repeat='booleanTime in booleanTimeList']")
    booleanTimeListLen = len(booleanTimeList)
    return booleanTimeListLen

# 平面圖設定 編輯圖層頁面列表
def mapInMapFolderList(driver):
    mapFolderList = driver.find_elements_by_css_selector("[ng-repeat='(mapIndex, mapFolder) in mapFolderList']")
    mapFolderListLen = len(mapFolderList)
    return mapFolderListLen

# 平面圖設定 圖面列表
def mapInMapList(driver):
    mapList = driver.find_elements_by_css_selector("[ng-repeat='map in mapList']")
    mapListLen = len(mapList)
    return mapListLen

# 事件類別 事件類別列表
def eventCategoryList(driver):
    eventCategoryList = driver.find_elements_by_css_selector("[ng-repeat='eventType in eventTypes']")
    eventCategoryListLen = len(eventCategoryList)
    return eventCategoryListLen

# 連動管理 連動時間排程
def scheduleInScheduleList(driver):
    scheduleList = driver.find_elements_by_css_selector("[ng-repeat='schedule in scheduleList']")
    scheduleListLen = len(scheduleList)
    return scheduleListLen

# 定期工作設定 定期工作列表
def regularWorkSet(driver):
    regularWorkList = driver.find_elements_by_css_selector("[ng-repeat='regularWork in regularWorkList']")
    regularWorkListLen = len(regularWorkList)
    return regularWorkListLen

# 假日管理 國定假日列表
def nationalInHolidayList(driver):
    nationalHolidayList = driver.find_elements_by_css_selector("[ng-repeat='nationalHoliday in nationalHolidayList']")
    nationalHolidayListLen = len(nationalHolidayList)
    return nationalHolidayListLen

# 相關檔案 檔案列表
def downloadFileInSubDownloadFileList(driver):
    relevantFileList = driver.find_elements_by_css_selector("[ng-repeat='downloadFile in subDownloadFileList']")
    relevantFileListLen = len(relevantFileList)
    return relevantFileListLen

# 相關連結 連結列表
def otherLinkInOtherLinkList(driver):
    relevantLinkList = driver.find_elements_by_css_selector("[ng-repeat='otherLink in otherLinkList']")
    relevantLinkListLen = len(relevantLinkList)
    return relevantLinkListLen

# 帳號管理 帳號列表
def accountInAccountList(driver):
    accountManageList = driver.find_elements_by_css_selector("[ng-repeat='account in accountList']")
    accountManageListLen = len(accountManageList)
    return accountManageListLen