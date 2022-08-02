from common import system_tab
import pytest
from time import sleep

@pytest.mark.usefixtures("driver")
def test_backEndLeftSideBar(driver):
    """
        @type driver: selenium.webdriver.remote.webdriver.WebDriver
        @:type driver: selenium.webdriver.remote.webdriver.WebDriver
        :return:
        """
    # @:type driver: selenium.webdriver.remote.webdriver
    # @type driver: selenium.webdriver.remote.webdriver.WebDriver
    # @:type driver: selenium.webdriver.remote.webdriver.WebDriver



    # ----------------------- 左側欄收合狀態 -----------------------
    # 驗證後台左邊側邊攔 點擊正常進入該頁面

    system_tab.login(driver)
    # 點擊子系統資訊，進入後台管理頁面
    driver.find_element_by_xpath("/html/body/div[2]/div/ul[1]/div/div/li[1]").click()

    driver.find_element_by_class_name("sidebar-collapse-button").click()

    # # 驗證後台左側欄收合為開啟狀態
    # assert driver.find_element_by_class_name("page-sidebar").is_displayed()
    # # 點擊後台左側欄收合按鈕，收起左側欄
    # driver.find_element_by_class_name("sidebar-collapse-button").click()
    # # 驗證後台左側欄收合為收起狀態
    # assert driver.find_element_by_class_name("page-sidebar collapsed").is_displayed()
    # # 點擊後台左側欄收合按鈕，開啟左側欄
    # driver.find_element_by_class_name("sidebar-collapse-button").click()
    # # 驗證後台左側欄收合為開啟狀態
    # assert driver.find_element_by_class_name("page-sidebar").is_displayed()



    # ----------------------- 左側欄各頁面進入狀態 -----------------------
    # 頁面標題

    # 點擊子系統資訊
    subSystemInformation = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[2]")
    subSystemInformation.click()
    sleep(1)

   # ---------------------------------------- 子系統資訊 ----------------------------------------
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '子系統資訊'
    # 驗證子系統資訊列表標題，是否在子系統資訊頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '子系統列表'

    # ---------------------------------------- 設備資訊 ----------------------------------------
    # 點擊設備資訊
    devicesInformation = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[3]")
    devicesInformation.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '設備資訊'
    # 驗證設備資訊列表標題，是否在設備資訊頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[3]/div[2]/h2").text == '設備列表'

    # ---------------------------------------- 運轉紀錄 ----------------------------------------

    # 點擊運轉紀錄
    operationRecord = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[4]")
    operationRecord.click()
    # 驗證頁面標題，是否在運轉紀錄頁面
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '運轉紀錄'

    # ---------------------------------------- 運轉時數設定 ----------------------------------------

    # 點擊運轉時數設定
    operatingTime = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[5]")
    operatingTime.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '運轉時數'
    # 驗證運轉時數列表標題，是否在運轉時數設定頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '運轉時數列表'

    # ---------------------------------------- 通訊錄設定 ----------------------------------------

    # 點擊通訊錄設定
    directory = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[7]")
    directory.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '通訊錄設定'
    # 驗證聯絡人列表標題，是否在通訊錄設定頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[2]/h2").text == '聯絡人列表'


    # ---------------------------------------- 通知事件設定 ----------------------------------------
    # 點擊通知事件設定，開啟下拉式選單
    notificationEvent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[8]/a")
    notificationEvent.click()
    # 點擊設備事件通知
    deviceEventNotifi = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[8]/ul/li[1]")
    deviceEventNotifi.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "通知事件設定"
    # 驗證設備事件通知列表標題，是否在設備事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '設備事件通知列表'
    sleep(2)
    # 點擊數值事件通知
    valueEventNotifi = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[8]/ul/li[2]")
    valueEventNotifi.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "通知事件設定"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '數值事件通知列表'
    sleep(2)
    # 點擊複合式條件事件通知
    compoundEventNotifi = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[8]/ul/li[3]")
    compoundEventNotifi.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "通知事件設定"
    # 驗證複合式條件事件通知列表標題，是否在複合式條件事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '複合式條件事件通知列表'


    # ---------------------------------------- 平面圖設定 ----------------------------------------
    # 點擊平面圖設定
    plan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[10]")
    plan.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '平面圖設定'
    # 驗證平面圖設定列表標題，是否在平面圖設定頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div[2]/h2").text == '平面圖列表'

    # ---------------------------------------- 平面圖設備設定 ----------------------------------------
    # 點擊平面圖設備設定
    planDevices = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[11]")
    planDevices.click()
    # 頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == '平面圖設備設定'

    # ---------------------------------------- 事件設定 ----------------------------------------
    # 點擊事件設定
    eventNotifi = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[13]/a")
    eventNotifi.click()

    # 點擊設備事件
    devicesEvent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[13]/ul/li[1]")
    devicesEvent.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件設定"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '設備事件列表'

    # 數值事件
    valueEvent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[13]/ul/li[2]/a")
    valueEvent.click()
    # 驗證頁面標題
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件設定"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '數值事件列表'

    # 複合式事件
    compoundEvent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[13]/ul/li[3]/a")
    compoundEvent.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件設定"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '複合式條件事件列表'

    # ---------------------------------------- 事件類別 ----------------------------------------
    eventClass = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[14]/a")
    eventClass.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件類別"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '事件類別列表'

    # ---------------------------------------- 事件紀錄 ----------------------------------------
    eventRecord = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[15]")
    eventRecord.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件紀錄"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '事件紀錄列表'

    # ---------------------------------------- 動作群組 ----------------------------------------
    actionGroup = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[17]")
    actionGroup.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "事件紀錄"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '動作群組列表'

    # ---------------------------------------- 連動設定 ----------------------------------------
    linkEvent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[18]")
    linkEvent.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "連動設定"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '連動列表'

    # ---------------------------------------- 連動時間排程 ----------------------------------------
    linkTime = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[19]")
    linkTime.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "連動時間排程"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '時間排程列表'


    # ---------------------------------------- 帳號管理 ----------------------------------------
    accManage = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[21]")
    accManage.click()
    systemTitle = driver.find_element_by_xpath('//*[@id="PageContainer"]/div[1]/h1')
    assert systemTitle.text == "帳號管理"
    # 驗證數值事件通知列表標題，是否在數值事件通知頁面
    assert driver.find_element_by_xpath("//*[@id='PageContainer']/div[2]/div/h2").text == '帳號列表'