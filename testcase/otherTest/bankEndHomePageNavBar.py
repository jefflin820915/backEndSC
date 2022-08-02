from common import system_tab
from common import menu_rightSideBar
import pytest
import time


@pytest.mark.usefixtures("driver")
def test_bankEndHomePageNavBar(driver):
    """
    @type driver: selenium.webdriver.remote.webdriver.WebDriver
    @:type driver: selenium.webdriver.remote.webdriver.WebDriver
    :return:
    """
    # @:type driver: selenium.webdriver.remote.webdriver
    # @type driver: selenium.webdriver.remote.webdriver.WebDriver
    # @:type driver: selenium.webdriver.remote.webdriver.WebDriver


    # 驗證後台右上角導覽列跳轉以及點擊功能是否正常
    # 調用登入方法,登入admin帳戶,進入後台首頁
    system_tab.login(driver)


    # --------------------------- 後台首頁右上角導覽列 使用者---------------------------
    # 點擊右上角導覽列
    # 點擊導覽列"使用者"
    navBarUser = driver.find_element_by_xpath("/html/body/ul/li[4]/div/a")
    navBarUser.click()

    # 驗證使用者名稱是否為登入之該使用者
    # 後台左側導覽列使用者名稱
    leftNavBarUserName = driver.find_element_by_xpath("/html/body/div[1]/div[2]/span[2]")
    # 後台右上角使用者下拉使用者名稱
    navBarUserName = driver.find_element_by_xpath("/html/body/ul/li[4]/div/ul/li[1]/div/span[1]")
    # 驗證使用者名稱是否為登入之該使用者
    assert leftNavBarUserName.text == navBarUserName.text

    oldPws = '7ujm*IK<'
    newPws = '7ujm*IK<'
    # 點擊下拉選單"修改密碼"
    driver.find_element_by_xpath("/html/body/ul/li[4]/div/ul/li[2]").click()
    # 舊密碼欄位
    driver.find_element_by_xpath("//*[@id='ChangePasswordModal']/div/div/form/div[2]/div/div[2]/div[2]/input").send_keys(oldPws)

    # 輸入新密碼
    # 新密碼欄位
    driver.find_element_by_xpath("//*[@id='ChangePasswordModal']/div/div/form/div[2]/div/div[4]/div[2]").send_keys(newPws)
    # 確認新密碼欄位
    driver.find_element_by_xpath("//*[@id='ChangePasswordModal']/div/div/form/div[2]/div/div[5]/div[2]").send_keys(newPws)
    # 確定按鈕
    driver.find_element_by_xpath("//*[@id='ChangePasswordModal']/div/div/form/div[3]/button[2]").click()

    # 點擊導覽列"使用者"
    navBarUser.click()
    # 點擊下拉選單"登出"
    driver.find_element_by_xpath("/html/body/ul/li[4]/div/ul/li[3]/a").click()

    # 驗證登入按鈕是否存在，確認是否在登入頁面
    assert driver.find_element_by_xpath("//*[@id='LoginForm']/div/div[4]/div/button").is_displayed()
    # 調用登入方法來登入
    system_tab.login(driver)
    # 調用進入後台方法進後台
    menu_rightSideBar.backEnd(driver)
    # 驗證功能列表是否存在，確認是否在後台首頁
    assert driver.find_element_by_xpath("/html/body/div[2]/div").is_displayed()


    # --------------------------- 後台首頁右上角導覽列 通知---------------------------
    # 點擊導覽列"通知"按鈕
    driver.find_element_by_xpath("/html/body/ul/li[3]").click()
    # 驗證事件處理列表標題是否在事件列表頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[1]/h1").text == '事件處理狀態列表'


    # --------------------------- 後台首頁右上角導覽列 前台---------------------------
    # 點擊導覽列"前台"
    driver.find_element_by_xpath("//*[@id='PageContainer']/div[1]/ul[1]/li[2]").click()
    # 驗證前台首頁平面部屬按鈕,是否正在前台首頁
    assert driver.find_element_by_xpath("/html/body/div[2]/button").text == '平面部署' or driver.find_element_by_xpath("/html/body/div[3]/ul/li[12]/button").text == "平面部署"
    # 調用進入後台方法，進入後台
    menu_rightSideBar.backEnd(driver)


    # --------------------------- 後台首頁右上角導覽列 首頁---------------------------
    # 點擊導覽列"通知"按鈕
    driver.find_element_by_xpath("/html/body/ul/li[3]").click()
    # 點擊導覽列"首頁"按鈕
    driver.find_element_by_xpath("//*[@id='PageContainer']/div[1]/ul[1]/li[1]").click()

    # 獲取當前時間，與前台首頁左邊導覽列時間相比，驗證是否在前台首頁
    localtime = time.localtime()
    resultTime = time.strftime("%Y/%m/%d %I:%M", localtime)
    assert driver.find_element_by_xpath("//*[@id='nowTime']").text == resultTime



    # --------------------------- 後台首頁左側導覽列 ---------------------------
    # 後台首頁左側導覽列
    # 點擊登出按鈕
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/button[1]").click()
    # 驗證登入按鈕是否存在，確認是否在登入頁面
    assert driver.find_element_by_xpath("//*[@id='LoginForm']/div/div[4]/div/button").is_displayed()
    # 調用登入方法來登入
    system_tab.login(driver)
    # 調用進入後台方法進後台
    menu_rightSideBar.backEnd(driver)
    # 獲取當前時間，與前台首頁左邊導覽列時間相比，驗證是否在前台首頁
    assert driver.find_element_by_xpath("//*[@id='nowTime']").text == resultTime

    # 點擊前往前台按鈕
    # 驗證前台首頁平面部屬按鈕,是否正在前台首頁
    assert driver.find_element_by_xpath("/html/body/div[2]/button").text == '平面部署' or driver.find_element_by_xpath("/html/body/div[3]/ul/li[12]/button").text == "平面部署"
    # 調用進入後台方法，進入後台
    menu_rightSideBar.backEnd(driver)
    # 獲取當前時間，與前台首頁左邊導覽列時間相比，驗證是否在前台首頁
    assert driver.find_element_by_xpath("//*[@id='nowTime']").text == resultTime