from time import sleep
import pytest

# 前台平面配置圖 右側側邊攔


def pageSideBar(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊右側邊欄收合hamburger - icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-hamburger']").click()

def homePageIcon(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊首頁icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-home']").click()

def airConditioningSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊空調系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-1']").click()

def monitoringSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊監視系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-2']").click()

def fireProtectionSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊消防系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-3']").click()

def plumbingSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊給排水系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-4']").click()

def accessControlSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊門禁系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-6']").click()

def electricalSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊電力系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-7']").click()

def illuminationSystem(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊照明系統icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-8']").click()

def floorPlan(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊平面配置圖icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-12']").click()

def backEnd(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊後台icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-setting']").click()

def logOut(driver):
    # 點擊前台 前往平面配置圖
    driver.find_element_by_css_selector("[onclick='redirectToButtonUrl()']").click()
    sleep(3)
    # 點擊登出icon
    driver.find_element_by_css_selector("[class='link-icon link-icon-sign_out']").click()