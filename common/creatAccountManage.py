from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common import loadYaml
import pytest

load_yaml = loadYaml.loadYaml()


def creatSystemManager(driver):
    # ------------------ 程式/系統管理員 ----------------------

    # 姓名
    # 姓名編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(load_yaml['SystemManager']['name'])
    # 登入帳號
    # 登入帳號欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.loginId']").send_keys(load_yaml['SystemManager']['account'])

    sleep(1)

    # 電話
    # 電話欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.phone']").send_keys(load_yaml['SystemManager']['phone'])

    sleep(1)

    # 信箱
    # 信箱編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.email']").send_keys(load_yaml['SystemManager']['email'])

    sleep(1)

    # 密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").send_keys(load_yaml['SystemManager']['password'])

    sleep(1)

    # 確認密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").send_keys(load_yaml['SystemManager']['password'])

    sleep(1)

    # 權限身分下拉選單
    driver.find_element_by_css_selector("[ng-model='accountModel.authorityText']").click()

    sleep(1)

    # 點擊系統管理員
    driver.find_element_by_xpath("//li[contains(.,'系統管理員')]").click()

    # 前台
    # 消防系統核取方塊
    fireProtectionCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/input")
    # 門禁系統核取方塊
    accessControlCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/input")

    # 後台
    # 設備管理核取方塊
    deviceManageCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[1]/input")
    # 通知管理核取方塊
    notifyManageCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[3]/td[1]/input")

    # 點擊各核取方塊
    # 前台
    fireProtectionCheckBox.click()
    accessControlCheckBox.click()
    # 後台
    deviceManageCheckBox.click()
    notifyManageCheckBox.click()

    # 點擊確定按鈕
    driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()
    sleep(1)


def creatNormalManager(driver):
    # ------------------ 一般管理員 ----------------------
    # 姓名
    # 姓名編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(load_yaml['NormalManager']['name'])
    # 登入帳號
    # 登入帳號欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.loginId']").send_keys(load_yaml['NormalManager']['account'])

    sleep(1)

    # 電話
    # 電話欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.phone']").send_keys(load_yaml['NormalManager']['phone'])

    sleep(1)

    # 信箱
    # 信箱編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.email']").send_keys(load_yaml['NormalManager']['email'])

    sleep(1)

    # 密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").send_keys(load_yaml['NormalManager']['password'])

    sleep(1)

    # 確認密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").send_keys(load_yaml['NormalManager']['password'])

    sleep(1)

    # 權限身分下拉選單
    driver.find_element_by_css_selector("[ng-model='accountModel.authorityText']").click()

    # 點擊一般管理者
    driver.find_element_by_xpath("//li[contains(.,'一般管理員')]").click()

    # 前台
    # 消防系統核取方塊
    fireProtectionCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/input")
    # 門禁系統核取方塊
    accessControlCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/input")

    # 後台
    # 設備管理核取方塊
    deviceManageCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[2]/td[1]/input")
    # 通知管理核取方塊
    notifyManageCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr[3]/td[1]/input")

    # 點擊各核取方塊
    # 前台
    fireProtectionCheckBox.click()
    accessControlCheckBox.click()
    # 後台
    deviceManageCheckBox.click()
    notifyManageCheckBox.click()
    # 點擊確定按鈕
    driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()
    sleep(1)



def creatNormalUser(driver):
    # ------------------ 一般使用者 ----------------------
    # 姓名
    # 姓名編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.userName']").send_keys(load_yaml['NormalUser']['name'])
    # 登入帳號
    # 登入帳號欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.loginId']").send_keys(load_yaml['NormalUser']['account'])

    sleep(1)

    # 電話
    # 電話欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.phone']").send_keys(load_yaml['NormalUser']['phone'])

    sleep(1)

    # 信箱
    # 信箱編輯欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.email']").send_keys(load_yaml['NormalUser']['email'])

    sleep(1)

    # 密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.password']").send_keys(load_yaml['NormalUser']['password'])

    sleep(1)

    # 確認密碼欄位
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").clear()
    driver.find_element_by_css_selector("[ng-model='accountModel.confirmPassword']").send_keys(load_yaml['NormalUser']['password'])

    sleep(1)

    # 權限身分下拉選單
    driver.find_element_by_css_selector("[ng-model='accountModel.authorityText']").click()

    sleep(1)

    # 點擊一般使用者
    driver.find_element_by_xpath("//li[contains(.,'一般使用者')]").click()

    # 前台
    # 消防系統核取方塊
    fireProtectionCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/input")
    # 門禁系統核取方塊
    accessControlCheckBox = driver.find_element_by_xpath("//*[@id='CreateEditAccountModal']/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/input")

    # 點擊各核取方塊
    fireProtectionCheckBox.click()
    accessControlCheckBox.click()

    # 點擊確定按鈕
    driver.find_element(By.CSS_SELECTOR, "[ng-click='submitModel()']").click()
    sleep(1)